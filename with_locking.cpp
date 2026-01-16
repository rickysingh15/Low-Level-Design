
#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <mutex>

using namespace std;

struct Node
{
    string val;
    Node * parent;
    int uid;
    // int anc_locked; 
    unordered_set<Node*> desc_locked;
    vector<Node*> children;
    std::mutex mtx;
    
    Node(string v, Node * p)
    {
        val = v;
        parent = p;
        // anc_locked = 0;
        uid = -1;
    }
    
    void addChild(Node * node)
    {
        children.push_back(node);
    }
};


class LockingTree
{
    private:
    Node * root;
    unordered_map<string, Node*> vmap;
    
    public:
    LockingTree(int n, int m, vector<string> &nodes)
    {
        root = new Node(nodes[0], nullptr);
        vmap[nodes[0]] = root;
        buildTree(m, nodes);
    }
    
    void buildTree(int m, vector<string> &nodes)
    {
        queue<Node*> q;
        q.push(this->root);
        int nextChild = 1;
        while(!q.empty())
        {
            Node * node = q.front();
            q.pop();

            if(nextChild >= nodes.size()) continue;
            for(int i=nextChild; i<nextChild+m; i++)
            {
                Node * child = new Node(nodes[i], node);
                vmap[nodes[i]] = child;
                node->addChild(child);
                q.push(child);
            }
            nextChild += m;
        }
    }
    
    Node * getRoot()
    {
        return root;
    }
    
    Node * getNode(string v)
    {
        if(vmap.find(v) == vmap.end()) return nullptr;
        return vmap[v];
    }  
    
    vector<Node *> getPathFromRoot(Node * node)
    {
        vector<Node*> path;
        Node * curr = node;
        while(curr != nullptr)
        {
            path.push_back(curr);
            curr = curr->parent;
        }
        reverse(path.begin(), path.end());
        return path;
    }
    
    
    
    vector<std::unique_lock<std::mutex>> lockPath(vector<Node *> &path)
    {
        vector<std::unique_lock<std::mutex>> guards;
        guards.reserve(path.size());
        for(auto n: path)
        {
            guards.emplace_back(n->mtx);
        }
        return guards;
    }
    
    void lockInternal(Node * node, int id)
    {
        Node * curr = node->parent;
        while(curr != nullptr)
        {
            curr->desc_locked.insert(node);
            curr = curr->parent;
        }
        node->uid = id;
    }
    
    void unlockInternal(Node * node, int id)
    {
        Node * curr = node->parent;
        while(curr != nullptr)
        {
            if(curr->desc_locked.find(node) != curr->desc_locked.end())
            {
                curr->desc_locked.erase(node);
            }
            curr = curr->parent;
        }
        
        node->uid = -1;
    }
    
    
    bool lock(string val, int id)
    {
        Node * node = getNode(val);
        if(node == nullptr) return false;
        
        vector<Node *> path = getPathFromRoot(node);
        vector<std::unique_lock<std::mutex>> guards = lockPath(path);
        
        if(node->uid != -1) return false;
        if(node->desc_locked.size() != 0) return false;
        
        Node * curr = node->parent;
        while(curr != nullptr)
        {
            if(curr->uid != -1) return false;
            curr = curr->parent;
        }
        
        lockInternal(node, id);
        return true;
    }
    
    bool unlock(string val, int id)
    {
        Node * node = getNode(val);
        if(node == nullptr) return false;
        
        vector<Node *> path = getPathFromRoot(node);
        vector<std::unique_lock<std::mutex>> guards = lockPath(path);
        
        if(node->uid == -1) return false;
        if(node->uid != id) return false;
 
        // Node * curr = node->parent;
        // while(curr != nullptr)
        // {
        //     if(curr->desc_locked.find(node) != curr->desc_locked.end())
        //     {
        //         curr->desc_locked.erase(node);
        //     }
        //     curr = curr->parent;
        // }
        unlockInternal(node, id);     
        return true;
    
    }
    
    bool upgrade(string val, int id)
    {
        Node * node = getNode(val);
        if(node == nullptr) return false;

        vector<Node *> path = getPathFromRoot(node);
        vector<std::unique_lock<std::mutex>> guards = lockPath(path);
        
        if(node->uid != -1) return false;
        
        Node * curr = node->parent;
        while(curr != nullptr)
        {
            if(curr->uid != -1) return false;
            curr = curr->parent;
        }
        
        if(node->desc_locked.size() == 0) return false;
        
        vector<Node*> locked_descendents(node->desc_locked.begin(), node->desc_locked.end());
        for(auto ld: locked_descendents)
        {
            if(ld->uid != id) return false;
            unlockInternal(ld, id);
        }
        
        lockInternal(node, id);
        return true;    
    }
    
};


int main() {
    int N = 0;
    int M = 0;
    int Q = 0;
    vector<string> nodes;
    cin>>N>>M>>Q;
    for(int i=0; i<N; i++)
    {
        string node = "";
        cin>>node;
        nodes.push_back(node);
    }
    
    LockingTree * t = new LockingTree(N,M,nodes);
    cout<<endl;
    cout<<endl;
    vector<bool> result;
    for(int i=0; i<Q; i++)
    {
        int opcode = -1;
        string node = "";
        int id = -1;
        cin>>opcode>>node>>id;
        bool res = false;
        switch(opcode)
        {
            case 1:
                cout<<"lock node "<<node<<" by "<<id<<endl;
                res = t->lock(node, id);
                if(res) cout<<"success"<<endl;
                else cout<<"failed"<<endl;
                result.push_back(res);
                break;
            case 2:
                cout<<"unlock node "<<node<<" by "<<id<<endl;
                res = t->unlock(node, id);
                if(res) cout<<"success"<<endl;
                else cout<<"failed"<<endl;
                result.push_back(res);
                break;
            case 3:
                cout<<"upgrade node "<<node<<" by "<<id<<endl;
                res = t->upgrade(node, id);
                if(res) cout<<"success"<<endl;
                else cout<<"failed"<<endl;
                result.push_back(res);
                break;
        }
    }
    
}
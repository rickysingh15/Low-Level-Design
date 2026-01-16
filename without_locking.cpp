
#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <unordered_map>
#include <algorithm>

using namespace std;

struct Node
{
    string val;
    Node * parent;
    int uid;
    int anc_locked; 
    int desc_locked;
    vector<Node*> children;
    
    Node(string v, Node * p)
    {
        val = v;
        parent = p;
        anc_locked = 0;
        desc_locked = 0;
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
    
    void updateDesc(Node * node, int v)
    {
        vector<Node *> children = node->children;
        for(int i=0; i<children.size(); i++)
        {
            children[i]->anc_locked += v;
            updateDesc(children[i], v);
        }
    }
    
    bool checkDesc(Node * node, int &id, vector<Node *> &lockedNodes)
    {
        if(node->uid != -1)
        {
            if(node->uid != id) return false;
            lockedNodes.push_back(node);
        }
        
        if(node->desc_locked == 0) return true;
        
        vector<Node*> children = node->children;
        for(int i=0; i<children.size(); i++)
        {
            if(!checkDesc(children[i],id,lockedNodes)) return false;
        }
        return true;
    }
    
    bool lock(string val, int id)
    {
        Node * node = getNode(val);
        if(node == nullptr) return false;
        
        
        if(node->uid != -1) return false;
        if(node->anc_locked != 0) return false;
        if(node->desc_locked != 0) return false;
        
        Node * curr = node->parent;
        while(curr != nullptr)
        {
            curr->desc_locked++;
            curr = curr->parent;
        }
        
        updateDesc(node, 1);
        

        node->uid = id;
        return true;
    }
    
    bool unlock(string val, int id)
    {
        Node * node = getNode(val);
        if(node == nullptr) return false;
        
        if(node->uid == -1) return false;
        if(node->uid != id) return false;
 
        Node * curr = node->parent;
        while(curr != nullptr)
        {
            curr->desc_locked--;
            curr = curr->parent;
        }
        
        updateDesc(node, -1);
        
        node->uid = -1;
        return true;
    
    }
    
    bool upgrade(string val, int id)
    {
        Node * node = getNode(val);
        if(node == nullptr) return false;

        if(node->uid != -1) return false;
        if(node->anc_locked != 0) return false;
        if(node->desc_locked == 0) return false;
        
        vector<Node*> lockedNodes;
        for(auto d: node->children)
        {
            if(!checkDesc(d, id, lockedNodes)) return false;
        }
        
        for(auto ln: lockedNodes)
        {
            bool r = unlock(ln->val, id);
        }
        
        lock(node->val, id);
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
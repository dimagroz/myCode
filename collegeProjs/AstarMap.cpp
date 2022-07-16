 #include <algorithm>
#include <climits>
#include <iostream>
#include <string>
#include <unordered_map>
#include <map>
#include <set>
#include <vector>
#include <limits.h> 
#include <stdio.h> 
#include <math.h>

/*Dimitry Grozny -College project 5/20
Astar-shortest path finder
For my project I used the A-star concept to create an algorithm in C++ that finds the shortest distance between two nodes on a graph. Every node has an x,y coordinate, and the weight between two nodes is found using the distance formula a^2 +b^2=c^2. The values are trunked down to an int type to simplify the presentation. My project allows for both removal/attachment of links between any nodes. The graph contains 10 nodes. The admissible heuristic is the distance between any node and the destination node, and I used maps and sets to create a time optimal algorithm.
*/



using namespace std;

void buildFull(map<int, pair<int, int>> loc);
void build_graph(map<int, pair<int, int>> loc, vector<pair<int, int>> connect);
void disconnect(int x, int y);
void connect2(int x, int y);
void astar(int src, int dst);
int hueristic(int point1, int point2);
void print(int** graphed);



int graphsize = 10;
map <string, int> names;
map<int, string> nums;
map< int, pair<int, int> > loc;
int** full_graph = new int*[graphsize];
int** graph = new int*[graphsize];
int main() {

	for (int i = 0; i < graphsize; i++)
	{
		graph[i] = new int[graphsize];
		for (int n = 0; n < graphsize; n++)
		{
			graph[i][n] = 0;
		}
	}

	
	string input_names[] = { "a","b","c","d","e","f","g","h","i","j" }; //nodes
	pair<int, int> input_loc[] = { {15,-15},{25,-50},{-45,-50},{-25,0},{0,0},{20,15},{10,40},{-15,50},{-25,25},{50,-25} }; //(x,y) cordinates
	//vector <pair<int, int>> connect = {{0,1},{1,2},{1,3},{5,8}};
	vector <pair<string, string>> str_connect = { {"a","e"},{"a","c"},{"a","b"},{"b","d"},{"b","j"},{"c","d"},{"e","f"},{"e","g"},{"f","g"},{"g","h"},{"h","i"} };

	for (int i = 0; i < 10; i++)
	{
		names[input_names[i]] = i;
		nums[i] = input_names[i];
		loc[i] = input_loc[i];
	}

	vector <pair<int, int>> connect;
	for (auto con : str_connect)
	{
		connect.push_back(make_pair(names[con.first], names[con.second]));
	}

	buildFull(loc);

	string entered = "";
	getline(cin, entered);

	

	string point1;
	string point2;
	string command;
	string word = "";

	

	build_graph(loc, connect);
	bool point_1;
	bool point_2;
	bool res;
	while (entered != "")
	{
		res = true;
		for (auto x : entered)
		{
			if (x == ' ')
			{
				res = false;
				if (command == "") {
					command = word;
					word = "";
				}
			}
			else if (x == ',')
			{
				point1 = word;
				word = "";
			}
			else
			{
				word = word + x;
			}
		}
		if (res)
			command = word;
		else
			point2 = word;
		//cout << point1 << ',' << point2 << endl;
		word = "";

		point_1 = false;
		point_2 = false;

		if (names.find(point1) != names.end())
			point_1 = true;
		if (names.find(point2) != names.end())
			point_2 = true;

		//if (command == "reset")
			//reset(connect);
		if (command == "graph")
		{
			print(graph);
		}
		else
		{
			if (point_1 && point_2)
			{
				if (command == "path")
				{
					//build_graph(loc, connect);
					astar(names[point1], names[point2]);
				}
				else if (command == "connect")
				{
					connect2(names[point1], names[point2]);
				}
				else if (command == "disconnect")
				{
					disconnect(names[point1], names[point2]);
				}
				else cout << "unknown command";
			}
			else cout << "unknown command";
		}
		point1 = "";
		point2 = "";
		command = "";
		word = "";
		entered = "";
		cout << endl;
		getline(cin, entered);
	}



	build_graph(loc, connect);

	//print(graph);
	cout << endl<<endl;
	
}


void buildFull(map<int, pair<int, int>> loc) 
{

	for (int i = 0; i < graphsize; i++)
	{
		full_graph[i] = new int[graphsize];

		for (int n = 0; n < graphsize; n++)
		{
			int x1 = loc[i].first;
			int x2 = loc[n].first;
			int y1 = loc[i].second;
			int y2 = loc[n].second;
			int dis = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
			full_graph[i][n] = dis;
		}
	}

	//return full_graph;
}


void build_graph(map<int, pair<int, int>> loc, vector<pair<int,int>> connect)
{
	for(int i = 0;i<connect.size();i++)
	{
		graph[connect[i].first][connect[i].second] = full_graph[connect[i].first][connect[i].second];
		graph[connect[i].second][connect[i].first] = full_graph[connect[i].first][connect[i].second];
	}
}



void disconnect(int x, int y)
{
	graph[x][y] = 0;
	graph[y][x] = 0;

	cout << "dis-connected\n";
}

void connect2(int x, int y)
{
	graph[x][y] = full_graph[x][y];
	graph[y][x] = full_graph[x][y];
	//cout << full_graph[x][y]<<endl;
	//cout << graph[x][y]<<endl;
	cout << "connected\n";
}

void astar(int src, int dst)
{
	map<int, pair<int, int>> disthuer; //stores the value of distance + huersistic at each 
	map<int, int> dist; // b, dist
	set<pair<int, int>> mapped; //stores the a-b  as the next
	map<int, int> mapped2;
	dist[src] = 0;
	int g_dist;
	int cur = src;
	int total_d;
	bool valid_path = true;


	while (cur != dst && valid_path)
	{
		valid_path = false;
		for (int i = 0; i < graphsize; i++)
		{
			g_dist = graph[cur][i];
			if (g_dist != 0)
			{
				total_d = dist[cur] + g_dist;
				if (dist.find(i) == dist.end() || total_d < dist[i])
				{
					disthuer[total_d + hueristic(i, dst)] = make_pair(cur, i);
					dist[i] = total_d;
				}
			}
		}

		for (auto x : disthuer)
		{
			if (mapped.find(x.second) == mapped.end())
			{
				cout << "expand " << nums[x.second.first] << " -> " << nums[x.second.second] << " huer=" << hueristic(x.second.second, dst) << " dist=" << dist[x.second.second] << " combined=" << hueristic(x.second.second, dst) + dist[x.second.second] << endl;
				mapped.insert(x.second);
				mapped2[x.second.second] = x.second.first;
				cur = x.second.second;
				valid_path = true;
				break;
			}
		}
	}

	if (!valid_path)
		cout << "no valid path found\n";
	else
	{

		cout << "shortest path\n";

		vector<int> order;
		int let = dst;
		while (let != src)
		{
			order.push_back(let);
			let = mapped2[let];
		}
		order.push_back(let);

		for (int i = order.size() - 1; i > 0; i--)
			cout << nums[order[i]] << " -> ";
		cout << nums[order[0]] << endl;
		cout << "total distance = " << dist[dst]<< " units" << endl;
	}
}

int hueristic(int point1, int point2)
{

	int x1 = loc[point1].first;
	int x2 = loc[point2].first;
	int y1 = loc[point1].second;
	int y2 = loc[point2].second;

	int dis = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2)); //distance formula
	//cout << dis;
	return dis;
}

void print(int** graphed)
{
	set<pair<int, int>> printed;
	for (int i = 0; i < 10; i++)
	{
		for (int n = 0; n < 10; n++)
		{
			//cout << graphed[i][n] << ' ';
			if (graphed[i][n])
			{
				if (printed.find(make_pair(i,n)) == printed.end())
				{
					cout << nums[i] << " -> " << nums[n] << ", dis=" << graphed[i][n] << endl;
					printed.insert(make_pair(n,i ));
				}
			}
		}
		//cout << endl;
	}
}


/*
BST and A* in C++ -> main.cpp
    Main entry point to the program
Author: Abhigya Raval
*/

#include <iostream>
#include <vector>
#include <string>
#include <random>
using namespace std;

/* Classes */
// Map class to define the environment that the robot can move in
class Map
{
    private:
    int map_height = 5;
    int map_width = 6;
    vector <vector <int> > grid = {
        {0,1,0,0,0,0},
        {0,1,0,0,0,0},
        {0,1,0,1,0,0},
        {0,1,0,1,0,0},
        {0,0,0,1,1,0}
    };

    public:
    // Constructor that takes in requested map dimensions and creates a map grid
    // Map (int in_height, int in_width)
    // {
    //     map_height = in_height;
    //     map_width = in_width;
    // }
    vector<vector<int>> get_grid(void){
        return grid;
    }
};

class Planner
{
    private:
    int start[2];
    int goal[2];
    int grid_size[2] = {5,6};
    int cost = 1;
    vector <vector<int>> movements = {
        {-1,0}, //up
        {0,1},  //right
        {0,-1}, //left
        {1,0}   //down
    };
    string movementarrow = {'^', '>', '<', 'v'};


    public:
    // Constructor for start and goal inputs
    Planner (int _start_x, int _start_y, int _goal_x, int _goal_y)
    {
        start[0] = _start_x;
        start[1] = _start_y;
        goal[0] = _goal_x;
        goal[1] = _goal_y;
    }

    void print_inputs(void){
        cout << "Start is: " << start[0] << start[1] << endl;
        cout << "Goal is: " << goal[0] << goal[1] << endl;
        cout << movementarrow[0] << endl;
    }
};
/*-------------------------------------------------------------------------------------------------*/

/* Function declarations */
// Template function to print any 2D vector
template <typename T> //  Template to enable dynamic input
void print2Dvector(T vec){
    int height = vec.size();
    int width = vec[0].size();
    cout << "Height, Width: " << height << ", " << width << endl;
    for (int i = 0; i < height; i++){
        cout << "[ ";
        for (int j = 0; j < width; j++){
            cout << vec[i][j];
        }
        cout << " ]" << endl;
    }
}

// Search function takes in a Map object and a Planner object and return the best path found
struct path // Struct to return multiple outputs
{
    vector <int> path;
    string path_sym[];
};

path search (Map map, Planner planner){

}

/*-------------------------------------------------------------------------------------------------*/



/* Main function */
int main(int argc, char *argv[])
{
    /*
    // Printing out the cmdline passed arguments

    cout << "You have entered " << argc << " arguments:" << "\n";
  
    for (int i = 0; i < argc; ++i)
        cout << argv[i] << "\n";
    */
    Planner planner(0,0,1,1);
    planner.print_inputs();
   

    Map map;
    cout << endl << endl;
    vector<vector<int>> grid1 = map.get_grid();

    print2Dvector(map.get_grid());
    return 0;
}


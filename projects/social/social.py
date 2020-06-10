import random
from collections import deque

class User:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f'{self.name}'

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # Add users
        for i in range(0, num_users):
            self.add_user(f'User {i}')

        # Create friendships
        # Generate all possible friendship combinations
        possible_friendships = []

        # Avoid duplicates by ensuring first number is smaller than second
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))
        
        # Shuffle possible friendships
        random.shuffle(possible_friendships)

        # Create friendships for first X pairs of the list
        # X is determined by: num_users * avg_friendships // 2
        # Divide by 2 because each add_friendship() makes 2 friendships
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.

        Understand
        ----------
        Connected Components

        Parts of the graph that are connected, 
        but disjoint from other parts of the graph

        To count connected components:
            For each node:
                If node not visited:
                    Traverse from that node
                    Increment counter

        BFS for shortest path
        we will not know until traversal how many degrees we can go

        self.friendships is adjacency set
        - key is node, value is set of neighbors
        self.users is set of all nodes

        Plan
        ----------
        visited dictionary - key: user, value: path
        use deque to search friends
        store path, which lengthens with each degree of separation

        start at input user
        initial path is []

        for each dequeue'd user:
            if not in visited:
                increment path, adding self
                add to visited (user: path)
                enqueue each of user's friend with path (friend, path)

        return visited
        """
        visited = {}  # Note that this is a dictionary, not a set
        q = deque()
        q.append((user_id, []))

        while len(q) > 0:
            user, path = q.popleft()

            if user not in visited:
                path.append(user)
                visited[user] = path

                for friend in self.friendships[user]:
                    q.append((friend, path.copy()))

        return visited
    # O(V + E)

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(100, 3)
    print(sg.friendships)
    print(sg.users)
    connections = sg.get_all_social_paths(1)
    print(connections)

    # sg.add_user(1)
    # sg.add_user(2)
    # sg.add_user(3)
    # sg.add_user(4)
    # sg.add_user(5)
    # sg.add_user(6)
    # sg.add_user(7)
    # sg.add_user(8)
    # sg.add_user(9)
    # sg.add_user(10)
    # sg.add_friendship(1, 8)
    # sg.add_friendship(1, 10)
    # sg.add_friendship(1, 5)
    # sg.add_friendship(2, 10)
    # sg.add_friendship(2, 5)
    # sg.add_friendship(2, 7)
    # sg.add_friendship(3, 4)
    # sg.add_friendship(4, 9)
    # sg.add_friendship(5, 8)
    # sg.add_friendship(6, 10)
    # connections = sg.get_all_social_paths(1)
    # print(connections)
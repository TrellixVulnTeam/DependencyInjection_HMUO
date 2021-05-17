fuser 5000/tcp | awk '{print $0}' | xargs kill -9

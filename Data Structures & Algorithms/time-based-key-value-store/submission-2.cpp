class TimeMap {
public:
    TimeMap() {}

    void set(string key, string value, int timestamp) {
        timeMap[key].emplace_back(timestamp, value);
    }

    string get(string key, int timestamp) {
        auto it = timeMap.find(key);
        if (it == timeMap.end()) return "";

        const auto &arr = it->second;
        int l = 0, r = (int)arr.size() - 1;
        int idx = -1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (arr[mid].first <= timestamp) {
                idx = mid;
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return idx == -1 ? "" : arr[idx].second;
    }

private:
    unordered_map<string, vector<pair<int, string>>> timeMap;
};
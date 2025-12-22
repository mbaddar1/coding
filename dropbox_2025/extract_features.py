"""
Problem: User Session Feature Extraction

You are given a list of raw user events.
Each event is represented as a tuple:

    (user_id, timestamp_sec, event_type, value)

The events are NOT guaranteed to be sorted.

--------------------------------------------------
Definitions

- A session is a sequence of events for the same user such that the time
  difference between consecutive events is <= 1800 seconds (30 minutes).

- If the time difference between two consecutive events for a user is
  > 1800 seconds, a new session starts.

- A session containing only one event has a duration of 0 seconds.

- Session duration is defined as:
      last_event_timestamp - first_event_timestamp

--------------------------------------------------
Task

For each user, compute the following features across all their sessions:

1) num_sessions
   Total number of sessions for the user.

2) avg_session_duration_sec
   Average session duration in seconds.

3) most_common_event_type
   The event type that occurs most frequently for the user.
   If there is a tie, return the lexicographically smallest event type.

4) purchase_rate
   Fraction of sessions that contain at least one "purchase" event.

   purchase_rate = (# sessions with a purchase) / num_sessions

--------------------------------------------------
Function Signature

    Event = Tuple[str, int, str, float]

    def extract_user_features(
        events: List[Event]
    ) -> Dict[str, Tuple[int, float, str, float]]:
        Returns:
        {
            user_id: (
                num_sessions,
                avg_session_duration_sec,
                most_common_event_type,
                purchase_rate
            )
        }

--------------------------------------------------
Example 1

Input:
    events = [
        ("u1", 100, "view", 0.0),
        ("u1", 1300, "click", 0.0),
        ("u1", 4000, "purchase", 10.0),
    ]

Explanation:
- Sorted timestamps for u1: [100, 1300, 4000]
- Session 1: [100, 1300] -> duration = 1200
- Session 2: [4000] -> duration = 0
- num_sessions = 2
- avg_session_duration = (1200 + 0) / 2 = 600
- Event counts: view=1, click=1, purchase=1 -> tie -> "click"
- purchase_rate = 1 / 2 = 0.5

Output:
    {
        "u1": (2, 600.0, "click", 0.5)
    }

--------------------------------------------------
Example 2 (Multiple Users)

Input:
    events = [
        ("u1", 100, "view", 0.0),
        ("u1", 200, "view", 0.0),
        ("u2", 300, "click", 0.0),
        ("u2", 2600, "click", 0.0),
        ("u2", 2700, "purchase", 20.0),
    ]

Output:
    {
        "u1": (1, 100.0, "view", 0.0),
        "u2": (2, 50.0, "click", 0.5),
    }

--------------------------------------------------
Example 3 (Tie-breaking and Edge Cases)

Input:
    events = [
        ("u3", 1000, "b", 0.0),
        ("u3", 1200, "a", 0.0),
        ("u3", 1400, "a", 0.0),
        ("u3", 6000, "b", 0.0),
    ]

Output:
    {
        "u3": (2, 200.0, "a", 0.0)
    }

--------------------------------------------------
Constraints & Notes

- Total number of events <= 200,000
- Events may be unsorted
- Each user may have many sessions
- Return floats where appropriate
"""
if __name__=="__main__":
    pass
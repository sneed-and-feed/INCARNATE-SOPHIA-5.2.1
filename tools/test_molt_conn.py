from sophia.gateways.moltbook import MoltbookGateway
import os

def test_connectivity():
    print("--- MOLTBOOK CONNECTIVITY TEST ---")
    g = MoltbookGateway("dummy_key_for_test")
    
    print("\nTesting 'browse_feed'...")
    posts = g.browse_feed("ponderings")
    print(f"Result: {posts}")
    
    print("\nTesting 'post_thought'...")
    res = g.post_thought("Test content from Sophia refactor.")
    print(f"Result: {res}")

if __name__ == "__main__":
    test_connectivity()

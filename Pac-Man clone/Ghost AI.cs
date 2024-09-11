using UnityEngine;

public class GhostController : MonoBehaviour
{
    public float speed = 3.0f;
    private Vector2 direction = Vector2.zero;

    void Start()
    {
        // Initialize ghost direction
        direction = Vector2.left;
    }

    void Update()
    {
        Move();
    }

    void Move()
    {
        transform.Translate(direction * speed * Time.deltaTime);
    }

    // Add more complex AI logic here
}
using UnityEngine;
using System.Collections.Generic;

public class GhostController : MonoBehaviour
{
    public float speed = 3.0f;
    private Vector2 direction = Vector2.zero;
    private List<Vector2> patrolPoints = new List<Vector2>();

    void Start()
    {
        direction = Vector2.left;
        // Initialize patrol points based on maze layout
        // This should be done dynamically based on the generated maze
    }

    void Update()
    {
        Move();
        CheckPatrolPoints();
    }

    void Move()
    {
        transform.Translate(direction * speed * Time.deltaTime);
    }

    void CheckPatrolPoints()
    {
        // Implement logic to change direction when reaching patrol points
        // This will make the ghosts patrol around the maze
    }

    void OnCollisionEnter2D(Collision2D collision)
    {
        if (collision.gameObject.CompareTag("Wall"))
        {
            ChangeDirection();
        }
    }

    void ChangeDirection()
    {
        // Implement logic to change direction when hitting walls
        // This could involve choosing a random valid direction
    }
}
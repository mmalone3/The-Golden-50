using UnityEngine;

public class PacManController : MonoBehaviour
{
    public float speed = 5.0f;
    private Vector2 direction = Vector2.zero;
    private Vector2 nextDirection = Vector2.zero;

    void Update()
    {
        HandleInput();
        Move();
    }

    void HandleInput()
    {
        if (Input.GetKeyDown(KeyCode.UpArrow))
            nextDirection = Vector2.up;
        else if (Input.GetKeyDown(KeyCode.DownArrow))
            nextDirection = Vector2.down;
        else if (Input.GetKeyDown(KeyCode.LeftArrow))
            nextDirection = Vector2.left;
        else if (Input.GetKeyDown(KeyCode.RightArrow))
            nextDirection = Vector2.right;
    }

    void Move()
    {
        if (CanMoveInDirection(nextDirection))
        {
            direction = nextDirection;
        }
        transform.Translate(direction * speed * Time.deltaTime);
    }

    bool CanMoveInDirection(Vector2 dir)
    {
        // Raycast in the desired direction to check for obstacles
        RaycastHit2D hit = Physics2D.Raycast(transform.position, dir, 0.5f);
        return !hit.collider || !hit.collider.CompareTag("Wall");
    }

    void OnTriggerEnter2D(Collider2D collision)
    {
        if (collision.gameObject.CompareTag("Pellet"))
        {
            GameManager.Instance.AddScore(10);
            Destroy(collision.gameObject);
        }
        else if (collision.gameObject.CompareTag("PowerPellet"))
        {
            GameManager.Instance.AddScore(50);
            // Activate power pellet effect
            Destroy(collision.gameObject);
        }
    }
}
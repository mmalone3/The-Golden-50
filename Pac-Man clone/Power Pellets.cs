using UnityEngine;

public class PowerPellet : MonoBehaviour
{
    void OnTriggerEnter2D(Collider2D other)
    {
        if (other.CompareTag("PacMan"))
        {
            // Add logic for power pellet effect
            Destroy(gameObject);
        }
    }
}
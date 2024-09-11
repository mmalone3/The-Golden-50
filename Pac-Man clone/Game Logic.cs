using UnityEngine;

public class GameManager : MonoBehaviour
{
    public int score = 0;

    public void AddScore(int points)
    {
        score += points;
        // Update UI or other game elements
    }

    public void GameOver()
    {
        // Implement game over logic
        Debug.Log("Game Over!");
    }
}
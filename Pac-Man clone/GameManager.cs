using UnityEngine;
using UnityEngine.SceneManagement;

public class GameManager : MonoBehaviour
{
    public static GameManager Instance { get; private set; }
    public int score = 0;
    public int lives = 3;
    public GameObject pacManPrefab;
    public GameObject[] ghostPrefabs;
    public Transform spawnPoint;

    private void Awake()
    {
        if (Instance == null)
        {
            Instance = this;
        }
        else if (Instance != this)
        {
            Destroy(gameObject);
        }
    }

    public void AddScore(int points)
    {
        score += points;
        Debug.Log($"Current Score: {score}");
    }

    public void LoseLife()
    {
        lives--;
        if (lives <= 0)
        {
            GameOver();
        }
        else
        {
            ResetLevel();
        }
    }

    public void GameOver()
    {
        Debug.Log("Game Over!");
        SceneManager.LoadScene(SceneManager.GetActiveScene().name);
    }

    public void ResetLevel()
    {
        Instantiate(pacManPrefab, spawnPoint.position, Quaternion.identity);
        foreach (var ghostPrefab in ghostPrefabs)
        {
            Instantiate(ghostPrefab, spawnPoint.position, Quaternion.identity);
        }
    }
}
using UnityEngine;
using System.Collections.Generic;

public class MazeGenerator : MonoBehaviour
{
    public int width = 21;
    public int height = 29;
    public GameObject wallPrefab;
    public GameObject pelletPrefab;
    public GameObject powerPelletPrefab;

    private void Start()
    {
        GenerateMaze();
    }

    private void GenerateMaze()
    {
        // Implement maze generation algorithm (e.g., recursive backtracking)
        // Create walls, pellets, and power pellets based on the generated maze
        // This is a simplified placeholder
        for (int x = 0; x < width; x++)
        {
            for (int y = 0; y < height; y++)
            {
                if (x == 0 || y == 0 || x == width - 1 || y == height - 1)
                {
                    Instantiate(wallPrefab, new Vector3(x, y, 0), Quaternion.identity);
                }
                else if (Random.value > 0.7f)
                {
                    Instantiate(pelletPrefab, new Vector3(x, y, 0), Quaternion.identity);
                }
                else if (Random.value > 0.95f)
                {
                    Instantiate(powerPelletPrefab, new Vector3(x, y, 0), Quaternion.identity);
                }
            }
        }
    }
}
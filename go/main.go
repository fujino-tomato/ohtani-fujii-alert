package main

import (
	"C"
	"github.com/labstack/echo/v4"
	"net/http"
	"os/exec"
)

func main() {
	e := echo.New()
	e.GET("/", callScrapingEndpoint)
	e.Logger.Fatal(e.Start(":9090"))
}

func callScrapingEndpoint(c echo.Context) error {
	output, err := exec.Command("cd ..", "&&", "python", "python/scraping.py").Output()
	if err != nil {
		return err
	}
	return c.String(http.StatusOK, string(output))
}

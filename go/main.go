package main

import (
	"github.com/labstack/echo/v4"
	"net/http"
)

func main() {

	e := echo.New()
	e.GET("/", sayhelloName)
	e.Logger.Fatal(e.Start(":9090"))
}

func sayhelloName(c echo.Context) error {
	return c.String(http.StatusOK, "Hello, World!")
}

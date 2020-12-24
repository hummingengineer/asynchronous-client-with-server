package main

import (
	"github.com/gin-gonic/gin"
)

// Message is a structure for c.Request.Body of echo router
type Message struct {
	Title   string `form:"title" json:"title" binding:"required"`
	Content string `form:"content" json:"content" binding:"required"`
}

func main() {
	r := setupRouter()
	r.Run(":8080")
}

func setupRouter() *gin.Engine {
	r := gin.Default()

	r.GET("/echo", echo)
	r.POST("/echo", echo)

	return r
}

func echo(c *gin.Context) {
	var message Message

	if c.ShouldBind(&message) != nil {
		c.String(400, "Bad Request. Try Agin")
		return
	}

	c.JSON(200, message)
}

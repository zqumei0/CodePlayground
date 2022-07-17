# Commands

List Version</br>
`go version`

Get Help</br>
`go help`

Get Environment Variables</br>
`go env`

Format Code</br>
`go fmt ../.`

Builds then runs code (Does not create executable) </br>
`go run`

Builds binary (throws away packages)</br>
`go build`

Builds binary and packages and installs in GOBIN</br>
`go install`

Create new module (go.mod file)</br>
`go mod init`

Prints all current module's dependencies</br>
`go list -m`

Changes/Adds required version of dependency</br>
`go get`

Prune unused dependencies
`go mod tidy`
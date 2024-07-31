pipeline {
agent any





stages {
stage('Build') {
steps {
// Get some code from a GitHub repository
git url: 'https://github.com/sanketsir/new-flask-project.git'

// Run Maven on a Unix agent.
script{
if(isUnix()){
sh ""
}
else{
bat "pip install -r requirements.txt "
}
}
}
}



stage('UI Test') {
steps {

// Run Maven on a Unix agent.
script{
if(isUnix()){
sh "pytest"
}
else{
bat "pytest"
}
}
}

}
}
}
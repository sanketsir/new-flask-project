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
sh "pip install -r requirements.txt"
}
else{
bat "pip install -r requirements.txt"
}
}
}
}




stage('Unit Test') {
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
stage('Docker Build') {
            steps {
                script{
                if(isUnix()){
                sh "docker build -t sanket7420/newflaskapp ."
                }
                else{
                 bat "docker build -t sanket7420/newflaskapp ."
                 }
                 }

            }
        }
        stage('Docker Push') {
            steps {
               withCredentials([usernamePassword(credentialsId:'dockerHub',passwordVariable: 'dockerHubPassword',usernameVariable:'dockerHubUser')]){
                bat "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPassword}"
                bat "docker push sanket7420/newflaskapp:latest"
                }


            }

    }
    stage('Kubernetes Pod') {

    steps {
                script{
 if (isUnix()){

 sh "kubectl apply -f deployment.yaml"
 } else {
 bat("kubectl apply -f deployment.yaml")
 }
                }
    }

 }

 stage('Kubernetes Service') {

    steps {
                script{
 if (isUnix()){

 sh "kubectl apply -f service.yaml"
 } else {
 bat("kubectl apply -f service.yaml")
 }
                }
    }

 }


}
}
pipeline {
agent any





stages {
stage('Build') {
steps {
// Get some code from a GitHub repository
git url: 'https://github.com/krishnamurthypradeep/newflaskproject.git'

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




stage('Docker Build') {
            steps {
                script{
                if(isUnix()){
                sh "docker build -t ."
                }
                else{
                 bat "docker build -t ."
                 }
                 }



}

}
}
}
node {
     stage 'Checkout'
        checkout scm

    stage 'Prepare'
        bat 'pip install -r requirements.txt'

    stage 'Test'
        bat 'nosetests --with-xunit'
}
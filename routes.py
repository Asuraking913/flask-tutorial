from flask import request, render_template, g

def root_routes(app): 
    
    # @app.before_request
    # def return_value():
    #     g.user = 'sadasdf'
    #     print(g.user)

    @app.route("/")
    def home():
        app.logger.info('Tring to complete request')
        return render_template('index.html')
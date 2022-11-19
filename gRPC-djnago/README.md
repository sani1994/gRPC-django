##gRPC-djnago
* Clone the project.
* Rename .env.example to .env and set django secret key.
* run `build.sh`
* run `python manage.py makemigraions`
* run `python manage.py migrate`
* run `update_proto.sh`
* run `python manage.py runserver` for access django admin panel.
* run `run_grpc.sh`
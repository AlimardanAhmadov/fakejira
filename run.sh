case $1 in
  dev)
    python manage.py runserver --settings=configs.settings
    ;;
  prod)
  	python manage.py collectstatic --noinput
    python manage.py makemigrations    
    python manage.py migrate
    python manage.py runserver --settings=configs.settings
    ;;
esac
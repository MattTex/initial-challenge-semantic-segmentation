train:
	python src/train.py
infer:
	python src/infer.py
dashboard:
	streamlit run src/app.py
explain:
	python src/explain.py
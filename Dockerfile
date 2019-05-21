FROM continuumio/miniconda3:4.5.11

ENV HOME=/app
WORKDIR $HOME

RUN apt-get update && apt-get install -y --no-install-recommends \
    git
# build-essential

COPY environment.yml $HOME/
RUN conda update -n base conda && \
    conda env create -f $HOME/environment.yml

RUN echo "source activate workshop" > ~/.bashrc
ENV PATH /opt/conda/envs/workshop/bin:$PATH


#ENV PATH=$HOME/miniconda3/envs/workshop/bin:$PATH

COPY . $HOME/

RUN mkdir -p $HOME/model/

EXPOSE 5000

CMD ["python", "app.py"]

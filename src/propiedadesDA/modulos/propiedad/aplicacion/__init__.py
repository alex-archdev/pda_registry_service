from pydispatch import dispatcher
from propiedadesDA.modulos.analisis.aplicacion.handlers import HandlePropiedadDominio

from propiedadesDA.modulos.propiedad.dominio.eventos import PropiedadRegistrada

dispatcher.connect(HandlePropiedadDominio.handle_propiedad_registrada, signal=f"{PropiedadRegistrada.__name__}Dominio")
-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 22-10-2021 a las 17:38:02
-- Versión del servidor: 10.4.21-MariaDB
-- Versión de PHP: 7.4.24

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `senasoft_2021`
--
CREATE DATABASE IF NOT EXISTS `senasoft_2021` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `senasoft_2021`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cargos`
--

DROP TABLE IF EXISTS `cargos`;
CREATE TABLE IF NOT EXISTS `cargos` (
  `id_cargo` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_cargo` varchar(45) NOT NULL,
  PRIMARY KEY (`id_cargo`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `cargos`
--

INSERT INTO `cargos` (`id_cargo`, `nombre_cargo`) VALUES
(1, 'prueba');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `consultas`
--

DROP TABLE IF EXISTS `consultas`;
CREATE TABLE IF NOT EXISTS `consultas` (
  `id_consulta` int(11) NOT NULL AUTO_INCREMENT,
  `id_empleado` int(11) NOT NULL,
  `id_paciente` int(11) NOT NULL,
  `fecha_consulta` varchar(20) NOT NULL,
  `num_histo` varchar(20) NOT NULL,
  `motiv_consu` varchar(100) NOT NULL,
  `detal_consu` varchar(200) NOT NULL,
  `antec_hered_famil` varchar(100) NOT NULL,
  `temperatura` varchar(10) NOT NULL,
  `tensi_arter` varchar(30) NOT NULL,
  `frecu_respi` varchar(30) NOT NULL,
  `frecu_cardi` varchar(30) NOT NULL,
  `talla` varchar(10) NOT NULL,
  `peso` varchar(10) NOT NULL,
  `imc` varchar(10) NOT NULL,
  PRIMARY KEY (`id_consulta`),
  KEY `fk_empleado_consulta` (`id_empleado`),
  KEY `fk_paciente_consulta` (`id_paciente`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `consultas`
--

INSERT INTO `consultas` (`id_consulta`, `id_empleado`, `id_paciente`, `fecha_consulta`, `num_histo`, `motiv_consu`, `detal_consu`, `antec_hered_famil`, `temperatura`, `tensi_arter`, `frecu_respi`, `frecu_cardi`, `talla`, `peso`, `imc`) VALUES
(6, 1, 10, ' 20/10/2021', ' 02', ' Tiene dolor de pecho.', ' La paciente presenta dificultades al respirar.', ' Cancer, deficiencia cardíaca.', ' 38 °C', ' 80 mm Hg', ' 20 rpm', ' 80 1pm.', ' 58 m', ' 62 Kg', ' 24'),
(7, 1, 11, ' 22/10/2021', ' 06', ' Dolor en\nel\ncuerpo.', ' El paciente tieng Fiebre, mareos, dolor de', ' Deficiencia cardíaca, asma.', ' 42°C', ' 90 mm Hg', ' 130 rpm', '\n50 1pm', ' 1.72', ' 60 Kg', ' 24'),
(10, 1, 11, ' 22/10/2021', ' 06', ' Dolor en\nel\ncuerpo.', ' El paciente tieng Fiebre, mareos, dolor de', ' Deficiencia cardíaca, asma.', ' 42°C', ' 90 mm Hg', ' 130 rpm', '\n50 1pm', ' 1.72', ' 60 Kg', ' 24');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleados`
--

DROP TABLE IF EXISTS `empleados`;
CREATE TABLE IF NOT EXISTS `empleados` (
  `id_empleado` int(11) NOT NULL AUTO_INCREMENT,
  `id_cargo` int(11) NOT NULL,
  `id_persona` int(11) NOT NULL,
  PRIMARY KEY (`id_empleado`),
  KEY `fk_cargo_empleado` (`id_cargo`) USING BTREE,
  KEY `fk_persona_empleado` (`id_persona`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `empleados`
--

INSERT INTO `empleados` (`id_empleado`, `id_cargo`, `id_persona`) VALUES
(1, 1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pacientes`
--

DROP TABLE IF EXISTS `pacientes`;
CREATE TABLE IF NOT EXISTS `pacientes` (
  `id_paciente` int(11) NOT NULL AUTO_INCREMENT,
  `id_persona` int(11) NOT NULL,
  `fecha_nacim` varchar(20) NOT NULL,
  `genero` enum('F','M') NOT NULL,
  `ocupacion` varchar(45) NOT NULL,
  `estad_civil` enum('SOLTERO','CASADO','UNIÓN LIBRE','VIUDO') NOT NULL,
  `nacionalidad` varchar(45) NOT NULL,
  `direccion` varchar(45) NOT NULL,
  PRIMARY KEY (`id_paciente`),
  KEY `fk_persona_paciente` (`id_persona`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `pacientes`
--

INSERT INTO `pacientes` (`id_paciente`, `id_persona`, `fecha_nacim`, `genero`, `ocupacion`, `estad_civil`, `nacionalidad`, `direccion`) VALUES
(10, 17, ' 21/01/2003', '', ' Aprendiz', '', ' Colombiana', ' Calle 2b N° 25-09'),
(11, 18, ' 25/01/2001', '', ' Aprendiz', '', ' Colombiana', ' Calle 2b #25-09');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `personas`
--

DROP TABLE IF EXISTS `personas`;
CREATE TABLE IF NOT EXISTS `personas` (
  `id_persona` int(11) NOT NULL AUTO_INCREMENT,
  `num_doc` varchar(12) NOT NULL,
  `nombres` varchar(30) NOT NULL,
  `apellidos` varchar(30) NOT NULL,
  `correo` varchar(35) NOT NULL,
  `telefono` varchar(10) NOT NULL,
  PRIMARY KEY (`id_persona`),
  UNIQUE KEY `num_doc` (`num_doc`),
  UNIQUE KEY `correo` (`correo`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `personas`
--

INSERT INTO `personas` (`id_persona`, `num_doc`, `nombres`, `apellidos`, `correo`, `telefono`) VALUES
(1, '1149195921', 'lucia', 'sanchez', 'luci@gmail.com', '3124080018'),
(17, ' 1006509459', ' Natalia Exerzin fer ', ' Garzón Castiblanco', '\ngarzencastiblanconatalia@gmail.com', ' 319203862'),
(18, ' 1003802951', ' Juan David', ' Bernal Quimbaya', ' Michuzstej@gmail.com', ' 321212332');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `roles`
--

DROP TABLE IF EXISTS `roles`;
CREATE TABLE IF NOT EXISTS `roles` (
  `id_rol` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_rol` varchar(20) NOT NULL,
  PRIMARY KEY (`id_rol`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `roles`
--

INSERT INTO `roles` (`id_rol`, `nombre_rol`) VALUES
(1, 'Empleado'),
(2, 'Administrador');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
CREATE TABLE IF NOT EXISTS `usuarios` (
  `id_usuario` int(11) NOT NULL AUTO_INCREMENT,
  `id_empleado` int(11) NOT NULL,
  `id_rol` int(11) NOT NULL,
  `user_name` varchar(12) NOT NULL,
  `contrasena` varchar(20) NOT NULL,
  PRIMARY KEY (`id_usuario`),
  KEY `fk_empleado_usuario` (`id_empleado`),
  KEY `fk_rol_usuario` (`id_rol`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id_usuario`, `id_empleado`, `id_rol`, `user_name`, `contrasena`) VALUES
(2, 1, 2, 'lucia', '1234');

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `consultas`
--
ALTER TABLE `consultas`
  ADD CONSTRAINT `fk_empleado_consulta` FOREIGN KEY (`id_empleado`) REFERENCES `empleados` (`id_empleado`) ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_paciente_consulta` FOREIGN KEY (`id_paciente`) REFERENCES `pacientes` (`id_paciente`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `empleados`
--
ALTER TABLE `empleados`
  ADD CONSTRAINT `fk_cargo_empleado` FOREIGN KEY (`id_cargo`) REFERENCES `cargos` (`id_cargo`) ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_persona_empleado` FOREIGN KEY (`id_persona`) REFERENCES `personas` (`id_persona`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `pacientes`
--
ALTER TABLE `pacientes`
  ADD CONSTRAINT `fk_id_person` FOREIGN KEY (`id_persona`) REFERENCES `personas` (`id_persona`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD CONSTRAINT `fk_empleado_usuario` FOREIGN KEY (`id_empleado`) REFERENCES `empleados` (`id_empleado`) ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_rol_usuario` FOREIGN KEY (`id_rol`) REFERENCES `roles` (`id_rol`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 20-10-2021 a las 00:28:18
-- Versión del servidor: 10.4.21-MariaDB
-- Versión de PHP: 8.0.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pacientes`
--

DROP TABLE IF EXISTS `pacientes`;
CREATE TABLE IF NOT EXISTS `pacientes` (
  `id_paciente` int(11) NOT NULL AUTO_INCREMENT,
  `id_persona` int(11) NOT NULL,
  `fecha_nacim` DATE NOT NULL,
  `genero` ENUM('F','M') NOT NULL,
  `ocupacion` varchar(45) NOT NULL,
  `estad_civil` ENUM('SOLTERO','CASADO','UNIÓN LIBRE','VIUDO') NOT NULL,
  `nacionalidad` varchar(45) NOT NULL,
  `direccion` varchar(45) NOT NULL,
  PRIMARY KEY (`id_paciente`),
  KEY `fk_persona_paciente` (`id_persona`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `consultas`
--

DROP TABLE IF EXISTS `consultas`;
CREATE TABLE IF NOT EXISTS `consultas` (
  `id_consulta` int(11) NOT NULL AUTO_INCREMENT,
  `id_empleado` int(11) NOT NULL,
  `id_paciente` int(11) NOT NULL,
  `fecha_consulta` datetime NOT NULL,
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
  UNIQUE KEY `num_histo` (`num_histo`),
  KEY `fk_empleado_consulta` (`id_empleado`),
  KEY `fk_paciente_consulta` (`id_paciente`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `roles`
--

DROP TABLE IF EXISTS `roles`;
CREATE TABLE IF NOT EXISTS `roles` (
  `id_rol` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_rol` varchar(20) NOT NULL,
  PRIMARY KEY (`id_rol`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;


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
-- Filtros para la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD CONSTRAINT `fk_empleado_usuario` FOREIGN KEY (`id_empleado`) REFERENCES `empleados` (`id_empleado`) ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_rol_usuario` FOREIGN KEY (`id_rol`) REFERENCES `roles` (`id_rol`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
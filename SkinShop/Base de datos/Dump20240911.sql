-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: ecommerce
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `carrito`
--

DROP TABLE IF EXISTS `carrito`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `carrito` (
  `id_Carrito` int NOT NULL AUTO_INCREMENT,
  `id_Usuario` int DEFAULT NULL,
  `Oculto` tinyint DEFAULT NULL,
  PRIMARY KEY (`id_Carrito`),
  KEY `fk_carrito_usuario_idx` (`id_Usuario`),
  CONSTRAINT `fk_carrito_usuario` FOREIGN KEY (`id_Usuario`) REFERENCES `usuario` (`id_Usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carrito`
--

LOCK TABLES `carrito` WRITE;
/*!40000 ALTER TABLE `carrito` DISABLE KEYS */;
/*!40000 ALTER TABLE `carrito` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `categoria`
--

DROP TABLE IF EXISTS `categoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categoria` (
  `id_Categoria` int NOT NULL AUTO_INCREMENT,
  `Arma` varchar(45) DEFAULT NULL,
  `Ropa` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_Categoria`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categoria`
--

LOCK TABLES `categoria` WRITE;
/*!40000 ALTER TABLE `categoria` DISABLE KEYS */;
/*!40000 ALTER TABLE `categoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detalles`
--

DROP TABLE IF EXISTS `detalles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detalles` (
  `id_Detalles` int NOT NULL AUTO_INCREMENT,
  `id_Carrito` int DEFAULT NULL,
  `id_Producto` int DEFAULT NULL,
  `Cantidad` int DEFAULT NULL,
  `Precio` float DEFAULT NULL,
  PRIMARY KEY (`id_Detalles`),
  KEY `fk_detalles_carrito_idx` (`id_Carrito`),
  KEY `fk_detalles_producto_idx` (`id_Producto`),
  CONSTRAINT `fk_detalles_carrito` FOREIGN KEY (`id_Carrito`) REFERENCES `carrito` (`id_Carrito`),
  CONSTRAINT `fk_detalles_producto` FOREIGN KEY (`id_Producto`) REFERENCES `producto` (`id_Producto`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalles`
--

LOCK TABLES `detalles` WRITE;
/*!40000 ALTER TABLE `detalles` DISABLE KEYS */;
/*!40000 ALTER TABLE `detalles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `juego`
--

DROP TABLE IF EXISTS `juego`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `juego` (
  `id_Juego` int NOT NULL AUTO_INCREMENT,
  `Logo` blob,
  `Plataforma` varchar(45) DEFAULT NULL,
  `Nombre` varchar(45) DEFAULT NULL,
  `URL_pagina` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_Juego`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `juego`
--

LOCK TABLES `juego` WRITE;
/*!40000 ALTER TABLE `juego` DISABLE KEYS */;
/*!40000 ALTER TABLE `juego` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pasarela`
--

DROP TABLE IF EXISTS `pasarela`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pasarela` (
  `id_Pasarela` int NOT NULL AUTO_INCREMENT,
  `id_Carrito` int DEFAULT NULL,
  `Estado` varchar(45) DEFAULT NULL,
  `Total` float DEFAULT NULL,
  `Fecha` datetime DEFAULT NULL,
  PRIMARY KEY (`id_Pasarela`),
  KEY `fk_pasarela_carrito_idx` (`id_Carrito`),
  CONSTRAINT `fk_pasarela_carrito` FOREIGN KEY (`id_Carrito`) REFERENCES `carrito` (`id_Carrito`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pasarela`
--

LOCK TABLES `pasarela` WRITE;
/*!40000 ALTER TABLE `pasarela` DISABLE KEYS */;
/*!40000 ALTER TABLE `pasarela` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `producto`
--

DROP TABLE IF EXISTS `producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `producto` (
  `id_Producto` int NOT NULL AUTO_INCREMENT,
  `id_Juego` int DEFAULT NULL,
  `id_Categoria` int DEFAULT NULL,
  `Descripcion` varchar(45) DEFAULT NULL,
  `Stock` int DEFAULT NULL,
  `Nombre` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_Producto`),
  KEY `fk_producto_juego_idx` (`id_Juego`),
  KEY `fk_producto_categoria_idx` (`id_Categoria`),
  CONSTRAINT `fk_producto_categoria` FOREIGN KEY (`id_Categoria`) REFERENCES `categoria` (`id_Categoria`),
  CONSTRAINT `fk_producto_juego` FOREIGN KEY (`id_Juego`) REFERENCES `juego` (`id_Juego`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `producto`
--

LOCK TABLES `producto` WRITE;
/*!40000 ALTER TABLE `producto` DISABLE KEYS */;
/*!40000 ALTER TABLE `producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tarjeta`
--

DROP TABLE IF EXISTS `tarjeta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tarjeta` (
  `id_Tarjeta` int NOT NULL AUTO_INCREMENT,
  `Fecha` date DEFAULT NULL,
  `Numero` int DEFAULT NULL,
  `DNI` int DEFAULT NULL,
  PRIMARY KEY (`id_Tarjeta`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tarjeta`
--

LOCK TABLES `tarjeta` WRITE;
/*!40000 ALTER TABLE `tarjeta` DISABLE KEYS */;
/*!40000 ALTER TABLE `tarjeta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `id_Usuario` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(45) DEFAULT NULL,
  `Pais` varchar(45) DEFAULT NULL,
  `Apellido` varchar(45) DEFAULT NULL,
  `id_Validacion` int DEFAULT NULL,
  `id_Tarjeta` int DEFAULT NULL,
  PRIMARY KEY (`id_Usuario`),
  KEY `fk_usuario_validacion_idx` (`id_Validacion`),
  KEY `fk_usuario_tarjeta_idx` (`id_Tarjeta`),
  CONSTRAINT `fk_usuario_tarjeta` FOREIGN KEY (`id_Tarjeta`) REFERENCES `tarjeta` (`id_Tarjeta`),
  CONSTRAINT `fk_usuario_validacion` FOREIGN KEY (`id_Validacion`) REFERENCES `validacion` (`id_Validacion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `validacion`
--

DROP TABLE IF EXISTS `validacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `validacion` (
  `id_Validacion` int NOT NULL AUTO_INCREMENT,
  `Correo` varchar(45) DEFAULT NULL,
  `Contraseña` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_Validacion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `validacion`
--

LOCK TABLES `validacion` WRITE;
/*!40000 ALTER TABLE `validacion` DISABLE KEYS */;
/*!40000 ALTER TABLE `validacion` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-09-11 22:06:49

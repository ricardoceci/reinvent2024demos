# Bedrock Runtime API Example for Prompt Routing

This project demonstrates how to use the AWS Bedrock Runtime API to generate responses to user prompts using a default prompt router.

## Repository Structure

The repository has the following structure:

```
.
└── bedrock
    └── promptrouting
        └── promptrouting.py
```

- `bedrock/promptrouting/promptrouting.py`: The main Python script that interacts with the Bedrock Runtime API.

## Usage Instructions

### Prerequisites

- Python 3.x
- AWS account with access to Bedrock Runtime
- AWS CLI configured with appropriate credentials

### Installation

1. Clone the repository:
   ```
   git clone <repository_url>
   cd <repository_name>
   ```

2. Install the required dependencies:
   ```
   pip install boto3
   ```

### Configuration

1. Ensure your AWS CLI is configured with the correct credentials and region.
2. If needed, modify the `profile_name` and `region` in the script to match your AWS setup.

### Running the Script

1. Navigate to the `bedrock/promptrouting` directory:
   ```
   cd bedrock/promptrouting
   ```

2. Run the script:
   ```
   python promptrouting.py
   ```

3. The script will send a predefined user message to the Bedrock Runtime API and print the response.

### Customization

To change the user prompt, modify the `user_message` variable in the `promptrouting.py` file:

```python
user_message = "Your custom prompt here"
```

## Data Flow

1. The script initializes an AWS session and creates a Bedrock Runtime client.
2. A user message is defined and formatted into a message object.
3. The script calls the `converse_stream()` method of the Bedrock Runtime API with the message object.
4. The API processes the prompt using the specified model (Anthropic Claude).
5. The script receives the streaming response and prints the generated text.
6. If available, metadata including trace information is printed.

```
[User] -> [Script] -> [Bedrock Runtime API] -> [Claude Model]
                                            |
                                            v
[User] <- [Script] <- [Streaming Response] <-
```

## Troubleshooting

### Common Issues

1. **AWS Credentials Not Found**
   - Error: `botocore.exceptions.NoCredentialsError: Unable to locate credentials`
   - Solution: Ensure your AWS CLI is properly configured with `aws configure` or set the appropriate environment variables.

2. **Region Not Supported**
   - Error: `botocore.exceptions.EndpointConnectionError: Could not connect to the endpoint URL`
   - Solution: Verify that you're using a supported region for Bedrock Runtime. The script currently uses `us-east-1`.

3. **Model Access Issues**
   - Error: `AccessDeniedException: User: arn:aws:iam::... is not authorized to perform: bedrock:InvokeModel`
   - Solution: Ensure your AWS account has the necessary permissions to access the Bedrock Runtime API and the specified model.

### Debugging

To enable more verbose logging:

1. Add the following import at the beginning of the script:
   ```python
   import logging
   ```

2. Add these lines before creating the Bedrock Runtime client:
   ```python
   logging.basicConfig(level=logging.DEBUG)
   ```

This will provide more detailed information about the API calls and responses, which can be helpful in diagnosing issues.

## Performance Optimization

- Monitor the response time of the Bedrock Runtime API calls.
- If you're making multiple calls, consider implementing rate limiting to avoid hitting API quotas.
- For production use, implement proper error handling and retries for API calls.

# Versión en Español

*Nota: Esta es una traducción del contenido en inglés proporcionado anteriormente.*

# Ejemplo de API de Bedrock Runtime para Enrutamiento de Prompts

Este proyecto demuestra cómo utilizar la API de Bedrock Runtime de AWS para generar respuestas a prompts de usuario utilizando un enrutador de prompts predeterminado.

## Estructura del Repositorio

El repositorio tiene la siguiente estructura:

```
.
└── bedrock
    └── promptrouting
        └── promptrouting.py
```

- `bedrock/promptrouting/promptrouting.py`: El script principal de Python que interactúa con la API de Bedrock Runtime.

## Instrucciones de Uso

### Prerrequisitos

- Python 3.x
- Cuenta de AWS con acceso a Bedrock Runtime
- AWS CLI configurado con las credenciales apropiadas

### Instalación

1. Clonar el repositorio:
   ```
   git clone <url_del_repositorio>
   cd <nombre_del_repositorio>
   ```

2. Instalar las dependencias requeridas:
   ```
   pip install boto3
   ```

### Configuración

1. Asegúrese de que su AWS CLI esté configurado con las credenciales y la región correctas.
2. Si es necesario, modifique el `profile_name` y la `region` en el script para que coincidan con su configuración de AWS.

### Ejecutando el Script

1. Navegue al directorio `bedrock/promptrouting`:
   ```
   cd bedrock/promptrouting
   ```

2. Ejecute el script:
   ```
   python promptrouting.py
   ```

3. El script enviará un mensaje de usuario predefinido a la API de Bedrock Runtime e imprimirá la respuesta.

### Personalización

Para cambiar el prompt del usuario, modifique la variable `user_message` en el archivo `promptrouting.py`:

```python
user_message = "Su prompt personalizado aquí"
```

## Flujo de Datos

1. El script inicializa una sesión de AWS y crea un cliente de Bedrock Runtime.
2. Se define un mensaje de usuario y se formatea en un objeto de mensaje.
3. El script llama al método `converse_stream()` de la API de Bedrock Runtime con el objeto de mensaje.
4. La API procesa el prompt utilizando el modelo especificado (Anthropic Claude).
5. El script recibe la respuesta en streaming e imprime el texto generado.
6. Si está disponible, se imprime la metadata, incluyendo información de trazado.

```
[Usuario] -> [Script] -> [API de Bedrock Runtime] -> [Modelo Claude]
                                                  |
                                                  v
[Usuario] <- [Script] <- [Respuesta en Streaming] <-
```

## Solución de Problemas

### Problemas Comunes

1. **Credenciales de AWS No Encontradas**
   - Error: `botocore.exceptions.NoCredentialsError: Unable to locate credentials`
   - Solución: Asegúrese de que su AWS CLI esté configurado correctamente con `aws configure` o establezca las variables de entorno apropiadas.

2. **Región No Soportada**
   - Error: `botocore.exceptions.EndpointConnectionError: Could not connect to the endpoint URL`
   - Solución: Verifique que esté utilizando una región compatible con Bedrock Runtime. El script actualmente usa `us-east-1`.

3. **Problemas de Acceso al Modelo**
   - Error: `AccessDeniedException: User: arn:aws:iam::... is not authorized to perform: bedrock:InvokeModel`
   - Solución: Asegúrese de que su cuenta de AWS tenga los permisos necesarios para acceder a la API de Bedrock Runtime y al modelo especificado.

### Depuración

Para habilitar un registro más detallado:

1. Agregue la siguiente importación al principio del script:
   ```python
   import logging
   ```

2. Agregue estas líneas antes de crear el cliente de Bedrock Runtime:
   ```python
   logging.basicConfig(level=logging.DEBUG)
   ```

Esto proporcionará información más detallada sobre las llamadas a la API y las respuestas, lo cual puede ser útil para diagnosticar problemas.

## Optimización de Rendimiento

- Monitoree el tiempo de respuesta de las llamadas a la API de Bedrock Runtime.
- Si está realizando múltiples llamadas, considere implementar limitación de tasa para evitar alcanzar las cuotas de la API.
- Para uso en producción, implemente un manejo adecuado de errores y reintentos para las llamadas a la API.
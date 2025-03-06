"""
HTML templates for ezmcp documentation.
"""

# HTML template for the documentation page
DOCS_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{app_name} - ezmcp Documentation</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }}
        h1, h2, h3 {{
            color: #1a73e8;
        }}
        .header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
            padding-bottom: 20px;
            border-bottom: 1px solid #eee;
        }}
        .tool-card {{
            background-color: #f9f9f9;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .tool-name {{
            font-size: 1.4em;
            margin-top: 0;
            margin-bottom: 10px;
            color: #1a73e8;
        }}
        .tool-description {{
            margin-bottom: 15px;
            color: #555;
        }}
        .params-table {{
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 15px;
        }}
        .params-table th, .params-table td {{
            text-align: left;
            padding: 12px;
            border-bottom: 1px solid #ddd;
        }}
        .params-table th {{
            background-color: #f2f2f2;
        }}
        .required {{
            color: #d32f2f;
            font-weight: bold;
        }}
        .optional {{
            color: #388e3c;
        }}
        .try-it {{
            background-color: #1a73e8;
            color: white;
            border: none;
            padding: 10px 15px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 14px;
        }}
        .try-it:hover {{
            background-color: #0d47a1;
        }}
        .try-section {{
            margin-top: 20px;
            padding: 20px;
            background-color: #f5f5f5;
            border-radius: 8px;
            display: none;
        }}
        .input-group {{
            margin-bottom: 15px;
        }}
        .input-group label {{
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }}
        .input-group input, .input-group textarea {{
            width: 100%;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 14px;
        }}
        .submit-btn {{
            background-color: #388e3c;
            color: white;
            border: none;
            padding: 10px 15px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 14px;
        }}
        .submit-btn:hover {{
            background-color: #2e7d32;
        }}
        .response-area {{
            margin-top: 15px;
            padding: 15px;
            background-color: #fff;
            border: 1px solid #ddd;
            border-radius: 4px;
            min-height: 100px;
        }}
        .footer {{
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid #eee;
            text-align: center;
            color: #777;
        }}
        .server-info {{
            background-color: #e8f0fe;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 20px;
        }}
        .server-info h3 {{
            margin-top: 0;
            color: #1a73e8;
        }}
        .server-info p {{
            margin-bottom: 5px;
        }}
        .server-info code {{
            background-color: #f1f3f4;
            padding: 2px 5px;
            border-radius: 3px;
            font-family: monospace;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>{app_name} - ezmcp Documentation</h1>
        <p>Powered by <a href="https://github.com/jujumilk3/ezmcp" target="_blank">ezmcp</a></p>
    </div>

    <div class="server-info">
        <h3>Server Information</h3>
        <p><strong>Server Name:</strong> {app_name}</p>
        <p><strong>SSE Endpoint:</strong> <code>{sse_endpoint}</code></p>
        <p><strong>Messages Path:</strong> <code>{sse_path}</code></p>
    </div>

    <h2>Available Tools</h2>
    
    {tools_html}
    
    <div class="footer">
        <p>Generated by ezmcp - A FastAPI-style framework for MCP SSE</p>
    </div>

    <script>
        function toggleTrySection(toolName) {{
            const section = document.getElementById(`try-section-${{toolName}}`);
            if (section.style.display === 'block') {{
                section.style.display = 'none';
            }} else {{
                section.style.display = 'block';
            }}
        }}

        async function submitToolRequest(toolName) {{
            const form = document.getElementById(`form-${{toolName}}`);
            const responseArea = document.getElementById(`response-${{toolName}}`);
            
            // Collect form data
            const formData = new FormData(form);
            const params = {{}};
            
            for (const [key, value] of formData.entries()) {{
                params[key] = value;
            }}
            
            responseArea.innerHTML = 'Sending request...';
            
            try {{
                // This is just a placeholder - in a real implementation, 
                // you would connect to the SSE endpoint and send a message
                responseArea.innerHTML = `Tool request sent to ${{toolName}} with parameters: <pre>${{JSON.stringify(params, null, 2)}}</pre>`;
                
                // Note: In a real implementation, you would need to implement
                // the actual SSE client connection and message sending logic
            }} catch (error) {{
                responseArea.innerHTML = `Error: ${{error.message}}`;
            }}
        }}
    </script>
</body>
</html>
"""

# Template for each tool card
TOOL_CARD_TEMPLATE = """
<div class="tool-card">
    <h3 class="tool-name">{name}</h3>
    <p class="tool-description">{description}</p>
    
    <h4>Parameters</h4>
    <table class="params-table">
        <thead>
            <tr>
                <th>Name</th>
                <th>Type</th>
                <th>Required</th>
                <th>Description</th>
            </tr>
        </thead>
        <tbody>
            {params_rows}
        </tbody>
    </table>
    
    <button class="try-it" onclick="toggleTrySection('{name}')">Try it</button>
    
    <div id="try-section-{name}" class="try-section">
        <h4>Test Tool</h4>
        <form id="form-{name}" onsubmit="event.preventDefault(); submitToolRequest('{name}')">
            {form_inputs}
            <button type="submit" class="submit-btn">Send Request</button>
        </form>
        <div class="response-area" id="response-{name}">
            Response will appear here...
        </div>
    </div>
</div>
"""

# Template for parameter table row
PARAM_ROW_TEMPLATE = """
<tr>
    <td>{name}</td>
    <td>{type}</td>
    <td class="{required_class}">{required_text}</td>
    <td>{description}</td>
</tr>
"""

# Template for form input
FORM_INPUT_TEMPLATE = """
<div class="input-group">
    <label for="{name}-{tool_name}">{name}{required_mark}</label>
    <input type="{input_type}" id="{name}-{tool_name}" name="{name}" {required_attr}>
</div>
""" 
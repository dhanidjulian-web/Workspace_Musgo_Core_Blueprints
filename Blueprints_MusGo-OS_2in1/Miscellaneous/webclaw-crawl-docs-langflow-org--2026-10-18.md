# What is Langflow? | Langflow Documentation

`https://docs.langflow.org/`

# What is Langflow

Build and run your first flow in minutes: Install Langflow, and then try the Quickstart.

Copy page ⌥C Version: 1.12.x On this page
## Application development and prototyping​
## Endless modifications and integrations​
## Next steps​




Langflow is an open-source, Python-based, customizable framework for building AI applications. It supports important AI functionality like agents and the Model Context Protocol (MCP), and it doesn't require you to use specific large language models (LLMs) or vector stores.


The visual editor simplifies prototyping of application workflows, enabling developers to quickly turn their ideas into powerful, real-world solutions.


[#### Quickstart Build and run your first flow in minutes.](https://docs.langflow.org/get-started-quickstart) [#### Components Explore all available components and integrations.](https://docs.langflow.org/concepts-components) [#### Deploy Deploy Langflow to production environments.](https://docs.langflow.org/deployment-overview)


## Application development and prototyping [​](https://docs.langflow.org/#application-development-and-prototyping)


Langflow can help you develop a wide variety of AI applications, such as chatbots, document analysis systems, content generators, and agentic applications.


Langflow includes several pre-built templates that are ready to use or customize to your needs.


### Create flows in minutes [​](https://docs.langflow.org/#create-flows-in-minutes)


The primary purpose of Langflow is to create and serve flows, which are functional representations of application workflows.


To [build a flow](https://docs.langflow.org/concepts-flows), you connect and configure component nodes. Each component is a single step in the workflow.


With Langflow's [visual editor](https://docs.langflow.org/concepts-overview), you can drag and drop components to quickly build and test a functional AI application workflow. For example, you could build a chatbot flow for an e-commerce store that uses an LLM and a product data store to allow customers to ask questions about the store's products.


![Basic Prompting flow in Langflow](https://docs.langflow.org/assets/images/workspace-basic-prompting-c16e2f001725aa6dc1bc479f22aa11df.png)


### Test flows in real-time [​](https://docs.langflow.org/#test-flows-in-real-time)


You can use the [**Playground**](https://docs.langflow.org/concepts-playground) to test flows without having to build your entire application stack. You can interact with your flows and get real-time feedback about flow logic and response generation.


You can also run individual components to test dependencies in isolation.


### Run and serve flows [​](https://docs.langflow.org/#run-and-serve-flows)


You can use your flows as prototypes for more formal application development, or you can use the Langflow API to embed your flows into your application code.


For more extensive development, you can build Langflow as a dependency or deploy a Langflow server to serve flows over the public internet.


[#### Trigger flows with the API Use the Langflow API to run flows from your application code.](https://docs.langflow.org/concepts-publish) [#### Containerize your app Build and deploy Langflow as a containerized application.](https://docs.langflow.org/develop-application)


## Endless modifications and integrations [​](https://docs.langflow.org/#endless-modifications-and-integrations)


Langflow provides [components](https://docs.langflow.org/concepts-components) that support many services, tools, and functionality that are required for AI applications.


Some components are generalized, such as inputs, outputs, and data stores. Others are specialized, such as agents, language models, and embedding providers.


All components offer parameters that you can set to fixed or variable values. You can also use tweaks to temporarily override flow settings at runtime.


### Agent and MCP support [​](https://docs.langflow.org/#agent-and-mcp-support)


[#### Langflow Agents Build and configure AI agents with Langflow.](https://docs.langflow.org/agents) [#### Agent tools Use components and flows as agent tools.](https://docs.langflow.org/agents-tools) [#### MCP server Expose Langflow as an MCP server.](https://docs.langflow.org/mcp-server) [#### MCP client Connect Langflow to external MCP servers.](https://docs.langflow.org/mcp-client)


### Extensibility [​](https://docs.langflow.org/#extensibility)


In addition to the core components, Langflow supports custom components.


You can use custom components developed by others, and you can develop your own custom components for personal use or to share with other Langflow users.


[#### Contribute Help build Langflow.](https://docs.langflow.org/contributing-how-to-contribute) [#### Custom components Create your own Python components.](https://docs.langflow.org/components-custom-components) [#### Get help Request enhancements and report issues.](https://docs.langflow.org/contributing-github-issues)


## Next steps [​](https://docs.langflow.org/#next-steps)


- [Install Langflow](https://docs.langflow.org/get-started-installation)
- [Quickstart](https://docs.langflow.org/get-started-quickstart)


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)

- [Application development and prototyping](https://docs.langflow.org/#application-development-and-prototyping)
  - [Create flows in minutes](https://docs.langflow.org/#create-flows-in-minutes)
  - [Test flows in real-time](https://docs.langflow.org/#test-flows-in-real-time)
  - [Run and serve flows](https://docs.langflow.org/#run-and-serve-flows)- [Endless modifications and integrations](https://docs.langflow.org/#endless-modifications-and-integrations)
  - [Agent and MCP support](https://docs.langflow.org/#agent-and-mcp-support)
  - [Extensibility](https://docs.langflow.org/#extensibility)- [Next steps](https://docs.langflow.org/#next-steps)[Manage Privacy Choices](https://docs.langflow.org/#)

---

# Langflow deployment overview | Langflow Documentation

`https://docs.langflow.org/deployment-overview`

# Langflow deployment overview

To self-host your local server through an ngrok gateway, see Deploy a public Langflow server. This approach uses ngrok to forward traffic and share your local Langflow server over the internet, without deploying to a cloud provider or exposing your network directly.

Copy page ⌥C Version: 1.12.x

This section includes the different ways to bring your locally-built flows to the world.


- To self-host your local server through an ngrok gateway, see [Deploy a public Langflow server](https://docs.langflow.org/deployment-public-server). This approach uses [ngrok](https://ngrok.com/docs/getting-started/) to forward traffic and share your local Langflow server over the internet, without deploying to a cloud provider or exposing your network directly.
- To build and deploy a Langflow container that includes your flow files, see [Containerize a Langflow application](https://docs.langflow.org/develop-application). This approach bundles your flows and dependencies into a portable, reproducible Docker image for easy deployment across different environments.
- To deploy a Langflow server on a remote server with Docker and Caddy, see [Deploy Langflow on a remote server](https://docs.langflow.org/deployment-caddyfile). This approach is good for hosting your own Langflow instance on a remote server with secure web access, using Docker containers and Caddy as a reverse proxy for HTTPS support.
- To deploy Langflow with Nginx and automatic SSL certificates, see [Deploy Langflow with Nginx and Let's Encrypt](https://docs.langflow.org/deployment-nginx-ssl). This approach uses Nginx as a reverse proxy with Let's Encrypt for automatic HTTPS certificate management to provide a secure deployment *without* Docker.
- To deploy Langflow on Kubernetes, see [Langflow Kubernetes architecture and best practices](https://docs.langflow.org/deployment-prod-best-practices) This approach creates production-grade deployments with high availability, scalability, and robust orchestration.
- For cloud provider-specific deployment guides, see your cloud provider's documentation. The Langflow documentation provides a few examples, such as [Google Cloud Platform](https://docs.langflow.org/deployment-gcp) and [Hugging Face Spaces](https://docs.langflow.org/deployment-hugging-face-spaces), to help you get started.


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)[Manage Privacy Choices](https://docs.langflow.org/deployment-overview#)

---

# Test flows in the Playground | Langflow Documentation

`https://docs.langflow.org/concepts-playground`

# Test flows in the Playground
## Run a flow in the Playground​
*For technical details about how the Playground works, see Monitor endpoints.*

*For more information, see Human-in-the-Loop.*

## Set custom session IDs​
## Share a flow's Playground​
## See also​





Langflow's Playground is a dynamic interface you can use to test your LLM-based flows in real-time.

Copy page ⌥C Version: 1.12.x On this page

Langflow's **Playground** is a dynamic interface you can use to test your LLM-based flows in real-time.


You can test how a flow responds to different inputs, review and modify memories, and monitor flow output and logic. For example, you can make sure agent flows use the appropriate tools to respond to different inputs.


The **Playground** allows you to quickly iterate over your flow's logic and behavior, making it easier to prototype and refine your applications.


## Run a flow in the Playground [​](https://docs.langflow.org/concepts-playground#run-a-flow-in-the-playground)


To run a flow in the **Playground**, open the flow, and then click **Playground**. Then, if your flow has a [**Chat Input** component](https://docs.langflow.org/chat-input-and-output), enter a prompt or [use voice mode](https://docs.langflow.org/concepts-voice-mode) to trigger the flow and start a chat session.


To expand the **Playground** view, click **Enter fullscreen** within the **Playground** panel.


![The Langflow visual builder with the Playground active](https://docs.langflow.org/assets/images/playground-34f869f8763b3c69ddcd4d365c96d0e6.png)


![Playground window](https://docs.langflow.org/assets/images/playground-34f869f8763b3c69ddcd4d365c96d0e6.png)


For technical details about how the **Playground** works, see [Monitor endpoints](https://docs.langflow.org/api-monitor).


### Review agent logic [​](https://docs.langflow.org/concepts-playground#review-agent-logic)


If your flow has an **Agent** component, the **Playground** prints the tools used by the agent and the output from each tool. This helps you monitor the agent's tool use and understand the logic behind the agent's responses. For example, the following agent used a connected `fetch_content` tool to perform a web search:


![Playground with agent response](https://docs.langflow.org/assets/images/playground-with-agent-56fa39130f9a50d376ba5a226ae254f0.png)


### Respond to Human-in-the-Loop prompts [​](https://docs.langflow.org/concepts-playground#respond-to-human-in-the-loop-prompts)


When a flow pauses for human approval from a [**Human Input** component](https://docs.langflow.org/human-input) or an [**Agent**](https://docs.langflow.org/agents), the **Playground** prompts you to approve or reject the tool call.


Select an action to resume the run from where it was paused.


For more information, see [Human-in-the-Loop](https://docs.langflow.org/human-in-the-loop).


### View chat history [​](https://docs.langflow.org/concepts-playground#view-chat-history)


In the **Playground**, you can view message logs for each of your flow's chat sessions, including timestamps, content, and senders.


In the **Playground** sidebar, find the chat session you want to review, click **Options**, and then select **Message Logs**.


![Playground logs](https://docs.langflow.org/assets/images/messages-logs-0253cad77c1fb946dc1e2f0fe239261f.png)


Message logs break apart the [`Message` data](https://docs.langflow.org/data-types#message) for each chat message. Click any cell in the message logs to view the full contents of that cell.


### Modify memories in the Playground [​](https://docs.langflow.org/concepts-playground#modify-memories-in-the-playground)


To help debug and test your flows, you can edit or delete individual messages in [message logs](https://docs.langflow.org/concepts-playground#view-chat-history). For example, you might want to delete messages that you sent while testing a component that is no longer part of your flow.


You can also delete entire chat sessions from the sidebar: click **Options**, and then select **Delete**.


Modifying memories influences the behavior of the chatbot responses if you continue the chat session or if you preserve memories over multiple chat sessions.


**Editing message logs edits Langflow's internal `messages` table, which is the default chat memory storage.** For more information about managing sessions and chat memory in Langflow, see [Use custom session IDs](https://docs.langflow.org/concepts-playground#session-ids) and [Memory management options](https://docs.langflow.org/memory).


## Set custom session IDs [​](https://docs.langflow.org/concepts-playground#session-ids)


Chat sessions are identified by session ID (`session_id`), which is a unique identifier for a flow run.


The default session ID is the flow ID, which means that all chat messages for a flow are stored under the same session ID as one enormous chat session.


If you need to preserve chat context over multiple flow runs or differentiate chat sessions when debugging flows, you can set a custom `session_id`.


Custom session IDs are helpful for multiple reasons:


- Separate chat sessions in situations where one flow has multiple chat sessions, such as a chatbot that can have multiple simultaneous user interactions.
- Preserve memory when continuing a chat session across multiple flow runs or when passing context from one flow to another.
- Differentiate activity from multiple users within the same flow.
- Identify your own chat sessions when debugging and testing flows.


You can set custom session IDs in the visual editor and programmatically.


- Visual editor
- Langflow API


In your [input and output components](https://docs.langflow.org/chat-input-and-output), use the **Session ID** field:


1. Click the component where you want to set a custom session ID.
2. In the [component inspection panel](https://docs.langflow.org/concepts-components#component-menus), enable **Session ID**.
3. Click **Close**.
4. Enter a custom session ID. If the field is empty, the flow uses the default session ID.
5. Open the **Playground** to start a chat under your custom session ID.


Make sure to change the **Session ID** when you want to start a new chat session or continue an earlier chat session with a different session ID.


When you trigger a flow with the Langflow API, include the `session_id` parameter in the request payload. For example:


```bash
curl -X POST "http://$LANGFLOW_SERVER_ADDRESS/api/v1/run/$FLOW_ID" \
-H "Content-Type: application/json" \
-H "x-api-key: $LANGFLOW_API_KEY" \
-d '{
    "session_id": "CUSTOM_SESSION_ID",
    "input_value": "message",
    "input_type": "chat",
    "output_type": "chat"
}'
```


This command starts a new chat sessions with the specified `session_id` or it retrieves an existing session with that ID, if one exists.


For more information, see [Use session ID to manage communication between components](https://docs.langflow.org/session-id).


## Share a flow's Playground [​](https://docs.langflow.org/concepts-playground#share-a-flows-playground)


The **Shareable Playground** option exposes the **Playground** for a single flow at the `/public_flow/$FLOW_ID` endpoint.


After you [deploy a public Langflow server](https://docs.langflow.org/deployment-overview), you can share this public URL with another user to allow them to access the specified flow's **Playground** only. The user can interact with the flow's chat input and output and view the results without installing Langflow or generating a Langflow API key.


To share a flow's **Playground** with another user, do the following:


1. In Langflow, open the flow you want share.
2. In the [workspace](https://docs.langflow.org/concepts-overview#workspace), click **Share**, and then enable **Shareable Playground**.
3. Click **Shareable Playground** again to open the **Playground** window. This window's URL is the flow's **Shareable Playground** address, such as `https://3f7c-73-64-93-151.ngrok-free.app/playground/d764c4b8-5cec-4c0f-9de0-4b419b11901a`.
4. Send the URL to another user to give them access to the flow's **Playground**.


By default, a shared **Playground** can't run a flow that contains a custom component, because the run is unauthenticated and Langflow executes only its own copy of each component on that path. To run one anyway, install the component on the server with `LANGFLOW_COMPONENTS_PATH`. For more information, see [Custom components in publicly shared flows](https://docs.langflow.org/deployment-block-custom-components#public-flow-custom-components).


## See also [​](https://docs.langflow.org/concepts-playground#see-also)


- [Upload images](https://docs.langflow.org/concepts-file-management#upload-images)
- [Use voice mode](https://docs.langflow.org/concepts-voice-mode)
- [Trigger flows with the Langflow API](https://docs.langflow.org/concepts-publish)
- [Session ID](https://docs.langflow.org/session-id)


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)

- [Run a flow in the Playground](https://docs.langflow.org/concepts-playground#run-a-flow-in-the-playground)
  - [Review agent logic](https://docs.langflow.org/concepts-playground#review-agent-logic)
  - [Respond to Human-in-the-Loop prompts](https://docs.langflow.org/concepts-playground#respond-to-human-in-the-loop-prompts)
  - [View chat history](https://docs.langflow.org/concepts-playground#view-chat-history)
  - [Modify memories in the Playground](https://docs.langflow.org/concepts-playground#modify-memories-in-the-playground)- [Set custom session IDs](https://docs.langflow.org/concepts-playground#session-ids)
- [Share a flow's Playground](https://docs.langflow.org/concepts-playground#share-a-flows-playground)
- [See also](https://docs.langflow.org/concepts-playground#see-also)[Manage Privacy Choices](https://docs.langflow.org/concepts-playground#)

---

# Components overview | Langflow Documentation

`https://docs.langflow.org/concepts-components`

# Components overview

Langflow provides keyboard shortcuts for the workspace.

Copy page ⌥C Version: 1.12.x On this page
## Add a component to a flow​
*To view the output and logs for a single component, click  Inspect.*

## Component ports​
## Component code​
## Component versions​
## Group components​
## Legacy components​







Components are the building blocks of your flows. Like classes in an application, each component is designed for a specific use case or integration.


## Add a component to a flow [​](https://docs.langflow.org/concepts-components#component-menus)


To add a component to a flow, drag the component from the **Core components** or **Bundles** menu into the [workspace](https://docs.langflow.org/concepts-overview#workspace).


Components are grouped by type or provider, and some components are hidden by default:


- **Core components**: Langflow's base components are grouped by purpose, such as **Inputs and Outputs** or **Data**. These components either provide generic functionality, like loops and parsing, or they provide single components that support multiple third-party integrations.
- **Bundles**: Bundles contain one or more components that support specific third-party integrations, and they are grouped by service provider.
- **Legacy**: These components are hidden by default. For more information, see [Legacy components](https://docs.langflow.org/concepts-components#legacy-components).


### Configure a component [​](https://docs.langflow.org/concepts-components#configure-a-component)


After adding a component to a flow, configure the component's parameters and connect it to the other components in your flows.


Each component has inputs, outputs, parameters, and controls related to the component's purpose. By default, components show only required and common options. To access additional settings and controls, including meta settings, use the [component inspection panel](https://docs.langflow.org/concepts-components#component-inspection-panel).


### Component inspection panel [​](https://docs.langflow.org/concepts-components#component-inspection-panel)


When you select a component in the workspace, a component inspection panel appears on the right side of the screen.


The inspection panel displays all of a component's parameters, including hidden or advanced parameters.


### Component header menus [​](https://docs.langflow.org/concepts-components#component-header-menus)


To access a component's header menu, click the component in your workspace.


![Agent component](https://docs.langflow.org/assets/images/agent-component-1388a5c249e1f446bce2a7586a87e986.png)


The following options are available directly on the header menu:


- **Code**: Modify component settings by directly editing the component's Python code.
- **Freeze**: Freeze a component and all upstream components to prevent re-running. For more information, see [Freeze a component](https://docs.langflow.org/concepts-components#freeze-a-component).
- **Tool Mode**: Enable this option when combining a component with an **Agent** component.


For all other options, including **Delete** and **Duplicate** controls, click **Show More**.


### Rename a component [​](https://docs.langflow.org/concepts-components#rename-a-component)


To modify a component's name or description, click the component in the workspace, and then click **Edit**. Component descriptions accept Markdown syntax.


### Run a component [​](https://docs.langflow.org/concepts-components#run-a-component)


To run a single component, click **Run component**. A **Last Run** value indicates that the component ran successfully.


Running a single component is different from running an entire flow. In a single component run, the `build_vertex` function is called, which builds and runs only the single component with direct inputs provided through the visual editor (the `inputs_dict` parameter). The `VertexBuildResult` data is passed to the `build_and_run` method that calls the component's `build` method and runs it. Unlike running an entire flow, running a single component doesn't automatically execute its upstream dependencies.


### Inspect component output and logs [​](https://docs.langflow.org/concepts-components#inspect-component-output-and-logs)


To view the output and logs for a single component, click **Inspect**.


### Freeze a component [​](https://docs.langflow.org/concepts-components#freeze-a-component)


Use the freeze option if you expect consistent output from a component *and all upstream components*, and you only need to run those components once.


Freezing a component prevents that component and all upstream components from re-running, and it preserves the last output state for those components. Any future flow runs use the preserved output.


To freeze a component, click the component in the workspace to expose the component's header menu, and then click **Freeze**.


## Component ports [​](https://docs.langflow.org/concepts-components#component-ports)


Around the border of each component, there are circular port icons like . These indicate a component *connection point* or *port*.


Ports either accept input or produce output of a specific data type. You can infer the data type from the field the port is attached to or from the [port's color](https://docs.langflow.org/concepts-components#port-colors). For example, the **System Message** field accepts [message data](https://docs.langflow.org/data-types#message), as illustrated by the blue port icon: .


![Prompt Template component with multiple inputs](https://docs.langflow.org/assets/images/prompt-component-858130cb1fdfd071e743d5f0b122fd0e.png)


When building flows, connect output ports to input ports of the same type (color) to transfer that type of data between two components. For information about the programmatic representation of each data type, see [Langflow data types](https://docs.langflow.org/data-types).


### Dynamic ports [​](https://docs.langflow.org/concepts-components#dynamic-ports)


Some components have ports that are dynamically added or removed. For example, the **Prompt Template** component accepts [inputs wrapped in curly braces](https://docs.langflow.org/components-prompts#define-variables-in-prompts), and new ports are opened when a value wrapped in curly braces is detected in the **Template** field.


![Prompt Template component with multiple inputs](https://docs.langflow.org/assets/images/prompt-component-with-multiple-inputs-858130cb1fdfd071e743d5f0b122fd0e.png)


### Output type selection [​](https://docs.langflow.org/concepts-components#output-type-selection)


All components produce output that is either sent to another component in the flow or returned as the final flow result.


Some components can produce multiple types of output:


- If the component emits all types at once, the component has multiple output ports in the visual editor. In component code, this is represented by `group_outputs=True`
- If the component emits only one type, you must select the output type by clicking the output label near the output port, and then selecting the desired output type. In component code, this is represented by `group_outputs=False` or omitting the `group_outputs` parameter.


For example, a language model component can output *either* a **Model Response** or **Language Model**. The **Model Response** output produces [`Message`](https://docs.langflow.org/data-types#message) data that can be passed to another component's `Message` port. The **Language Model** output must be connected to a component with a **Language Model** input, such as the [**Structured Output** component](https://docs.langflow.org/structured-output), that uses the attached LLM to power the receiving component's reasoning.


![Output type selection in the Language Model component](https://docs.langflow.org/assets/images/select-output-ad560bd6e07233463111cf2516097571.png)


### Port colors [​](https://docs.langflow.org/concepts-components#port-colors)


Component port colors indicate the data type ingested or emitted by the port. For example, a **Message** port either accepts or emits `Message` data.


The following table lists the component data types and their corresponding port colors:


| Data type | Port color | Port icon example |
| --- | --- | --- |
| JSON | Red |  |
| Table | Pink |  |
| Embeddings | Emerald |  |
| LanguageModel | Fuchsia |  |
| Memory | Orange |  |
| Message | Indigo |  |
| Tool | Cyan |  |
| Unknown or multiple types | Gray |  |


## Component code [​](https://docs.langflow.org/concepts-components#component-code)


You can edit components in the [workspace](https://docs.langflow.org/concepts-overview#workspace) and in code. When editing a flow, select a component, and then click **Code** to see and edit the component's underlying Python code.


All components have underlying code that determines how you configure them and what actions they can perform. In the context of creating and running flows, component code does the following:


- Determines what configuration options to show in the visual editor.
- Validates inputs based on the component's defined input types.
- Processes data using the configured parameters, methods, and functions.
- Passes results to the next component in the flow.


All components inherit from a base `Component` class that defines the component's interface and behavior. For example, the [**Recursive Character Text Splitter** component](https://github.com/langflow-ai/langflow/blob/main/src/lfx/src/lfx/components/langchain_utilities/recursive_character.py) is a child of the [`LCTextSplitterComponent`](https://github.com/langflow-ai/langflow/blob/main/src/lfx/src/lfx/base/textsplitters/model.py) class.


Each component's code includes definitions for inputs and outputs, which are represented in the workspace as [component ports](https://docs.langflow.org/concepts-components#component-ports). For example, the `RecursiveCharacterTextSplitter` has four inputs. Each input definition specifies the input type, such as `IntInput`, as well as the encoded name, display name, description, and other parameters for that specific input. These values determine the component settings, such as display names and tooltips in the visual editor.


RecursiveCharacterTextSplitter inputs (from recursive_character.py)

```python
    inputs = [
        IntInput(
            name="chunk_size",
            display_name="Chunk Size",
            info="The maximum length of each chunk.",
            value=1000,
        ),
        IntInput(
            name="chunk_overlap",
            display_name="Chunk Overlap",
            info="The amount of overlap between chunks.",
            value=200,
        ),
        DataInput(
            name="data_input",
            display_name="Input",
            info="The texts to split.",
            input_types=["Document", "Data", "JSON"],
            required=True,
        ),
        MessageTextInput(
            name="separators",
            display_name="Separators",
            info='The characters to split on.\nIf left empty defaults to ["\\n\\n", "\\n", " ", ""].',
            is_list=True,
        ),
    ]
```


Additionally, components have methods or functions that handle their functionality. For example, the `RecursiveCharacterTextSplitter` has two methods:


RecursiveCharacterTextSplitter methods (from recursive_character.py)

```python
    def get_data_input(self) -> Any:
        return self.data_input

    def build_text_splitter(self) -> TextSplitter:
        if not self.separators:
            separators: list[str] | None = None
        else:
            # check if the separators list has escaped characters
            # if there are escaped characters, unescape them
            separators = [unescape_string(x) for x in self.separators]

        return RecursiveCharacterTextSplitter(
            separators=separators,
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
        )
```


The `get_data_input` method retrieves the text to be split from the component's input, which makes the data available to the class. The `build_text_splitter` method creates a `RecursiveCharacterTextSplitter` object by calling its parent class's `build` method. Then, the text is split with the created splitter and passed to the next component.


## Component versions [​](https://docs.langflow.org/concepts-components#component-versions)


Component versions and states are stored in an internal Langflow database. When you add a component to a flow, you create a detached copy of the component based on the information in the Langflow database. These copies are detached from the primary Langflow database, and they don't synchronize with any updates that can occur when you upgrade your Langflow version.


In other words, an individual instance of a component retains the version number and state from the moment you add it to a specific flow. For example, if a component is at version 1.0 when you add it to a flow, it remains at version 1.0 *in that flow* unless you update it.


### Update component versions [​](https://docs.langflow.org/concepts-components#update-component-versions)


When editing a flow in the workspace, Langflow notifies you if a component's workspace version is behind the database version so you can update the component's workspace version:


- **Update ready**: This notification means the component update contains no breaking changes.
- **Update available**: This notification means the component update might contain breaking changes. Breaking changes modify component inputs and outputs, causing the components to be disconnected and break the flow. After updating the component, you might need to edit the component settings or reconnect component ports.


There are two ways to update components:


- Click **Update** to update a single component. This is recommended for updates without breaking changes.
- Click **Review** to view all available updates and create a snapshot before updating. This is recommended for updates with breaking changes. To save a snapshot of your flow before updating the components, enable **Create backup flow before updating**. Backup flows are stored in the same project folder as the original flow with the suffix `(backup)`. To update specific components, select the components you want to update, and then click **Update Components**.


Components are updated to the latest available version, based on the version of Langflow you are running.


## Group components [​](https://docs.langflow.org/concepts-components#group-components)


Multiple components can be grouped into a single component for reuse. This is useful for organizing large flows by combining related components together, such as a RAG **Agent** component and it's associated tools or vector store components.


1. Hold Shift, and then click and drag to highlight all components you want to merge. Components must be completely within the selection area to be merged. Alternatively, to select components for merging one by one, hold Ctrl on Windows or Cmd on Mac, and then click each component to add them to the group.
2. Release the mouse and keyboard, and then click **Group** to merge the components into a single, group component.


Grouped components are configured and managed as a single component, including the component name, code, and settings.


To ungroup the components, click the component in the workspace to expose the component's header menu, click **Show More**, and then select **Ungroup**.


If you want to reuse this grouping in other flows, click the component in the workspace to expose the component's header menu, click **Show More**, and then select **Save** to save the component to the **Core components** menu as a custom component.


## Legacy components [​](https://docs.langflow.org/concepts-components#legacy-components)


Legacy components are no longer supported and can be removed in a future release. You can continue to use them in existing flows, but it is recommended that you replace them with supported components as soon as possible. Suggested replacements are included in the **Legacy** banner on components in your flows. They are also given in release notes and Langflow documentation whenever possible.


If you aren't sure how to replace a legacy component, **Search** for components by provider, service, or component name. The component may have been deprecated in favor of a completely new component, a similar component, or a new version of the same component in a different category.


If there is no obvious replacement, consider whether another component can be adapted to your use case. For example, many **Core components** provide generic functionality that can support multiple providers and use cases, such as the [**API Request** component](https://docs.langflow.org/api-request).


If neither of these options are viable, you could use the legacy component's code to create your own custom component, or [start a discussion](https://docs.langflow.org/contributing-github-issues) about the legacy component.


To discourage use of legacy components in new flows, these components are hidden by default. In the visual editor, you can click **Component settings** to toggle the **Legacy** filter.


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)

- [Add a component to a flow](https://docs.langflow.org/concepts-components#component-menus)
  - [Configure a component](https://docs.langflow.org/concepts-components#configure-a-component)
  - [Component inspection panel](https://docs.langflow.org/concepts-components#component-inspection-panel)
  - [Component header menus](https://docs.langflow.org/concepts-components#component-header-menus)
  - [Rename a component](https://docs.langflow.org/concepts-components#rename-a-component)
  - [Run a component](https://docs.langflow.org/concepts-components#run-a-component)
  - [Inspect component output and logs](https://docs.langflow.org/concepts-components#inspect-component-output-and-logs)
  - [Freeze a component](https://docs.langflow.org/concepts-components#freeze-a-component)- [Component ports](https://docs.langflow.org/concepts-components#component-ports)
  - [Dynamic ports](https://docs.langflow.org/concepts-components#dynamic-ports)
  - [Output type selection](https://docs.langflow.org/concepts-components#output-type-selection)
  - [Port colors](https://docs.langflow.org/concepts-components#port-colors)- [Component code](https://docs.langflow.org/concepts-components#component-code)
- [Component versions](https://docs.langflow.org/concepts-components#component-versions)
  - [Update component versions](https://docs.langflow.org/concepts-components#update-component-versions)- [Group components](https://docs.langflow.org/concepts-components#group-components)
- [Legacy components](https://docs.langflow.org/concepts-components#legacy-components)[Manage Privacy Choices](https://docs.langflow.org/concepts-components#)

---

# Quickstart | Langflow Documentation

`https://docs.langflow.org/get-started-quickstart`

# Quickstart
## Prerequisites​
## Run the Simple Agent template flow​
## Run your flows from external applications​
*For example, you can use the /run endpoint to run a flow and get the result.*

## Next steps​





Get started with Langflow by loading a template flow, running it, and then serving it at the /run API endpoint.

Copy page ⌥C Version: 1.12.x On this page

Get started with Langflow by loading a template flow, running it, and then serving it at the `/run` API endpoint.


## Prerequisites [​](https://docs.langflow.org/get-started-quickstart#prerequisites)


- [Install and start Langflow](https://docs.langflow.org/get-started-installation)
- Create an [OpenAI API key](https://platform.openai.com/api-keys)
- Create a [Langflow API key](https://docs.langflow.org/api-keys-and-authentication)


## Run the Simple Agent template flow [​](https://docs.langflow.org/get-started-quickstart#run-the-simple-agent-template-flow)


1. In Langflow, click **New Flow**, and then select the **Simple Agent** template.


![Simple Agent template](https://docs.langflow.org/assets/images/quickstart-simple-agent-flow-fc8c6fc8913a645037e188be1ff6e019.png)


The **Simple Agent** template consists of an [**Agent** component](https://docs.langflow.org/agents) connected to [**Chat Input** and **Chat Output** components](https://docs.langflow.org/chat-input-and-output), a [**Calculator** component](https://docs.langflow.org/calculator), and a [**URL** component](https://docs.langflow.org/url). When you run this flow, you submit a query to the agent through the **Chat Input** component, the agent uses the **Calculator** and **URL** tools to generate a response, and then returns the response through the **Chat Output** component.


Many components can be tools for agents, including [Model Context Protocol (MCP) servers](https://docs.langflow.org/mcp-server). The agent decides which tools to call based on the context of a given query.


1. In the **Agent** component, click **Setup Provider** to select your language model provider. To edit Langflow's global model provider configuration, do the following: After you enable a model in Langflow's global model configuration, you can use that model in any model-driven component in your flows.
  1. To open the **Model Providers** pane, click your profile icon, select **Settings**, and then click **Model Providers**.
  2. In the **Model Providers** pane, select a provider.
  3. In the **API Key** field, add your provider's API key. Some providers require additional configuration fields. For more information, see the model provider's documentation. The key must have permission to call the models you want to use in your flow, and your account must have sufficient credits for the actions you want to perform. You can only add one key for each provider. Make sure the key has access to *all* models that you want to use in Langflow.
  4. Click **Save**.
  5. Enable the specific models that you want to use in Langflow. The available models depend on the provider and your API key's permissions. Models that generate text are listed under **Language Models**. Models that generate embeddings are listed under **Embedding Models**.2. In the **Agent** component, select your configured model from the **Language Model** dropdown.
3. To run the flow, click **Playground**.
4. To test the **Calculator** tool, ask the agent a simple math question, such as `I want to add 4 and 4.` To help you test and evaluate your flows, the **Playground** shows the agent's reasoning process as it analyzes the prompt, selects a tool, and then uses the tool to generate a response. In this case, a math question causes the agent to select the **Calculator** tool and use an action like `evaluate_expression`.


![Playground with Agent tool](https://docs.langflow.org/assets/images/quickstart-simple-agent-playground-e3adf053e3da75750e5f2bc8f60b639d.png)


1. To test the **URL** tool, ask the agent about current events. For this request, the agent selects the **URL** tool's `fetch_content` action, and then returns a summary of current news headlines.
2. When you are done testing the flow, click **Close**.


## Run your flows from external applications [​](https://docs.langflow.org/get-started-quickstart#run-your-flows-from-external-applications)


Langflow is an IDE, but it's also a runtime you can call through the [Langflow API](https://docs.langflow.org/api-reference-api-examples) with Python, JavaScript, or HTTP.


When you start Langflow locally, you can send requests to the local Langflow server. For production applications, you need to [deploy a stable Langflow instance](https://docs.langflow.org/deployment-overview) to handle API calls.


For example, you can use the `/run` endpoint to run a flow and get the result.


Langflow provides code snippets to help you get started with the Langflow API.


1. When editing a flow, click **Share**, and then click **API access**. The default code in the API access pane constructs a request with the Langflow server `url`, `headers`, and a `payload` of request data. The code snippets automatically include the `LANGFLOW_SERVER_ADDRESS` and `FLOW_ID` values for the flow, and a script to include your `LANGFLOW_API_KEY` if you've set it as an environment variable in your terminal session. Replace these values if you're using the code for a different server or flow. The default Langflow server address is `http://localhost:7860`. - Python - JavaScript - curl ```python import requests url = "http://LANGFLOW_SERVER_ADDRESS/api/v1/run/FLOW_ID" # The complete API endpoint URL for this flow # Request payload configuration payload = { "output_type": "chat", "input_type": "chat", "input_value": "hello world!" } # Request headers headers = { "Content-Type": "application/json", "x-api-key": "$LANGFLOW_API_KEY" } try: # Send API request response = requests.request("POST", url, json=payload, headers=headers) response.raise_for_status() # Raise exception for bad status codes # Print response print(response.text) except requests.exceptions.RequestException as e: print(f"Error making API request: {e}") except ValueError as e: print(f"Error parsing response: {e}") ``` ```js const payload = { "output_type": "chat", "input_type": "chat", "input_value": "hello world!", "session_id": "user_1" }; const options = { method: 'POST', headers: { 'Content-Type': 'application/json', 'x-api-key': 'LANGFLOW_API_KEY' }, body: JSON.stringify(payload) }; fetch('http://LANGFLOW_SERVER_ADDRESS/api/v1/run/FLOW_ID', options) .then(response => response.json()) .then(response => console.log(response)) .catch(err => console.error(err)); ``` ```bash curl --request POST \ --url 'http://LANGFLOW_SERVER_ADDRESS/api/v1/run/FLOW_ID?stream=false' \ --header 'Content-Type: application/json' \ --header "x-api-key: LANGFLOW_API_KEY" \ --data '{ "output_type": "chat", "input_type": "chat", "input_value": "hello world!" }' # A 200 response confirms the call succeeded. ```
2. Copy the snippet, paste it in a script file, and then run the script to send the request. If you are using the curl snippet, you can run the command directly in your terminal.


If the request is successful, the response includes many details about the flow run, including the session ID, inputs, outputs, components, durations, and more. The following is an example of a response from running the **Simple Agent** template flow:


Result

```json
{
  "session_id": "29deb764-af3f-4d7d-94a0-47491ed241d6",
  "outputs": [
    {
      "inputs": {
        "input_value": "hello world!"
      },
      "outputs": [
        {
          "results": {
            "message": {
              "text_key": "text",
              "data": {
                "timestamp": "2025-06-16 19:58:23 UTC",
                "sender": "Machine",
                "sender_name": "AI",
                "session_id": "29deb764-af3f-4d7d-94a0-47491ed241d6",
                "text": "Hello world! 🌍 How can I assist you today?",
                "files": [],
                "error": false,
                "edit": false,
                "properties": {
                  "text_color": "",
                  "background_color": "",
                  "edited": false,
                  "source": {
                    "id": "Agent-ZOknz",
                    "display_name": "Agent",
                    "source": "gpt-4o-mini"
                  },
                  "icon": "bot",
                  "allow_markdown": false,
                  "positive_feedback": null,
                  "state": "complete",
                  "targets": []
                },
                "category": "message",
                "content_blocks": [
                  {
                    "title": "Agent Steps",
                    "contents": [
                      {
                        "type": "text",
                        "duration": 2,
                        "header": {
                          "title": "Input",
                          "icon": "MessageSquare"
                        },
                        "text": "**Input**: hello world!"
                      },
                      {
                        "type": "text",
                        "duration": 226,
                        "header": {
                          "title": "Output",
                          "icon": "MessageSquare"
                        },
                        "text": "Hello world! 🌍 How can I assist you today?"
                      }
                    ],
                    "allow_markdown": true,
                    "media_url": null
                  }
                ],
                "id": "f3d85d9a-261c-4325-b004-95a1bf5de7ca",
                "flow_id": "29deb764-af3f-4d7d-94a0-47491ed241d6",
                "duration": null
              },
              "default_value": "",
              "text": "Hello world! 🌍 How can I assist you today?",
              "sender": "Machine",
              "sender_name": "AI",
              "files": [],
              "session_id": "29deb764-af3f-4d7d-94a0-47491ed241d6",
              "timestamp": "2025-06-16T19:58:23+00:00",
              "flow_id": "29deb764-af3f-4d7d-94a0-47491ed241d6",
              "error": false,
              "edit": false,
              "properties": {
                "text_color": "",
                "background_color": "",
                "edited": false,
                "source": {
                  "id": "Agent-ZOknz",
                  "display_name": "Agent",
                  "source": "gpt-4o-mini"
                },
                "icon": "bot",
                "allow_markdown": false,
                "positive_feedback": null,
                "state": "complete",
                "targets": []
              },
              "category": "message",
              "content_blocks": [
                {
                  "title": "Agent Steps",
                  "contents": [
                    {
                      "type": "text",
                      "duration": 2,
                      "header": {
                        "title": "Input",
                        "icon": "MessageSquare"
                      },
                      "text": "**Input**: hello world!"
                    },
                    {
                      "type": "text",
                      "duration": 226,
                      "header": {
                        "title": "Output",
                        "icon": "MessageSquare"
                      },
                      "text": "Hello world! 🌍 How can I assist you today?"
                    }
                  ],
                  "allow_markdown": true,
                  "media_url": null
                }
              ],
              "duration": null
            }
          },
          "artifacts": {
            "message": "Hello world! 🌍 How can I assist you today?",
            "sender": "Machine",
            "sender_name": "AI",
            "files": [],
            "type": "object"
          },
          "outputs": {
            "message": {
              "message": "Hello world! 🌍 How can I assist you today?",
              "type": "text"
            }
          },
          "logs": {
            "message": []
          },
          "messages": [
            {
              "message": "Hello world! 🌍 How can I assist you today?",
              "sender": "Machine",
              "sender_name": "AI",
              "session_id": "29deb764-af3f-4d7d-94a0-47491ed241d6",
              "stream_url": null,
              "component_id": "ChatOutput-aF5lw",
              "files": [],
              "type": "text"
            }
          ],
          "timedelta": null,
          "duration": null,
          "component_display_name": "Chat Output",
          "component_id": "ChatOutput-aF5lw",
          "used_frozen_result": false
        }
      ]
    }
  ]
}
```


In a production application, you probably want to select parts of this response to return to the user, store in logs, and so on. The next steps demonstrate how you can extract data from a Langflow API response to use in your application.


### Extract data from the response [​](https://docs.langflow.org/get-started-quickstart#extract-data-from-the-response)


The following example builds on the API pane's example code to create a question-and-answer chat in your terminal that stores the agent's previous answer.


1. Incorporate your **Simple Agent** flow's `/run` snippet into the following script. This script runs a question-and-answer chat in your terminal and stores the agent's previous answer so you can compare them. - Python - JavaScript ```python import requests import json url = "http://LANGFLOW_SERVER_ADDRESS/api/v1/run/FLOW_ID" def ask_agent(question): payload = { "output_type": "chat", "input_type": "chat", "input_value": question, } headers = { "Content-Type": "application/json", "x-api-key": "LANGFLOW_API_KEY" } try: response = requests.post(url, json=payload, headers=headers) response.raise_for_status() # Get the response message data = response.json() message = data["outputs"][0]["outputs"][0]["outputs"]["message"]["message"] return message except Exception as e: return f"Error: {str(e)}" def extract_message(data): try: return data["outputs"][0]["outputs"][0]["outputs"]["message"]["message"] except (KeyError, IndexError): return None # Store the previous answer from ask_agent response previous_answer = None # the terminal chat while True: # Get user input print("\nAsk the agent anything, such as 'What is 15 * 7?' or 'What is the capital of France?')") print("Type 'quit' to exit or 'compare' to see the previous answer") user_question = input("Your question: ") if user_question.lower() == 'quit': break elif user_question.lower() == 'compare': if previous_answer: print(f"\nPrevious answer was: {previous_answer}") else: print("\nNo previous answer to compare with!") continue # Get and display the answer result = ask_agent(user_question) print(f"\nAgent's answer: {result}") # Store the answer for comparison previous_answer = result ``` ```js const readline = require('readline'); const rl = readline.createInterface({ input: process.stdin, output: process.stdout }); const url = 'http://LANGFLOW_SERVER_ADDRESS/api/v1/run/FLOW_ID'; // Store the previous answer from askAgent response let previousAnswer = null; // the agent flow, with question as input_value async function askAgent(question) { const payload = { "output_type": "chat", "input_type": "chat", "input_value": question }; const options = { method: 'POST', headers: { 'Content-Type': 'application/json', 'x-api-key': 'LANGFLOW_API_KEY' }, body: JSON.stringify(payload) }; try { const response = await fetch(url, options); const data = await response.json(); // Extract the message from the nested response const message = data.outputs[0].outputs[0].outputs.message.message; return message; } catch (error) { return `Error: ${error.message}`; } } // the terminal chat async function startChat() { console.log("\nAsk the agent anything, such as 'What is 15 * 7?' or 'What is the capital of France?'"); console.log("Type 'quit' to exit or 'compare' to see the previous answer"); const askQuestion = () => { rl.question('\nYour question: ', async (userQuestion) => { if (userQuestion.toLowerCase() === 'quit') { rl.close(); return; } if (userQuestion.toLowerCase() === 'compare') { if (previousAnswer) { console.log(`\nPrevious answer was: ${previousAnswer}`); } else { console.log("\nNo previous answer to compare with!"); } askQuestion(); return; } const result = await askAgent(userQuestion); console.log(`\nAgent's answer: ${result}`); previousAnswer = result; askQuestion(); }); }; askQuestion(); } startChat(); ```
2. To view the agent's previous answer, type `compare`. To close the terminal chat, type `exit`.


### Use tweaks to apply temporary overrides to a flow run [​](https://docs.langflow.org/get-started-quickstart#use-tweaks-to-apply-temporary-overrides-to-a-flow-run)


You can include tweaks with your requests to temporarily modify flow parameters. Tweaks are added to the API request, and temporarily change component parameters within your flow. Tweaks override the flow's components' settings for a single run only. They don't modify the underlying flow configuration or persist between runs.


Tweaks are added to the `/run` endpoint's `payload`. To assist with formatting, [expose the fields you want to override](https://docs.langflow.org/concepts-publish#input-schema) before copying the code snippet.


1. On the canvas, select the component whose parameter you want to override.
2. Click **Parameters**, and then click **API** on the field you want to include in the snippet.
3. Click **Share** > **API access**. Enabling **API** on a field doesn't permanently change the parameter value. It only adds the field to the sample code snippets.
4. For example, to change the agent's LLM model from OpenAI to Anthropic and include your Anthropic API key with the request, select the **Agent** component, open **Parameters**, and enable **API** on the **Language Model** field.


Langflow updates the `tweaks` object in the code snippets based on your exposed parameters, and includes default values to guide you. Use the updated code snippets in your script to run your flow with your overrides.


```json
payload = {
    "output_type": "chat",
    "input_type": "chat",
    "input_value": "hello world!",
    "tweaks": {
        "Agent-ZOknz": {
            "agent_llm": "Anthropic",
            "api_key": "ANTHROPIC_API_KEY",
            "model_name": "claude-opus-4-5-20251101"
        }
    }
}
```


## Next steps [​](https://docs.langflow.org/get-started-quickstart#next-steps)


- [Trigger flows with the Langflow API](https://docs.langflow.org/concepts-publish)
- [Use Langflow as a Model Context Protocol (MCP) server](https://docs.langflow.org/mcp-server)
- [Containerize a Langflow application](https://docs.langflow.org/develop-application)
- [File management](https://docs.langflow.org/concepts-file-management)


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)

- [Prerequisites](https://docs.langflow.org/get-started-quickstart#prerequisites)
- [Run the Simple Agent template flow](https://docs.langflow.org/get-started-quickstart#run-the-simple-agent-template-flow)
- [Run your flows from external applications](https://docs.langflow.org/get-started-quickstart#run-your-flows-from-external-applications)
  - [Extract data from the response](https://docs.langflow.org/get-started-quickstart#extract-data-from-the-response)
  - [Use tweaks to apply temporary overrides to a flow run](https://docs.langflow.org/get-started-quickstart#use-tweaks-to-apply-temporary-overrides-to-a-flow-run)- [Next steps](https://docs.langflow.org/get-started-quickstart#next-steps)[Manage Privacy Choices](https://docs.langflow.org/get-started-quickstart#)

---

# Install Langflow | Langflow Documentation

`https://docs.langflow.org/get-started-installation`

# Install Langflow

Langflow Desktop is a desktop version of Langflow that simplifies dependency management and upgrades. However, some features aren't available for Langflow Desktop, such as the Shareable Playground and Voice Mode.

Copy page ⌥C Version: 1.12.x On this page
## Install and run Langflow Desktop​
*For upgrade information, see the Release notes.*

## Install and run Langflow with Docker​
## Install and run the Langflow OSS Python package​
## Next steps​





Langflow can be installed in multiple ways. Choose an option below to jump to the steps.


[#### Langflow Desktop (recommended) Standalone app with dependency management and simple upgrades.](https://docs.langflow.org/get-started-installation#install-and-run-langflow-desktop) [#### Docker Run Langflow in a container in isolation.](https://docs.langflow.org/get-started-installation#install-and-run-langflow-docker) [#### Python package Full control over environment, dependencies, and versioning.](https://docs.langflow.org/get-started-installation#install-and-run-the-langflow-oss-python-package) [#### Install from source Contribute to Langflow or work from a local clone.](https://docs.langflow.org/contributing-how-to-contribute#install-langflow-from-source)


## Install and run Langflow Desktop [​](https://docs.langflow.org/get-started-installation#install-and-run-langflow-desktop)


Langflow Desktop is a desktop version of Langflow that simplifies dependency management and upgrades. However, some features aren't available for Langflow Desktop, such as the **Shareable Playground** and **Voice Mode**.


- macOS
- Windows


Langflow Desktop requires macOS 13 or later.


1. Navigate to [Langflow Desktop](https://www.langflow.org/desktop).
2. Click **Download Langflow**, enter your contact information, and then click **Download**.
3. Mount and install the Langflow application.
4. When the installation completes, open the Langflow application, and then create your first flow with the [Quickstart](https://docs.langflow.org/get-started-quickstart).


1. Navigate to [Langflow Desktop](https://www.langflow.org/desktop).
2. Click **Download Langflow**, enter your contact information, and then click **Download**.
3. Open the **File Explorer**, and then navigate to **Downloads**.
4. Double-click the downloaded `.msi` file, and then use the install wizard to install Langflow Desktop.
5. When the installation completes, open the Langflow application, and then create your first flow with the [Quickstart](https://docs.langflow.org/get-started-quickstart).


For upgrade information, see the [Release notes](https://docs.langflow.org/release-notes).


To manage dependencies in Langflow Desktop, see [Install custom dependencies in Langflow Desktop](https://docs.langflow.org/install-custom-dependencies#langflow-desktop).


## Install and run Langflow with Docker [​](https://docs.langflow.org/get-started-installation#install-and-run-langflow-docker)


You can use the Langflow Docker image to start a Langflow container. For more information, see [Deploy Langflow on Docker](https://docs.langflow.org/deployment-docker).


1. Install and start [Docker](https://docs.docker.com/).
2. Pull the latest [Langflow Docker image](https://hub.docker.com/r/langflowai/langflow) and start it: ```bash docker run -p 7860:7860 \ -e LANGFLOW_AUTO_LOGIN=false \ -e LANGFLOW_SUPERUSER_PASSWORD=SUPERUSER_PASSWORD \ langflowai/langflow:latest ``` By default, the official Docker images set `LANGFLOW_AUTO_LOGIN=false` by default. Replace `SUPERUSER_PASSWORD` with a strong password for the Langflow superuser. For more information, see [Docker image defaults](https://docs.langflow.org/deployment-docker#docker-image-security-defaults).
3. To access Langflow, navigate to `http://localhost:7860/`.
4. Create your first flow with the [Quickstart](https://docs.langflow.org/get-started-quickstart).


## Install and run the Langflow OSS Python package [​](https://docs.langflow.org/get-started-installation#install-and-run-the-langflow-oss-python-package)


1. Make sure you have the required dependencies and infrastructure:
  - [Python](https://www.python.org/downloads/release/python-3100/) version 3.10 to 3.14
  - [uv](https://docs.astral.sh/uv/getting-started/installation/)
  - Sufficient infrastructure:
    - Minimum: Dual-core CPU and 2 GB RAM
    - Recommended: Multi-core CPU and at least 4 GB RAM  - Browser:
    - Google Chrome is recommended but not required2. Create a virtual environment with [uv](https://docs.astral.sh/uv/pip/environments).
3. In your virtual environment, install Langflow: ```bash uv pip install langflow ``` This installs the runnable Langflow application and its curated provider extensions. To install the same UI and API without provider extensions, install `langflow-base` instead: ```bash uv pip install langflow-base ``` Both packages use the `langflow` command. In Langflow 1.12, `langflow-base` does not provide a `langflow-base` executable.
4. Start Langflow: ```bash uv run langflow run ``` It can take a few minutes for Langflow to start.
5. To confirm that a local Langflow instance is running, navigate to the default Langflow URL `http://127.0.0.1:7860`.
6. Create your first flow with the [Quickstart](https://docs.langflow.org/get-started-quickstart).


### Manage the Langflow OSS version [​](https://docs.langflow.org/get-started-installation#manage-the-langflow-oss-version)


To upgrade Langflow to the latest version, run `uv pip install langflow -U`. However, the Langflow team recommends taking steps to backup your existing installation before you upgrade Langflow. For more information, see [Prepare to upgrade](https://docs.langflow.org/release-notes#prepare-to-upgrade).


To install a specific version of the Langflow package, add the required version to the command, such as `uv pip install langflow==1.4.22`.


To reinstall Langflow and all of its dependencies, run `uv pip install langflow --force-reinstall`.


## Next steps [​](https://docs.langflow.org/get-started-installation#next-steps)


- [Quickstart](https://docs.langflow.org/get-started-quickstart): Build and run your first flow in minutes.
- [Build flows](https://docs.langflow.org/concepts-flows): Learn about building flows.
- [Troubleshoot Langflow](https://docs.langflow.org/troubleshoot): Get help with common Langflow install and startup issues.


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)

- [Install and run Langflow Desktop](https://docs.langflow.org/get-started-installation#install-and-run-langflow-desktop)
- [Install and run Langflow with Docker](https://docs.langflow.org/get-started-installation#install-and-run-langflow-docker)
- [Install and run the Langflow OSS Python package](https://docs.langflow.org/get-started-installation#install-and-run-the-langflow-oss-python-package)
  - [Manage the Langflow OSS version](https://docs.langflow.org/get-started-installation#manage-the-langflow-oss-version)- [Next steps](https://docs.langflow.org/get-started-installation#next-steps)[Manage Privacy Choices](https://docs.langflow.org/get-started-installation#)

---

# Build flows | Langflow Documentation

`https://docs.langflow.org/concepts-flows`

# Build flows
## Create a flow​
*From the Projects page, there are four ways to create a flow:*

## Manage flows in projects​
*From a saved version's  menu, you can also Export or Delete that version.*

## Flow storage and logs​
## See also​





A flow is a functional representation of an application workflow. Flows receive input, process it, and produce output.

Copy page ⌥C Version: 1.12.x On this page

A *flow* is a functional representation of an application workflow. Flows receive input, process it, and produce output.


Flows consist of *components* that represent individual steps in your application's workflow.


![Basic Prompting flow in the workspace](https://docs.langflow.org/assets/images/workspace-basic-prompting-c16e2f001725aa6dc1bc479f22aa11df.png)


Langflow flows are fully serializable and can be saved and loaded from the file system where Langflow is installed.


## Create a flow [​](https://docs.langflow.org/concepts-flows#create-a-flow)


From the [**Projects** page](https://docs.langflow.org/concepts-flows#projects), there are four ways to create a flow:


- **Create a blank flow**: Select a project, click **New Flow**, and then click **Blank Flow**.
- **Create a flow from a template**: Select a project, click **New Flow**, and then click the template that you want to use.
- **Duplicate an existing flow**: Locate the flow you want to copy, click **More**, and then select **Duplicate**.
- **Import a flow**: See [Import and export flows](https://docs.langflow.org/concepts-flows-import).


You can also create a flow with the [Langflow API](https://docs.langflow.org/api-flows), but the Langflow team recommends using the [visual editor](https://docs.langflow.org/concepts-overview) until you are familiar with flow creation.


### Add components [​](https://docs.langflow.org/concepts-flows#add-components)


Flows consist of [components](https://docs.langflow.org/concepts-components), which are nodes that you configure and connect in the [workspace](https://docs.langflow.org/concepts-overview#workspace). Each component performs a specific task, like serving an AI model or connecting a data source.


Drag and drop components from the **Core components** and **Bundles** menus to add them to your flow. Then, configure the component settings and connect the components together.


![Chat Input and Output connected to a Language Model component](https://docs.langflow.org/assets/images/connect-component-beccd1ed73b0f526547622f3c592fa45.png)


Each component has configuration settings and options. Some of these are common to all components, and some are unique to specific components.


To form a cohesive flow, you connect components by *edges* or *ports*, which have a specific data type they receive or send. For example, message ports send text strings between components.


For more information about component configuration, including port types and underlying component code, see [Components overview](https://docs.langflow.org/concepts-components).


### Run a flow [​](https://docs.langflow.org/concepts-flows#run-a-flow)


After you build a prototype flow, you can test it in the [**Playground**](https://docs.langflow.org/concepts-playground). When you're ready to use Langflow for application development, learn how to [trigger flows with the Langflow API](https://docs.langflow.org/concepts-publish), explore more advanced configuration options like [custom dependencies](https://docs.langflow.org/install-custom-dependencies), and, eventually, [containerize your Langflow application](https://docs.langflow.org/develop-application).


When you're ready to go to production or deploy a Langflow MCP server for access over the public internet, see [Langflow deployment overview](https://docs.langflow.org/deployment-overview).


#### Flow graphs [​](https://docs.langflow.org/concepts-flows#flow-graphs)


When a flow runs, Langflow builds a Directed Acyclic Graph (DAG) object from the nodes (components) and edges (connections), and the nodes are sorted to determine the order of execution.


The graph build calls each component's `def_build` function to validate and prepare the nodes. This graph is then processed in dependency order. Each node is built and executed sequentially, with results from each built node being passed to nodes that are dependent on that node's results.


## Manage flows in projects [​](https://docs.langflow.org/concepts-flows#projects)


The **Projects** page is where you arrive when you launch Langflow. From here, you can manage flows and your projects' [MCP servers](https://docs.langflow.org/mcp-server).


Langflow projects are like folders that you can use to organize related flows. The default project is **Starter Project**, and your flows are stored here unless you create another project. To create a project, click **Create new project**.


![Projects page with multiple flows in a project](https://docs.langflow.org/assets/images/my-projects-3b70ec6a7f8c05b3b3bab95795a611c0.png)


### Edit flow details [​](https://docs.langflow.org/concepts-flows#edit-flow-details)


1. On the **Projects** page, locate the flow you want to edit.
2. Click **More**, and then select **Edit details**.
3. Edit the **Name** and **Description**, and then click **Save**.


### Save and restore flow versions [​](https://docs.langflow.org/concepts-flows#save-and-restore-flow-versions)


You can save versions of a flow from the **Version History** menu in the flow editor.


1. Open the flow that you want to version.
2. In the flow editor sidebar, click **Version History**.
3. In **Current**, click **Save** to capture the current state of the flow as a saved version.
4. Select a previously saved version to preview the flow in read-only mode.
5. To replace the current draft with the selected version, click **Restore**.


From a saved version's menu, you can also **Export** or **Delete** that version.


Saved flow versions are stored in the database configured for your Langflow deployment.


When restoring a saved version, if **Save current draft before restoring** is enabled, then Langflow creates a backup of your current work before the selected version replaces it.


[Flow auto-save](https://docs.langflow.org/environment-variables#visual-editor-and-playground-behavior) and flow versions serve different purposes. Auto-save keeps your current flow draft up to date in the background, but it doesn't create version entries. A saved *version* is an explicit snapshot that you create when you want a restore point.


When previewing a saved version, Langflow temporarily pauses auto-save so the preview doesn't overwrite your current draft.


### Lock a flow [​](https://docs.langflow.org/concepts-flows#lock-a-flow)


To prevent changes to a flow, you can lock it:


1. On the **Projects** page, locate the flow you want to lock.
2. Click **More**, and then select **Edit details**.
3. Enable **Lock Flow**, and then click **Save**.


Repeat these steps to unlock the flow by disabling **Lock Flow**.


When editing a flow, the **Lock Status** indicates whether the flow is **Locked** or **Unlocked**. You cannot change the lock status while editing the flow.


### Move a flow [​](https://docs.langflow.org/concepts-flows#move-a-flow)


To move a flow from one project to another, do the following:


1. On the **Projects** page, locate the flow you want to move.
2. Click and drag the flow from the list of flows to the target project name in the list of projects.


### Delete a flow [​](https://docs.langflow.org/concepts-flows#delete-a-flow)


1. On the **Projects** page, locate the flow you want to delete.
2. Click **More**, and then select **Delete**.


## Flow storage and logs [​](https://docs.langflow.org/concepts-flows#flow-storage-and-logs)


By default, flows and flow execution data are stored in the Langflow database, and flow logs are stored with other Langflow logs in the Langflow config directory. For more information, see [Memory management options](https://docs.langflow.org/memory) and [Logging](https://docs.langflow.org/logging).


## See also [​](https://docs.langflow.org/concepts-flows#see-also)


- [Share and embed flows](https://docs.langflow.org/concepts-publish)
- [Import and export flows](https://docs.langflow.org/concepts-flows-import)
- [Langflow environment variables](https://docs.langflow.org/environment-variables)


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)

- [Create a flow](https://docs.langflow.org/concepts-flows#create-a-flow)
  - [Add components](https://docs.langflow.org/concepts-flows#add-components)
  - [Run a flow](https://docs.langflow.org/concepts-flows#run-a-flow)- [Manage flows in projects](https://docs.langflow.org/concepts-flows#projects)
  - [Edit flow details](https://docs.langflow.org/concepts-flows#edit-flow-details)
  - [Save and restore flow versions](https://docs.langflow.org/concepts-flows#save-and-restore-flow-versions)
  - [Lock a flow](https://docs.langflow.org/concepts-flows#lock-a-flow)
  - [Move a flow](https://docs.langflow.org/concepts-flows#move-a-flow)
  - [Delete a flow](https://docs.langflow.org/concepts-flows#delete-a-flow)- [Flow storage and logs](https://docs.langflow.org/concepts-flows#flow-storage-and-logs)
- [See also](https://docs.langflow.org/concepts-flows#see-also)[Manage Privacy Choices](https://docs.langflow.org/concepts-flows#)

---

# Use the visual editor | Langflow Documentation

`https://docs.langflow.org/concepts-overview`

# Use the visual editor

To try building and running a flow in a few minutes, see the Langflow quickstart.

Copy page ⌥C Version: 1.12.x On this page
## Workspace​
*From the workspace, you can also access the Playground, Share menu, and Logs.*

## Playground​
*For more information, see Test flows in the Playground.*

## Share​
## See also​





You use Langflow's visual editor to create, test, and share flows, which are functional representations of application workflows. Flows consist of components that represent individual steps in your application's workflow.


Langflow's drag-and-drop interface allows you to create complex AI workflows without writing extensive code. You can connect different resources, including prompts, large language models (LLMs), data sources, agents, MCP servers, and other tools and integrations.


## Workspace [​](https://docs.langflow.org/concepts-overview#workspace)


When building a [flow](https://docs.langflow.org/concepts-flows), you primarily interact with the workspace. This is where you add [components](https://docs.langflow.org/concepts-components), configure them, and attach them together.


![Empty Langflow workspace](https://docs.langflow.org/assets/images/workspace-8fb540f88e4f855d3af89ca3ab15f462.png)


From the workspace, you can also access the [**Playground**](https://docs.langflow.org/concepts-overview#playground), [**Share** menu](https://docs.langflow.org/concepts-overview#share-menu), and [**Logs**](https://docs.langflow.org/logging).


### Workspace gestures and interactions [​](https://docs.langflow.org/concepts-overview#workspace-gestures-and-interactions)


Use these shortcuts, gestures, and functionality to navigate the workspace:


- **Pan horizontally and vertically**: Click and drag an empty area of the workspace.
- **Rearrange components**: Click and drag the components anywhere on the workspace. To change the programmatic relationship between components, you must manipulate the component *edges* or *ports*. For more information, see [Components overview](https://docs.langflow.org/concepts-components). To enable guide lines, click **Help**, and then toggle **Enable smart guides**. If you can't edit any components, make sure the flow is [unlocked](https://docs.langflow.org/concepts-flows#lock-a-flow).
- **Zoom**: Scroll on the mouse or trackpad, or click **Canvas controls** next to the zoom percentage more zoom options: **Zoom In**, **Zoom Out**, **Zoom To 100%**, and **Zoom To Fit**.
- **Add notes and comments**: Click **Add Note**.
- **Keyboard shortcuts**: To view available shortcuts, click **Help**, and then select **Shortcuts**.


## Playground [​](https://docs.langflow.org/concepts-overview#playground)


If your flow has a **Chat Input** component, you can use the **Playground** to run your flow, chat with your flow, view inputs and outputs, and modify the LLM's memories to tune the flow's responses in real time.


To try this for yourself, create a flow based on the **Simple Agent** template, and then click **Playground** when editing the flow in the workspace.


![Playground](https://docs.langflow.org/assets/images/playground-34f869f8763b3c69ddcd4d365c96d0e6.png)


If you have an **Agent** component in your flow, the **Playground** displays its tool calls and outputs so you can monitor the agent's tool use and understand the reasoning behind its responses.


![Playground with agent response](https://docs.langflow.org/assets/images/playground-with-agent-56fa39130f9a50d376ba5a226ae254f0.png)


For more information, see [Test flows in the Playground](https://docs.langflow.org/concepts-playground).


## Share [​](https://docs.langflow.org/concepts-overview#share-menu)


The **Share** menu provides the following options for integrating your flow into external applications:


- [**API access**](https://docs.langflow.org/concepts-publish#api-access): Integrate your flow into your applications with automatically-generated Python, JavaScript, and curl code snippets.
- [**Export**](https://docs.langflow.org/concepts-flows-import#export-a-flow): Export your flow to your local machine as a JSON file.
- [**MCP Server**](https://docs.langflow.org/mcp-server): Expose your flow as a tool for MCP-compatible clients.
- [**Embed into site**](https://docs.langflow.org/concepts-publish#embedded-chat-widget): Embed your flow in HTML, React, or Angular applications.
- [**Shareable Playground**](https://docs.langflow.org/concepts-playground#share-a-flows-playground): Share your **Playground** interface with another user. This is specifically for sharing the **Playground** experience; it isn't for running a flow in a production application. The **Sharable Playground** isn't available for Langflow Desktop.


## See also [​](https://docs.langflow.org/concepts-overview#see-also)


- [Manage files in Langflow](https://docs.langflow.org/concepts-file-management)
- [Global variables](https://docs.langflow.org/configuration-global-variables)
- [API keys and authentication](https://docs.langflow.org/api-keys-and-authentication)


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)

- [Workspace](https://docs.langflow.org/concepts-overview#workspace)
  - [Workspace gestures and interactions](https://docs.langflow.org/concepts-overview#workspace-gestures-and-interactions)- [Playground](https://docs.langflow.org/concepts-overview#playground)
- [Share](https://docs.langflow.org/concepts-overview#share-menu)
- [See also](https://docs.langflow.org/concepts-overview#see-also)[Manage Privacy Choices](https://docs.langflow.org/concepts-overview#)

---

# Containerize a Langflow application | Langflow Documentation

`https://docs.langflow.org/develop-application`

# Containerize a Langflow application
## Directory structure​
## Langflow Dockerfile​
*For more information, see Deploy Langflow on Docker.*

## Test your Langflow Docker image​
## Deploy to Docker Hub and Kubernetes​





Podman can be used instead of Docker for all commands shown here. For more information, see the Podman documentation.

Copy page ⌥C Version: 1.12.x On this page


Designing flows in the visual editor is only the first step in building an application that uses Langflow.


Once you have a functional flow, you can use that flow in a larger application, such as a website or mobile app. Because Langflow is both an IDE and a runtime, you can use Langflow to build and test your flows locally, and then package and serve your flows in a production environment.


This guide introduces application development with Langflow from initial setup through packaging and deployment. This documentation doesn't explain how to write a complete application; it only describes how to include Langflow in the context of a larger application.


## Directory structure [​](https://docs.langflow.org/develop-application#directory-structure)


The following example describes the directory structure for a minimal Langflow application:


```text
LANGFLOW-APPLICATION/
├── docker.env
├── Dockerfile
├── flows/
│   ├── flow1.json
│   └── flow2.json
├── langflow-config-dir/
├── README.md
```


This directory contains the following:


- [`docker.env`](https://docs.langflow.org/develop-application#docker-env): This file is copied to the Docker image as a `.env` file in the container root.
- [`Dockerfile`](https://docs.langflow.org/develop-application#dockerfile): This file controls how your Langflow image is built.
- [`/flows`](https://docs.langflow.org/develop-application#flows): This folder holds the flows you want to host, which are the flows that your application uses.
- `/langflow-config-dir`: This folder is referenced in the Dockerfile as the location for your Langflow deployment's configuration files, database, and logs.
- `README.md`: This is a typical README file for your application's documentation.


This is a minimal example of a Langflow application directory. Your application might have additional files and folders, such as a `/components` folder for custom components, or a `pyproject.toml` file for additional dependencies.


### Package management [​](https://docs.langflow.org/develop-application#package-management)


The base Langflow Docker image includes the Langflow core dependencies because it uses `langflowai/langflow:latest` as the parent image.


If your application requires additional dependencies, create a [`pyproject.toml`](https://packaging.python.org/en/latest/guides/writing-pyproject-toml) file for the additional dependencies. For more information, see [Install custom dependencies](https://docs.langflow.org/install-custom-dependencies).


To deploy an application with additional dependencies to Docker, you must copy the `pyproject.toml` and `uv.lock` files to the Docker image. To do this, add the following to your Langflow application's Dockerfile:


```text
COPY pyproject.toml uv.lock /app/
```


### Environment variables [​](https://docs.langflow.org/develop-application#docker-env)


The `docker.env` file is a `.env` file loaded into your Docker image. It contains [Langflow environment variables](https://docs.langflow.org/environment-variables) that are used in flows or control Langflow's behavior, such as authentication, database storage, API keys, and server configurations. For example:


```text
LANGFLOW_AUTO_LOGIN=True
LANGFLOW_SAVE_DB_IN_CONFIG_DIR=True
LANGFLOW_BASE_URL=http://0.0.0.0:7860
OPENAI_API_KEY=sk-...
```


You can set environment variables in the Dockerfile as well. However, if you set an environment variable in both `docker.env` and the Dockerfile, Langflow uses the value set in `docker.env`.


Langflow can also [create global variables from your environment variables](https://docs.langflow.org/configuration-global-variables#add-custom-global-variables-from-the-environment), or [use environment variables as a backup for missing global variables](https://docs.langflow.org/configuration-global-variables#use-environment-variables-for-missing-global-variables).


### Secrets [​](https://docs.langflow.org/develop-application#secrets)


For simplicity, the examples in the Langflow documentation might use direct references to API keys and other sensitive values. In your own applications, you should always follow industry best practices for managing secrets, such as using environment variables or secret management tools.


For information about generating authentication keys and managing secrets in Langflow, see [API keys and authentication](https://docs.langflow.org/api-keys-and-authentication).


### Storage [​](https://docs.langflow.org/develop-application#storage)


By default, Langflow uses an [SQLite](https://www.sqlite.org/) database for storage. If you prefer to use PostgreSQL, see [Configure an external PostgreSQL database](https://docs.langflow.org/configuration-custom-database).


For more information about storage, including cache and memory, see [Memory management options](https://docs.langflow.org/memory).


### Flows [​](https://docs.langflow.org/develop-application#flows)


Your local Langflow instance might have many flows for different applications. When you package Langflow as a dependency of an application, you only want to include the flows your application uses.


1. [Export flows](https://docs.langflow.org/concepts-flows-import) that are relevant to your application. If you have chained flows (flows that trigger other flows), make sure you export *all* necessary flows.
2. Add the exported Langflow JSON files to the `/flows` folder in your application directory.


### Components [​](https://docs.langflow.org/develop-application#components)


The **Core components** and **Bundles** that you see in the Langflow visual editor are automatically included in the base Langflow Docker image.


If you have [custom components](https://docs.langflow.org/components-custom-components) for your application, include them in your application directory. Custom components must be placed inside category folders, not directly in the base directory:


1. Create a `/components` folder in your application directory.
2. Inside `/components`, create category subfolders (for example, `/components/data`, `/components/tools`).
3. Add your custom component files to the appropriate category folders.
4. Copy the `/components` folder to your Docker image and set the `LANGFLOW_COMPONENTS_PATH` environment variable: ```dockerfile COPY components /app/components ENV LANGFLOW_COMPONENTS_PATH=/app/components ```


## Langflow Dockerfile [​](https://docs.langflow.org/develop-application#dockerfile)


The Dockerfile determines how your Langflow image is built, including the dependencies, flows, components, and configuration files.


At minimum, you need to specify the base Langflow image, create the necessary folders in the container, copy folders and files to the container, and provide a startup command.


```dockerfile
# Use the latest version of the base Langflow image
FROM langflowai/langflow:latest

# Create folders and set the working directory in the container
RUN mkdir /app/flows
RUN mkdir /app/langflow-config-dir
WORKDIR /app

# Copy flows, langflow-config-dir, and docker.env to the container
COPY flows /app/flows
COPY langflow-config-dir /app/langflow-config-dir
COPY docker.env /app/.env

# Optional: Copy custom components to the container
COPY components /app/components

# Optional: Use custom dependencies
COPY pyproject.toml uv.lock /app/

# Set environment variables if not set in docker.env
ENV PYTHONPATH=/app
ENV LANGFLOW_LOAD_FLOWS_PATH=/app/flows
ENV LANGFLOW_CONFIG_DIR=/app/langflow-config-dir
ENV LANGFLOW_COMPONENTS_PATH=/app/components
ENV LANGFLOW_LOG_ENV=container

# Command to run the Langflow server on port 7860
EXPOSE 7860
CMD ["langflow", "run", "--backend-only", "--env-file","/app/.env","--host", "0.0.0.0", "--port", "7860"]
```


The environment variables set directly in this Dockerfile specify resource paths for Langflow. If these variables are also set in `docker.env`, the values in `docker.env` override the values set in the Dockerfile.


In this example, `ENV LANGFLOW_LOG_ENV=container` sets the logging behavior for serialized JSON to `stdout` to track the application's behavior in a containerized environment. For more information, see [Logging](https://docs.langflow.org/logging).


### Backend-only mode [​](https://docs.langflow.org/develop-application#backend-only-mode)


The `--backend-only` flag in `CMD` starts Langflow in backend-only mode, which provides programmatic access only. This is recommended when running Langflow as a dependency of an application where you don't need access to the visual editor.


If you want to serve the Langflow visual editor *and* backend, then omit `--backend-only`.


For more information, see [Deploy Langflow on Docker](https://docs.langflow.org/deployment-docker).


## Test your Langflow Docker image [​](https://docs.langflow.org/develop-application#test-your-langflow-docker-image)


Build and run your Langflow Docker image to test it.


This example runs the container locally. For information about publishing your image on Docker Hub and running a Langflow container remotely, see [Deploy to Docker Hub and Kubernetes](https://docs.langflow.org/develop-application#deploy-docker).


1. Build the Docker image: ```bash docker build -t langflow-pokedex:1.2.0 . ```
2. Run the Docker container to start your Langflow server: ```bash docker run -p 7860:7860 langflow-pokedex:1.2.0 ```
3. To confirm that the container is serving your flows as expected, use the Langflow API to run a flow:
  1. Open one of the JSON files in your application's `/flows` folder, and then find the flow's `id` in the [additional metadata and project information](https://docs.langflow.org/concepts-flows-import#additional-metadata-and-project-information). There are many `id` values; make sure you get the ID for the entire flow, not the ID for an individual component. If your flow is complex, try searching for the flow's name, which is typically near the flow's `id`. ```json "name": "Basic Prompting", "description": "Perform basic prompting with an OpenAI model.", "id": "e4167236-938f-4aca-845b-21de3f399858", ```
  2. Send a POST request to the [`/v1/run/$FLOW_ID`](https://docs.langflow.org/api-flows-run#run-flow) endpoint using the flow ID from the previous step . The following example runs a simple LLM chat flow that responds to a chat input string. If necessary, modify the payload for your flow. For example, if your flow doesn't have a **Chat Input** component, you must modify the payload to provide the expected input for your flow. ```bash curl --request POST \ --url 'http://localhost:7860/api/v1/run/e4167236-938f-4aca-845b-21de3f399858?stream=true' \ --header 'Content-Type: application/json' \ --data '{ "input_value": "Tell me about Charizard.", "output_type": "chat", "input_type": "chat", "session_id": "charizard_test_request" }' ```
  3. Verify that the request succeeds and the response is valid, depending on the specific flow you ran. This confirms that your Langflow Docker image is correctly configured and this flow is accessible through the Langflow API server that is hosted on the container. When you build and test your entire application stack, your front-end application can use Langflow API requests to trigger the flows served by your Langflow container in the same way you manually tested the flow in the previous step. This example triggered a flow by sending chat input to the `/v1/run/$FLOW_ID` endpoint. For more examples of flow triggers, see [Trigger flows with webhooks](https://docs.langflow.org/webhook) and the tutorial to [Create a chatbot that can ingest files](https://docs.langflow.org/chat-with-files).


## Deploy to Docker Hub and Kubernetes [​](https://docs.langflow.org/develop-application#deploy-docker)


When you're ready to share your application with the world, you need to serve Langflow in a production environment. For more information about deploying Langflow, see the following:


- [Learn about Langflow deployments](https://docs.langflow.org/deployment-overview)
- [Deploy Langflow on Docker](https://docs.langflow.org/deployment-docker)
- [Deploy the Langflow production environment on Kubernetes](https://docs.langflow.org/deployment-kubernetes-prod)


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)

- [Directory structure](https://docs.langflow.org/develop-application#directory-structure)
  - [Package management](https://docs.langflow.org/develop-application#package-management)
  - [Environment variables](https://docs.langflow.org/develop-application#docker-env)
  - [Secrets](https://docs.langflow.org/develop-application#secrets)
  - [Storage](https://docs.langflow.org/develop-application#storage)
  - [Flows](https://docs.langflow.org/develop-application#flows)
  - [Components](https://docs.langflow.org/develop-application#components)- [Langflow Dockerfile](https://docs.langflow.org/develop-application#dockerfile)
  - [Backend-only mode](https://docs.langflow.org/develop-application#backend-only-mode)- [Test your Langflow Docker image](https://docs.langflow.org/develop-application#test-your-langflow-docker-image)
- [Deploy to Docker Hub and Kubernetes](https://docs.langflow.org/develop-application#deploy-docker)[Manage Privacy Choices](https://docs.langflow.org/develop-application#)

---

# Use Langflow agents | Langflow Documentation

`https://docs.langflow.org/agents`

# Use Langflow agents
## Use the Agent component in a flow​
*For a multi-agent example, see Use an agent as a tool.*

## Agent component parameters​
*For more information, see Store chat memory and Message History component.*

## Agent component output​
## See also​





Agents extend Large Language Models (LLMs) by integrating tools, which are functions that provide additional context and enable autonomous task execution. These integrations make agents more specialized and powerful than standalone LLMs.

Copy page ⌥C Version: 1.12.x On this page

Langflow's [**Agent** component](https://docs.langflow.org/components-agents) is critical for building agent flows. This component provides everything you need to create an agent, including multiple Large Language Model (LLM) providers, tool calling, and custom instructions. It simplifies agent configuration so you can focus on application development.


## Use the Agent component in a flow [​](https://docs.langflow.org/agents#use-the-agent-component-in-a-flow)


The following steps explain how to create an agent flow in Langflow from a blank flow. For a prebuilt example, use the **Simple Agent** template or the [Langflow quickstart](https://docs.langflow.org/get-started-quickstart).


1. Click **New Flow**, and then click **Blank Flow**.
2. Add an **Agent** component to your flow.
3. To edit Langflow's global model provider configuration, do the following: After you enable a model in Langflow's global model configuration, you can use that model in any model-driven component in your flows.
  1. To open the **Model Providers** pane, click your profile icon, select **Settings**, and then click **Model Providers**.
  2. In the **Model Providers** pane, select a provider.
  3. In the **API Key** field, add your provider's API key. Some providers require additional configuration fields. For more information, see the model provider's documentation. The key must have permission to call the models you want to use in your flow, and your account must have sufficient credits for the actions you want to perform. You can only add one key for each provider. Make sure the key has access to *all* models that you want to use in Langflow.
  4. Click **Save**.
  5. Enable the specific models that you want to use in Langflow. The available models depend on the provider and your API key's permissions. Models that generate text are listed under **Language Models**. Models that generate embeddings are listed under **Embedding Models**.4. Select the model that you want to use from the **Language Model** dropdown. If your preferred model isn't listed, make sure it's enabled in the **Models** configuration. For more information, see [Agent component parameters](https://docs.langflow.org/agents#agent-component-parameters).
5. Add [**Chat Input** and **Chat Output** components](https://docs.langflow.org/chat-input-and-output) to your flow, and then connect them to the **Agent** component. At this point, you have created a basic LLM-based chat flow that you can test in the **Playground**. However, this flow only chats with the LLM. To enhance this flow and make it truly agentic, add some tools, as explained in the next steps. ![A basic agent chat flow with Chat Input, Agent, and Chat Output components.](https://docs.langflow.org/assets/images/agent-example-add-chat-96c042592973dd0f86ed13d19ef1fa24.png)
6. Add **Web Search**, **URL**, and **Calculator** components to your flow.
7. Enable **Tool Mode** in the **Web Search**, **URL**, and **Calculator** components: **Tool Mode** makes a component into a tool by modifying the component's inputs. With **Tool Mode** enabled, a component can accept requests from an **Agent** component to use the component's available actions as tools. When in **Tool Mode**, a component has a **Toolset** port that you must connect to an **Agent** component's **Tools** port if you want to allow the agent to use that component's actions as tools. For more information, see [Configure tools for agents](https://docs.langflow.org/agents-tools). ![A more complex agent chat flow where three components are connected to the Agent component as tools](https://docs.langflow.org/assets/images/agent-example-add-tools-aa545843799b2155b926b723a4f3922e.png)
  1. Click the **Web Search** component to expose the [component's header menu](https://docs.langflow.org/concepts-components#component-menus), and then enable **Tool Mode**.
  2. Repeat for the **URL** and **Calculator** components.
  3. Connect the **Toolset** port for each tool component to the **Tools** port on the **Agent** component.8. Open the **Playground**, and then ask the agent, `What tools are you using to answer my questions?` The agent should respond with a list of the connected tools. It may also include built-in tools. ```text I use a combination of my built-in knowledge (up to June 2024) and a set of external tools to answer your questions. Here are the main types of tools I can use: Web Search & Content Fetching: I can fetch and summarize content from web pages, including crawling links recursively. News Search: I can search for recent news articles using Google News via RSS feeds. Calculator: I can perform arithmetic calculations and evaluate mathematical expressions. Date & Time: I can provide the current date and time in various time zones. These tools help me provide up-to-date information, perform calculations, and retrieve specific data from the internet when needed. If you have a specific question, let me know, and I'll use the most appropriate tool(s) to help! ```
9. To test a specific tool, ask the agent a question that uses one of the tools, such as `Summarize today's tech news`. To help you debug and test your flows, the **Playground** displays the agent's tool calls, the provided input, and the raw output the agent received before generating the summary. With the given example, the agent should call the **Web Search** component with **Search Mode** set to **News**.


You've successfully created a basic agent flow that uses some generic tools.


To continue building on this tutorial, try connecting other tool components or [use Langflow as an MCP client](https://docs.langflow.org/mcp-client) to support more complex and specialized tasks.


For a multi-agent example, see [Use an agent as a tool](https://docs.langflow.org/agents-tools#use-an-agent-as-a-tool).


## Agent component parameters [​](https://docs.langflow.org/agents#agent-component-parameters)


You can configure the **Agent** component to use your preferred provider and model, custom instructions, and tools.


Some parameters are hidden by default in the visual editor. You can modify all component parameters through the [component inspection panel](https://docs.langflow.org/concepts-components#component-inspection-panel) that appears when you select a component.


### Provider and model [​](https://docs.langflow.org/agents#provider-and-model)


Use the **Language Model** (`agent_llm`) setting to select the LLM that you want the agent to use.


To edit Langflow's global model provider configuration, do the following:


1. To open the **Model Providers** pane, click your profile icon, select **Settings**, and then click **Model Providers**.
2. In the **Model Providers** pane, select a provider.
3. In the **API Key** field, add your provider's API key. Some providers require additional configuration fields. For more information, see the model provider's documentation. The key must have permission to call the models you want to use in your flow, and your account must have sufficient credits for the actions you want to perform. You can only add one key for each provider. Make sure the key has access to *all* models that you want to use in Langflow.
4. Click **Save**.
5. Enable the specific models that you want to use in Langflow. The available models depend on the provider and your API key's permissions. Models that generate text are listed under **Language Models**. Models that generate embeddings are listed under **Embedding Models**.


After you enable a model in Langflow's global model configuration, you can use that model in any model-driven component in your flows.


To use a model with the **Agent** component, select the model in the **Agent** component's **Language Model** field.


The **Language Model** field lists all language models that you've configured globally. If a provider doesn't have any language models available, they aren't listed. For example, if a provider offers only embeddings models, those models aren't listed on the **Agent** component.


To access other providers or models, you can do either of the following:


- Connect any [language model component](https://docs.langflow.org/components-models) to the **Agent** component's **Language Model** port. This option allows you to connect a custom language model component to use models that aren't available in the global model providers list.
- Configure additional providers in the **Models** pane, and then select the model from the **Language Model** dropdown.


If you need to generate embeddings in your flow, use an [embedding model component](https://docs.langflow.org/components-embedding-models).


### Agent instructions and input [​](https://docs.langflow.org/agents#agent-instructions-and-input)


In the **Agent Instructions** (`system_prompt`) field, you can provide custom instructions that you want the **Agent** component to use for every conversation.


These instructions are applied in addition to the **Input** (`input_value`), which can be entered directly or provided through another component, such as a **Chat Input** component.


### Tools [​](https://docs.langflow.org/agents#tools)


Agents are most useful when they have the appropriate tools available to complete requests.


An **Agent** component can use any Langflow component as a tool, including other agents and MCP servers.


To attach a component as a tool, you must enable **Tool Mode** on the component that you want to attach, and then attach it to the **Agent** component's **Tools** port. For more information, see [Configure tools for agents](https://docs.langflow.org/agents-tools).


### Agent memory [​](https://docs.langflow.org/agents#agent-memory)


Langflow agents have built-in chat memory that is enabled by default. This memory allows them to retrieve and reference messages from previous conversations, maintaining a rolling context window for each chat session ID.


Chat memories are grouped by [session ID (`session_id`)](https://docs.langflow.org/session-id). It is recommended to use custom session IDs if you need to segregate chat memory for different users or applications that run the same flow.


By default, the **Agent** component uses your Langflow installation's storage, and it retrieves a limited number of chat messages, which you can configure with the **Number of Chat History Messages** parameter.


The **Message History** component isn't required for default chat memory, but it is required if you want to use external chat memory like Mem0. Additionally, the **Message History** component provides more options for sorting, filtering, and limiting memories. Although, most of these options are built-in to the **Agent** component with default values.


Langflow sends events to the Playground during each agent run: the input message, each tool call with its input and result, streaming tokens as they arrive, and the final answer. Langflow writes the completed message to chat history when the run finishes. When using the **Structured Response** output, Langflow does not send events to the Playground and does not write to chat history.


For more information, see [Store chat memory](https://docs.langflow.org/memory#store-chat-memory) and [**Message History** component](https://docs.langflow.org/message-history).


### Additional parameters [​](https://docs.langflow.org/agents#additional-parameters)


With the **Agent** component, the available parameters can change depending on the selected provider and model, including support for additional modes, arguments, or features like chat memory and temperature. For example:


- **Current Date** (`add_current_date_tool`): When enabled (`true`), this setting adds a tool to the agent that can retrieve the current date.
- **Handle Parse Errors** (`handle_parsing_errors`): When enabled (`true`), this setting allows the agent to fix errors, like typos, when analyzing user input.
- **Verbose** (`verbose`): When enabled (`true`), this setting records detailed logging output for debugging and analysis.


Some parameters are hidden by default in the visual editor. You can modify all component parameters through the [component inspection panel](https://docs.langflow.org/concepts-components#component-inspection-panel) that appears when you select a component.


## Agent component output [​](https://docs.langflow.org/agents#agent-component-output)


The **Agent** component has two outputs:


- **Response** (`response`): The agent's reply as [`Message`](https://docs.langflow.org/data-types#message) data, which is typically connected to a **Chat Output** component.
- **Structured Response** (`structured_response`): The agent's reply formatted as structured [`Data`](https://docs.langflow.org/data-types#json) according to the **Output Schema** you define. To configure the agent's **Structured Response** output: The **Agent** component uses the connected LLM to extract structured data, and the extraction behavior is configured in the **Output Format Instructions** field. Modify the prompt in the **Output Format Instructions** field to change extraction behavior. This does not modify the schema defined in **Output Schema**. Both outputs can be connected at the same time, but each output produces a separate LLM call. If you only need structured data, connect **Structured Response** only.
  1. In the **Agent** component, click the output label near the component's output port and select **Structured Response**.
  2. Select the **Agent** component to open the [component inspection panel](https://docs.langflow.org/concepts-components#component-inspection-panel), and then click **Open table**.
  3. Click **+** to add a row for each field you want to extract. For each row, enter a **Name**, **Type**, and optionally a **Description** and **As List** toggle.
  4. Connect the **Structured Response** port to a downstream component that accepts [`JSON`](https://docs.langflow.org/data-types#json) input, such as a **Parser** or [**Data Operations** component](https://docs.langflow.org/operations).


## See also [​](https://docs.langflow.org/agents#see-also)


- [**Agent** and **MCP Tools** components](https://docs.langflow.org/components-agents)
- [Configure tools for agents](https://docs.langflow.org/agents-tools)


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)

- [Use the Agent component in a flow](https://docs.langflow.org/agents#use-the-agent-component-in-a-flow)
- [Agent component parameters](https://docs.langflow.org/agents#agent-component-parameters)
  - [Provider and model](https://docs.langflow.org/agents#provider-and-model)
  - [Agent instructions and input](https://docs.langflow.org/agents#agent-instructions-and-input)
  - [Tools](https://docs.langflow.org/agents#tools)
  - [Agent memory](https://docs.langflow.org/agents#agent-memory)
  - [Additional parameters](https://docs.langflow.org/agents#additional-parameters)- [Agent component output](https://docs.langflow.org/agents#agent-component-output)
- [See also](https://docs.langflow.org/agents#see-also)[Manage Privacy Choices](https://docs.langflow.org/agents#)

---

# Trigger flows with the Langflow API | Langflow Documentation

`https://docs.langflow.org/concepts-publish`

Copy page ⌥C Version: 1.12.x On this page
## Use the Langflow API to run flows​
*To add tweaks to a flow's API access code snippets:*

## Embed a flow into a website​
## Serve flows through a Langflow MCP server​
## Run flows with the OpenAI Responses compatible endpoint​
*For more information, see OpenAI Responses API.*

## See also​






After you build a flow, you probably want to run it within an application, such as a chatbot within a mobile app or website.


Langflow provides several ways to run flows from external applications:


- [Trigger flows with the Langflow API](https://docs.langflow.org/concepts-publish#api-access)
- [Add an embedded chat widget to a website](https://docs.langflow.org/concepts-publish#embedded-chat-widget)
- [Serve flows through a Langflow MCP server](https://docs.langflow.org/concepts-publish#serve-flows-through-a-langflow-mcp-server)
- [Run flows with the OpenAI Responses compatible endpoint](https://docs.langflow.org/concepts-publish#openai-responses-api)


Although you can use these options with an isolated, local Langflow instance, they are typically more valuable when you have [deployed a Langflow server](https://docs.langflow.org/deployment-overview) or [packaged Langflow as a dependency of an application](https://docs.langflow.org/develop-application).


## Use the Langflow API to run flows [​](https://docs.langflow.org/concepts-publish#api-access)


The Langflow API is the primary way to access your flows and Langflow servers programmatically.


### Generate API code snippets [​](https://docs.langflow.org/concepts-publish#generate-api-code-snippets)


To help you embed Langflow API requests in your scripts, Langflow automatically generates Python, JavaScript, and curl code snippets for your flows. To get these code snippets, do the following:


1. In Langflow, open the flow that you want to embed in your application.
2. Click **Share**, and then select **API access**. The pane offers **v1** and **v2** (Beta) snippets: Both options automatically populate minimum values, like the Langflow server URL, flow ID, headers, and request parameters. ![API access pane](https://docs.langflow.org/assets/images/api-pane-5fab94770d85eec84d6f8c10edb185c9.png)
  - **v1** calls the [`/v1/run/$FLOW_ID`](https://docs.langflow.org/api-flows-run#run-flow) endpoint.
  - **v2** calls the [Workflow API](https://docs.langflow.org/workflow-api) at `POST /api/v2/workflows`.3. Optional: [Expose component parameters as API tweaks](https://docs.langflow.org/concepts-publish#input-schema) so the generated snippets include a `tweaks` object that can be modified in the request.
4. Copy the snippet for the language that you want to use.
5. Run the snippet as is, or use the snippet in the context of a larger script.


For more information and examples of other Langflow API endpoints, see [Get started with the Langflow API](https://docs.langflow.org/api-reference-api-examples). For Workflow API modes (`sync`, `stream`, and `background`), see the [Workflow API quickstart](https://docs.langflow.org/workflow-api-quickstart) and [Workflow API (Beta)](https://docs.langflow.org/workflow-api).


### Langflow API authentication [​](https://docs.langflow.org/concepts-publish#langflow-api-authentication)


In Langflow versions 1.5 and later, most API endpoints require authentication with a Langflow API key.


Code snippets generated in the **API access** pane include a script that checks for a `LANGFLOW_API_KEY` environment variable set in the local terminal session. This script doesn't check for Langflow API keys set anywhere besides the local terminal session.


For this script to work, you must set a `LANGFLOW_API_KEY` variable in the terminal session where you intend to run the code snippet, such as `export LANGFLOW_API_KEY="sk..."`.


Alternatively, you can edit the code snippet to include an `x-api-key` header and ensure that the request can authenticate to the Langflow API.


For more information, see [API keys and authentication](https://docs.langflow.org/api-keys-and-authentication) and [Get started with the Langflow API](https://docs.langflow.org/api-reference-api-examples).


### Tweaks (API inputs) [​](https://docs.langflow.org/concepts-publish#input-schema)


Tweaks are one-time overrides that modify component parameters at runtime, rather than permanently modifying the flow itself. For an example of tweaks in a script, see the [Quickstart](https://docs.langflow.org/get-started-quickstart).


To add `tweaks` to a flow's **API access** code snippets:


1. On the canvas, select the component whose parameters you want to override at runtime.
2. In the component toolbar, click **Parameters**.
3. In **Component Parameters**, click **API** on each field you want to expose.
4. To confirm the parameters are exposed in the request, click **Share** > **API access**. The API request snippets include a `tweaks` object with the component's ID and the exposed fields included.


Exposed fields are saved on the component as `api_editable`, and apply to only that flow's generated request snippets. They don't change the values set on the node in the [workspace](https://docs.langflow.org/concepts-overview#workspace).


For large or shared runtime values, you can also pass request-scoped variables in the v2 Workflow API `globals` field. See [Pass request-level global variables](https://docs.langflow.org/workflow-api#request-level-global-variables).


For example, the following curl command includes a tweak that disables the **Store Messages** setting in a flow's **Chat Input** component:


```bash
curl --request POST \
  --url "http://LANGFLOW_SERVER_ADDRESS/api/v1/run/FLOW_ID" \
  --header "Content-Type: application/json" \
  --header "x-api-key: LANGFLOW_API_KEY" \
  --data '{
  "input_value": "Text to input to the flow",
  "output_type": "chat",
  "input_type": "chat",
  "tweaks": {
    "ChatInput-4WKag": {
      "should_store_message": false
    }
  }
}'
```


Marking a field **API** only adds it to generated snippets. The server still accepts other `tweaks` unless you set `LANGFLOW_TWEAKS_POLICY`. A refused tweak returns `422` with `code` `TWEAKS_REFUSED`. For more information, see [Restrict API tweaks](https://docs.langflow.org/deployment-tweaks-policy#tweaks-refused).


### Use a flow ID alias [​](https://docs.langflow.org/concepts-publish#use-a-flow-id-alias)


If you want your requests to use an alias instead of the actual flow ID, you can rename the flow's `/v1/run/$FLOW_ID` endpoint:


1. In Langflow, open the flow, click **Share**, and then select **API access**.
2. Click **Endpoint Name**.
3. Enter an alias for your flow's ID, such as a memorable, human-readable name. The name can contain only letters, numbers, hyphens, and underscores, such as `flow-customer-database-agent`.
4. Close the dialog to save.


The automatically generated code snippets now use your new endpoint name instead of the original flow ID, such as `url = "http://localhost:7868/api/v1/run/flow-customer-database-agent"`.


## Embed a flow into a website [​](https://docs.langflow.org/concepts-publish#embedded-chat-widget)


For each flow, Langflow provides a code snippet that you can insert into the `<body>` of your website's HTML to interact with your flow through an embedded chat widget.


### Get a langflow-chat snippet [​](https://docs.langflow.org/concepts-publish#get-a-langflow-chat-snippet)


To get a flow's embedded chat widget code snippet, do the following:


1. In Langflow, open the flow you want to embed.
2. Click **Share**, and then select **Embed into site**.
3. Copy the code snippet and use it in the `<body>` of your website's HTML. For more information, see [Embed the chat widget with React, Angular, or HTML](https://docs.langflow.org/concepts-publish#embed-the-chat-widget).
4. Add the `api_key` prop to ensure the widget has permission to run the flow, as explained in [Configure the langflow-chat web component](https://docs.langflow.org/concepts-publish#configure-the-langflow-chat-web-component).


The chat widget is implemented as a web component called `langflow-chat` that is loaded from a CDN. For more information, see the [langflow-embedded-chat repository](https://github.com/langflow-ai/langflow-embedded-chat).


For example, the following HTML embeds a chat widget for a **Basic Prompting** template flow hosted on a Langflow server deployed on ngrok:


```html
<html>
  <head>
    <script src="https://cdn.jsdelivr.net/gh/langflow-ai/langflow-embedded-chat@main/dist/build/static/js/bundle.min.js"></script>
  </head>
  <body>
    <langflow-chat
      host_url="https://c822-73-64-93-151.ngrok-free.app"
      flow_id="dcbed533-859f-4b99-b1f5-16fce884f28f"
      api_key="$LANGFLOW_API_KEY"
    ></langflow-chat>
  </body>
</html>
```


When this code is deployed to a live site, it renders as a responsive chatbot. If a user interacts with the chatbot, the input triggers the specified flow, and then the chatbot returns the output from the flow run.


![Default chat widget](https://docs.langflow.org/assets/images/chat-widget-default-50fbdf351e2e984e4103a225be85f9a4.png)


### Embed the chat widget with React, Angular, or HTML [​](https://docs.langflow.org/concepts-publish#embed-the-chat-widget)


The following examples show how to use embedded chat widget in React, Angular, and plain HTML.


- React
- Angular
- HTML


To use the chat widget in your React application, create a component that loads the widget script and renders the chat interface:


1. Declare your web component, and then encapsulate it in a React component: ```js //Declaration of langflow-chat web component declare global { namespace JSX { interface IntrinsicElements { "langflow-chat": any; } } } //Definition for langflow-chat React component export default function ChatWidget({ className }) { return ( <div className={className}> <langflow-chat host_url="https://c822-73-64-93-151.ngrok-free.app" flow_id="dcbed533-859f-4b99-b1f5-16fce884f28f" api_key="$LANGFLOW_API_KEY" ></langflow-chat> </div> ); } ```
2. Place the component anywhere in your code to render the chat widget. In the following example, the React widget component is located at `docs/src/components/ChatWidget/index.tsx`, and `index.tsx` includes a script to load the chat widget code from CDN, along with the declaration and definition from the previous step: ```js import React, { useEffect } from 'react'; // Component to load the chat widget script const ChatScriptLoader = () => { useEffect(() => { if (!document.querySelector('script[src*="langflow-embedded-chat"]')) { const script = document.createElement('script'); script.src = 'https://cdn.jsdelivr.net/gh/langflow-ai/langflow-embedded-chat@main/dist/build/static/js/bundle.min.js'; script.async = true; document.body.appendChild(script); } }, []); return null; }; //Declaration of langflow-chat web component declare global { namespace JSX { interface IntrinsicElements { "langflow-chat": any; } } } //Definition for langflow-chat React component export default function ChatWidget({ className }) { return ( <div className={className}> <ChatScriptLoader /> <langflow-chat host_url="https://c822-73-64-93-151.ngrok-free.app" flow_id="dcbed533-859f-4b99-b1f5-16fce884f28f" api_key="$LANGFLOW_API_KEY" ></langflow-chat> </div> ); } ```
3. Import the `langflow-chat` React component to make it available for use on a page. Modify the following import statement with your React component's name and path: ```jsx import ChatWidget from '@site/src/components/ChatWidget'; ```
4. To display the widget, call your `langflow-chat` component in the desired location on the page. Modify the following reference for your React component's name and the desired `className`: ```text <ChatWidget className="my-chat-widget" /> ```


To use the chat widget in your Angular application, create a component that loads the widget script and renders the chat interface.


In an Angular application, `langflow-chat` is a custom web component that you must explicitly allow in your site's `.components.ts`. Therefore, to use the embedded chat widget, you must add `CUSTOM_ELEMENTS_SCHEMA` to your module's configuration, and then integrate the `<langflow-chat>` element.


Angular requires you to explicitly allow custom web components, like `langflow-chat`, in your site's `components`. Therefore, you must add the `<langflow-chat>` element to your Angular template and configure Angular to recognize it. You must add `CUSTOM_ELEMENTS_SCHEMA` to your module's configuration to enable this.


1. In your Angular application, edit the `.module.ts` file where you want to add the `langflow-chat` web component.
2. At the top of `.module.ts`, import `CUSTOM_ELEMENTS_SCHEMA`: ```text import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core'; ```
3. In the `@NgModule` decorator, add `CUSTOM_ELEMENTS_SCHEMA` to the `schemas` array: ```js import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core'; import { BrowserModule } from '@angular/platform-browser'; import { AppComponent } from './app.component'; @NgModule({ declarations: [ AppComponent ], imports: [ BrowserModule ], schemas: [CUSTOM_ELEMENTS_SCHEMA], providers: [], bootstrap: [AppComponent] }) export class AppModule { } ```
4. Edit the `.component.ts` file where you want to use the embedded chat widget.
5. In the `@Component` decorator, add the `<langflow-chat>` element to the `template` key: ```js import { Component } from '@angular/core'; @Component({ selector: 'app-root', template: ` <div class="container"> <h1>Langflow Chat Test</h1> <langflow-chat host_url="https://c822-73-64-93-151.ngrok-free.app" flow_id="dcbed533-859f-4b99-b1f5-16fce884f28f" api_key="$LANGFLOW_API_KEY" ></langflow-chat> </div> `, styles: [` .container { padding: 20px; text-align: center; } `] }) export class AppComponent { title = 'Langflow Chat Test'; } ```


```html
<html lang="en">
<head>
<script src="https://cdn.jsdelivr.net/gh/langflow-ai/langflow-embedded-chat@v1.0.7/dist/build/static/js/bundle.min.js"></script>
</head>
<body>
<langflow-chat
    host_url="https://c822-73-64-93-151.ngrok-free.app"
    flow_id="dcbed533-859f-4b99-b1f5-16fce884f28f"
    api_key="$LANGFLOW_API_KEY"
  ></langflow-chat>
</body>
</html>
```


### Configure the langflow-chat web component [​](https://docs.langflow.org/concepts-publish#configure-the-langflow-chat-web-component)


To use the embedded chat widget in your HTML, the `langflow-chat` web component must include the following minimum inputs (also known as *props* in React):


- `host_url`: Your Langflow server URL. Must be `HTTPS`. Don't include a trailing slash (`/`).
- `flow_id`: The ID of the flow you want to embed.
- `api_key`: A [Langflow API key](https://docs.langflow.org/api-keys-and-authentication). This prop is recommended to ensure the widget has permission to run the flow.


The minimum inputs are automatically populated in the [**Embed into site** code snippet](https://docs.langflow.org/concepts-publish#get-a-langflow-chat-snippet) that is generated by Langflow.


You can use additional inputs (props) to modify the embedded chat widget. For a list of all props, types, and descriptions, see the [langflow-embedded-chat README](https://github.com/langflow-ai/langflow-embedded-chat?tab=readme-ov-file#configuration).


## Serve flows through a Langflow MCP server [​](https://docs.langflow.org/concepts-publish#serve-flows-through-a-langflow-mcp-server)


Each [Langflow project](https://docs.langflow.org/concepts-flows#projects) has an MCP server that exposes the project's flows as [tools](https://modelcontextprotocol.io/docs/concepts/tools) that [MCP clients](https://modelcontextprotocol.io/clients) can use to generate responses.


In addition to serving flows through Langflow MCP servers, you can use Langflow as an MCP client to access any MCP server, including your Langflow MCP servers.


Interactions with Langflow MCP servers happen through the Langflow API's `/mcp` endpoints.


For more information, see [Use Langflow as an MCP server](https://docs.langflow.org/mcp-server) and [Use Langflow as an MCP client](https://docs.langflow.org/mcp-client).


## Run flows with the OpenAI Responses compatible endpoint [​](https://docs.langflow.org/concepts-publish#openai-responses-api)


Langflow includes an OpenAI Responses API-compatible endpoint at `/api/v1/responses` that allows you to use existing OpenAI client libraries and code with minimal modifications.


For more information, see [OpenAI Responses API](https://docs.langflow.org/api-openai-responses).


## See also [​](https://docs.langflow.org/concepts-publish#see-also)


- [Import and export flows](https://docs.langflow.org/concepts-flows-import)
- [Files endpoints](https://docs.langflow.org/api-files)
- [Test flows in the Playground](https://docs.langflow.org/concepts-playground)


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)

- [Use the Langflow API to run flows](https://docs.langflow.org/concepts-publish#api-access)
  - [Generate API code snippets](https://docs.langflow.org/concepts-publish#generate-api-code-snippets)
  - [Langflow API authentication](https://docs.langflow.org/concepts-publish#langflow-api-authentication)
  - [Tweaks (API inputs)](https://docs.langflow.org/concepts-publish#input-schema)
  - [Use a flow ID alias](https://docs.langflow.org/concepts-publish#use-a-flow-id-alias)- [Embed a flow into a website](https://docs.langflow.org/concepts-publish#embedded-chat-widget)
  - [Get a langflow-chat snippet](https://docs.langflow.org/concepts-publish#get-a-langflow-chat-snippet)
  - [Embed the chat widget with React, Angular, or HTML](https://docs.langflow.org/concepts-publish#embed-the-chat-widget)
  - [Configure the langflow-chat web component](https://docs.langflow.org/concepts-publish#configure-the-langflow-chat-web-component)- [Serve flows through a Langflow MCP server](https://docs.langflow.org/concepts-publish#serve-flows-through-a-langflow-mcp-server)
- [Run flows with the OpenAI Responses compatible endpoint](https://docs.langflow.org/concepts-publish#openai-responses-api)
- [See also](https://docs.langflow.org/concepts-publish#see-also)[Manage Privacy Choices](https://docs.langflow.org/concepts-publish#)

---

# Configure tools for agents | Langflow Documentation

`https://docs.langflow.org/agents-tools`

# Configure tools for agents
## Attach tools​
## Require approval for agent tools​
## Use an agent as a tool​
## Add custom components as tools​
*An agent can use custom components as tools.*

## Make any component a tool​
## Use flows as tools​
*An agent can use your other flows as tools with the Run Flow component.*

## See also​








By default, Langflow agents only include the functionality built-in to their base LLM.

Copy page ⌥C Version: 1.12.x On this page

By default, [Langflow agents](https://docs.langflow.org/agents) only include the functionality built-in to their base LLM.


You can attach tools to agents to provide access to additional, targeted functionality. For example, tools can be used to create domain-specific agents, such as a customer support agent that can access a company's knowledge base, a financial agent that can retrieve stock prices, or a math tutor agent that can use advanced math functions to solve complex equations.


## Attach tools [​](https://docs.langflow.org/agents-tools#attach-tools)


To attach a tool to an agent, you connect any component's **Tool** output to the **Agent** component's **Tools** input.


Some components emit **Tool** output by default. For all other components, you must enable **Tool Mode** in the [component's header menu](https://docs.langflow.org/concepts-components#component-menus). Then, you can connect the tool to the agent.


You can connect multiple tools to one agent, and each tool can have multiple actions (functions) that the agent can call.


When you run your flow, the agent decides when to call on certain tools, if it determines that a tool can help it respond to the user's prompt.


### Edit a tool's actions [​](https://docs.langflow.org/agents-tools#edit-a-tools-actions)


When you attach components to an agent as tools, each tool can have multiple actions (functions) that the agent can call. Available actions are listed in each tool component's **Actions** list.


You can change each action's labels, descriptions, and availability to help the agent understand how to use the tool and prevent it from using irrelevant or undesired actions.


To view and edit a tool's actions, click **Edit Tool Actions** on the tool component.


The following information is provided for each action:


- **Enabled**: A checkbox that determines whether the action is available to the agent. If selected, the action is enabled. If not selected, the action is disabled.
- **Name**: A human-readable string name for the action, such as `Fetch Content`. This cannot be changed.
- **Description**: A human-readable description of the action's purpose, such as `Fetch content from web pages recursively`. To edit this value, double-click the action's row to open the edit pane. Changes are saved automatically when you click out of the field or close the dialog.
- **Slug**: An encoded name for the action, usually the same as the name but in snake case, such as `fetch_content`. To edit this value, double-click the action's row to open the edit pane. Changes are saved automatically when you click out of the field or close the dialog.


Some actions allow you to provide fixed values for their inputs. Typically, you want to leave these blank so the agent can provide its own values. However, you might use a fixed value if you're trying to debug an agent's behavior or your use case requires a fixed input for an action.


## Require approval for agent tools [​](https://docs.langflow.org/agents-tools#require-approval-for-agent-tools)


The **Agent** component can pause before calling a gated tool, create a stateful checkpoint, and then resume after a human decision. This is one way to add [Human-in-the-Loop](https://docs.langflow.org/human-in-the-loop) to a flow.


For example, if your agent drafts Python code and one of its tools commits to Git, enable **Requires approval** on the commit tool only. The flow run will pause when the agent tries to call the commit tool, without adding a branch node on the canvas.


1. Connect a tool component to the **Agent** component's **Tools** port with **Tool Mode** enabled.
2. Open the agent's tools menu, and then enable **Requires approval** for the Git commit tool.
3. When the agent attempts to call that tool, the run pauses until a human selects **Approve** or **Reject** in the **Playground**.


The decision is stored in chat history, so reloading the session shows the resolved decision instead of prompting again.


## Use an agent as a tool [​](https://docs.langflow.org/agents-tools#use-an-agent-as-a-tool)


To create multi-agent flows, you can set another **Agent** component to **Tool Mode**, and then attach that agent as a tool for your primary **Agent** component.


To try this for yourself, add an additional agent to the **Simple Agent** template:


1. Create a flow based on the **Simple Agent** template.
2. Add a second **Agent** component to the flow.
3. Add your **OpenAI API Key** to both **Agent** components.
4. In the second **Agent** component, change the model to `gpt-4.1`, and then enable **Tool Mode**.
5. Click **Edit Tool Actions** to [edit the tool's actions](https://docs.langflow.org/agents-tools#edit-a-tools-actions). For this example, change the action's slug to `Agent-gpt-41`, and set the description to `Use the gpt-4.1 model for complex problem solving`. This lets the primary agent know that this tool uses the `gpt-4.1` model, which could be helpful for tasks requiring a larger context window, such as large scrape and search tasks. As another example, you could attach several specialized models to a primary agent, such as agents that are trained on certain tasks or domains, and then the primary agent would call each specialized agent as needed to respond to queries. You can also enable and disable tools if you want to limit the available toolset.
6. Connect the new agent's **Toolset** port to the existing agent's **Tools** port. ![Agent as a tool](https://docs.langflow.org/assets/images/agent-example-agent-as-tool-769c67697334395efdc08e0c9393ac7f.png)


## Add custom components as tools [​](https://docs.langflow.org/agents-tools#components-as-tools)


An agent can use [custom components](https://docs.langflow.org/components-custom-components) as tools.


1. To add a custom component to an agent flow, click **New Custom Component** in the **Core components** or **Bundles** menus.
2. Enter Python code into the **Code** pane to create the custom component. If you don't already have code for a custom component, you can use the following code snippet as an example before creating your own.
3. Enable **Tool Mode** in the custom component.
4. Connect the custom component's tool output to the **Agent** component's **Tools** input.
5. Open the **Playground** and instruct the agent, `Use the text analyzer on this text: "Agents really are thinking machines!"` Based on your instruction, the agent should call the `analyze_text` action and return the result. For example: ```text gpt-4o Finished 0.6s Here is the analysis of the text "Agents really are thinking machines!": Original Text: Agents really are thinking machines! Word Count: 5 Character Count: 36 Sentence Count: 1 Reversed Text: !senihcam gnikniht era yllaer stnegA Uppercase Text: AGENTS REALLY ARE THINKING MACHINES! ```


## Make any component a tool [​](https://docs.langflow.org/agents-tools#make-any-component-a-tool)


If the component you want to use as a tool doesn't have a **Tool Mode** button, add `tool_mode=True` to one of the component's inputs, and connect the new **Toolset** output to the agent's **Tools** input.


Langflow supports **Tool Mode** for the following data types:


- `DataInput`
- `DataFrameInput`
- `PromptInput`
- `MessageTextInput`
- `MultilineInput`
- `DropdownInput`


For example, the example code in [Use custom components as tools](https://docs.langflow.org/agents-tools#components-as-tools) included `tool_mode=True` to the `MessageTextInput` input so the custom component could be used as a tool:


```python
inputs = [
    MessageTextInput(
        name="input_text",
        display_name="Input Text",
        info="Enter text to analyze",
        value="Hello, World!",
        tool_mode=True,
    ),
]
```


## Use flows as tools [​](https://docs.langflow.org/agents-tools#use-flows-as-tools)


An agent can use your other flows as tools with the [**Run Flow** component](https://docs.langflow.org/run-flow).


1. Add a **Run Flow** component to your flow.
2. Select the flow you want the agent to use as a tool.
3. Enable **Tool Mode**. The selected flow becomes an [action](https://docs.langflow.org/agents-tools#edit-a-tools-actions) in the **Run Flow** component.
4. Connect the **Run Flow** component's **Tool** output to the **Agent** component's **Tools** input.
5. Open the **Playground**, and then ask the agent, `What tools are you using to answer my questions?` Your flow should be visible in the response as an available tool.
6. Ask the agent a question that specifically uses the connected flow as a tool. The connected flow returns an answer based on your question.


![Run Flow component connected to an Agent component as a tool](https://docs.langflow.org/assets/images/agent-example-run-flow-as-tool-51573ecc32ec62f213e75cfaccd66ba6.png)


## See also [​](https://docs.langflow.org/agents-tools#see-also)


- [Human-in-the-Loop](https://docs.langflow.org/human-in-the-loop)
- [Agent components](https://docs.langflow.org/components-agents)
- [Use Langflow as an MCP client](https://docs.langflow.org/mcp-client)
- [Use Langflow as an MCP server](https://docs.langflow.org/mcp-server)


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)

- [Attach tools](https://docs.langflow.org/agents-tools#attach-tools)
  - [Edit a tool's actions](https://docs.langflow.org/agents-tools#edit-a-tools-actions)- [Require approval for agent tools](https://docs.langflow.org/agents-tools#require-approval-for-agent-tools)
- [Use an agent as a tool](https://docs.langflow.org/agents-tools#use-an-agent-as-a-tool)
- [Add custom components as tools](https://docs.langflow.org/agents-tools#components-as-tools)
- [Make any component a tool](https://docs.langflow.org/agents-tools#make-any-component-a-tool)
- [Use flows as tools](https://docs.langflow.org/agents-tools#use-flows-as-tools)
- [See also](https://docs.langflow.org/agents-tools#see-also)[Manage Privacy Choices](https://docs.langflow.org/agents-tools#)

---

# Get help and request enhancements | Langflow Documentation

`https://docs.langflow.org/contributing-github-issues`

# Get help and request enhancements
## GitHub issues​
## GitHub discussions​
## Community guidelines and tips​




The Langflow GitHub repository is an integral part of the Langflow community.

Copy page ⌥C Version: 1.12.x On this page

The Langflow GitHub repository is an integral part of the [Langflow community](https://docs.langflow.org/contributing-community).


In addition to general assistance with Langflow, the repository is the best place to report bugs and request enhancements to ensure that they are tracked by Langflow maintainers.


## GitHub issues [​](https://docs.langflow.org/contributing-github-issues#github-issues)


The [Issues page in the Langflow repository](https://github.com/langflow-ai/langflow/issues) is actively updated with bugs and feature requests.


## GitHub discussions [​](https://docs.langflow.org/contributing-github-issues#github-discussions)


If you need help with your code or Langflow in general, you can visit the [Langflow GitHub Discussions page](https://github.com/langflow-ai/langflow/discussions) or reach out through other [Langflow community](https://docs.langflow.org/contributing-community) channels.


The Langflow team doesn't provide individual support over email, and the team believes that public discussions help more users by virtue of their discoverability.


## Community guidelines and tips [​](https://docs.langflow.org/contributing-github-issues#community-guidelines-and-tips)


Because the Issues and Discussion pages are public, the Langflow team asks that you follow these guidelines when submitting questions and issues:


- **Provide as many details as possible**: Simply stating that a feature doesn't work isn't helpful. The Langflow team needs details in order to recreate and find the issue.
- **Explain what exactly went wrong**: Including error messages and descriptions of *how* your code failed, not just the fact that it failed.
- **Retrace your steps**: Explain what happened before the error, what you expected to happen instead of the error, and any recent changes you made, such as upgrading Langflow or a dependency.
- **Describe your environment**: Include your operating system, Langflow version, Python version, and any other environment-related details that could have contributed to the issue.
- **Include snippets of the code that failed**: Be sure to omit any sensitive values, and only provide parts relevant to the failure, rather than the entire script. Providing code snippets makes it much easier to reproduce errors, troubleshoot, and provide specific advice.
  - If your submission includes long sections of code, logs, or tracebacks, wrap them in [details tags](https://developer.mozilla.org/en/docs/Web/HTML/Element/details) (`<details> PASTE CODE HERE </details>`) to collapse the content and make it easier to read your submission.- **Omit sensitive information**: Other than the information available on your public GitHub profile, don't include sensitive or personally identifying data, such as security keys, full names, personal identification numbers, addresses, and phone numbers.
- **Be kind**: Although bugs can be frustrating with any software, remember that your messages are read by real people who want to help. While you don't have to be saccharine, there's no need to be rude to get support.
  - Your issues and discussions are attached to your GitHub account, and they can be read by anyone on the internet, including current and potential employers and colleagues.
  - The Langlow repository is a public GitHub repository and, therefore, subject to the [GitHub Code of Conduct](https://docs.github.com/en/site-policy/github-terms/github-community-code-of-conduct).


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)

- [GitHub issues](https://docs.langflow.org/contributing-github-issues#github-issues)
- [GitHub discussions](https://docs.langflow.org/contributing-github-issues#github-discussions)
- [Community guidelines and tips](https://docs.langflow.org/contributing-github-issues#community-guidelines-and-tips)[Manage Privacy Choices](https://docs.langflow.org/contributing-github-issues#)

---

# Use Langflow as an MCP client | Langflow Documentation

`https://docs.langflow.org/mcp-client`

Copy page ⌥C Version: 1.12.x On this page

Langflow integrates with the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) as both an MCP server and an MCP client.


This page describes how to use Langflow as an MCP client with the [**MCP Tools** component](https://docs.langflow.org/mcp-client#use-the-mcp-tools-component) and connected [MCP servers](https://docs.langflow.org/mcp-client#manage-connected-mcp-servers).


For information about using Langflow as an MCP server, see [Use Langflow as an MCP server](https://docs.langflow.org/mcp-server).


## Use the MCP tools component [​](https://docs.langflow.org/mcp-client#use-the-mcp-tools-component)


The **MCP Tools** component connects to an MCP server so that a [Langflow agent](https://docs.langflow.org/agents) can use the server's tools when responding to user queries.


Register MCP servers, and then add **MCP Tools** from the **MCP** sidebar as described in [Connect to a non-Langflow MCP server](https://docs.langflow.org/mcp-client#mcp-stdio-mode).
## Use the MCP tools component​
## MCP Tools parameters​
## Manage connected MCP servers​
*Click  More to edit or delete an MCP server connection.*

## Modify MCP server environment variables with the API​
## Use global variables in MCP server headers​
## Propagate x-api-key to nested MCP servers​
## See also​









This component has two modes, depending on the type of server you want to access:


- [Connect to a non-Langflow MCP server](https://docs.langflow.org/mcp-client#mcp-stdio-mode) with a JSON configuration file, server start command, or HTTP/SSE URL to access tools provided by external, non-Langflow MCP servers.
- [Connect to a Langflow MCP server](https://docs.langflow.org/mcp-client#mcp-http-mode) to use flows from your [Langflow projects](https://docs.langflow.org/concepts-flows#projects) as MCP tools.


### Connect to a non-Langflow MCP server [​](https://docs.langflow.org/mcp-client#mcp-stdio-mode)


As of Langflow 1.9.x, the **MCP Tools** component is not listed as a draggable component under the **Agents** category. To add an MCP tool to a flow, do the following:


1. Register the MCP server. Open **Settings** → **MCP Servers**, and then click **Add MCP Server**, or click **MCP** in the flow editor’s left sidebar, and then click **Add MCP Server**.
2. Configure and save the server. Enter the connection details, and then click **Save**. For more information, see [Use Langflow as an MCP client](https://docs.langflow.org/mcp-client).
3. In the **MCP** sidebar, drag the new server to the canvas. The **MCP Tools** component for that server is added to the canvas.


For more information, see [Use Langflow as an MCP client](https://docs.langflow.org/mcp-client) and [Use Langflow as an MCP server](https://docs.langflow.org/mcp-server).


1. In the **MCP Server** field on the **MCP Tools** component, select the server you registered. New servers are registered in **Settings** > **MCP Servers**, or in the **MCP** sidebar > **Add MCP Server**, using one of the following connection types:
  - **JSON**: Paste the MCP server's JSON configuration object into the field, including required and optional parameters that you want to use, and then click **Add Server**.
  - **STDIO**: Enter the MCP server's **Name**, **Command**, and any **Arguments** and **Environment Variables** the server uses, and then click **Add Server**. For example, to start a [Fetch](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch) server, set **Command** to `uvx` and the first **Argument** to `mcp-server-fetch`.
  - **HTTP/SSE**: Enter your MCP server's **Name**, **URL**, and any **Headers** and **Environment Variables** the server uses, and then click **Add Server**. The default **URL** for Langflow MCP servers is `http://localhost:7860/api/v1/mcp/project/PROJECT_ID/streamable` or `http://localhost:7860/api/v1/mcp/streamable`. For more information, see [Connect to a Langflow MCP server](https://docs.langflow.org/mcp-client#mcp-http-mode).2. To configure headers for your MCP server, enter each header in the **Headers** fields as key-value pairs. You can use [global variables](https://docs.langflow.org/configuration-global-variables) in header values by entering the global variable name as the header value. For more information, see [Use global variables in MCP server headers](https://docs.langflow.org/mcp-client#use-global-variables-in-mcp-server-headers). If this server is nested inside a Langflow flow that runs as an MCP server, you can propagate the incoming request's `x-api-key` or `Authorization` header directly to this server at runtime. For more information, see [Propagate x-api-key to nested MCP servers](https://docs.langflow.org/mcp-client#propagate-x-api-key).
3. To use environment variables in your server command, enter each variable in the **Env** fields as key-value pairs.
4. In the **Tool** field, select a tool that you want this component to use, or leave the field blank to allow access to all tools provided by the MCP server. If you select a specific tool, you might need to configure additional tool-specific fields. For information about tool-specific fields, see your MCP server's documentation. At this point, the **MCP Tools** component is serving a tool from the connected server, but nothing is using the tool. The next steps explain how to make the tool available to an [**Agent** component](https://docs.langflow.org/components-agents) so that the agent can use the tool in its responses.
5. In the [component's header menu](https://docs.langflow.org/concepts-components#component-menus), enable **Tool mode** so you can use the component with an agent.
6. Connect the **MCP Tools** component's **Toolset** port to an **Agent** component's **Tools** port. If not already present in your flow, make sure you also attach **Chat Input** and **Chat Output** components to the **Agent** component. ![MCP Tools component in STDIO mode](https://docs.langflow.org/assets/images/component-mcp-stdio-a13a643e61ceea972c4a3f64dd1ae72f.png)
7. Test your flow to make sure the MCP server is connected and the selected tool is used by the agent. Open the **Playground**, and then enter a prompt that uses the tool you connected through the **MCP Tools** component. For example, if you use `mcp-server-fetch` with the `fetch` tool, you could ask the agent to summarize recent tech news. The agent calls the MCP server function `fetch`, and then returns the response.
8. If you want the agent to be able to use more tools, repeat these steps to add more tools components with different servers or tools.


### Connect a Langflow MCP server [​](https://docs.langflow.org/mcp-client#mcp-http-mode)


Every Langflow project runs a separate MCP server that exposes the project's flows as MCP tools. For more information about your projects' MCP servers, including exposing flows as MCP tools, see [Use Langflow as an MCP server](https://docs.langflow.org/mcp-server).


Langflow MCP servers support both the **streamable HTTP** transport and **Server-Sent Events (SSE)** as a fallback.


To leverage flows-as-tools, register your Langflow MCP endpoint as a server first, and then add the **MCP Tools** component from the **MCP** sidebar.


1. Register the Langflow MCP server. Open **Settings** > **MCP Servers** or the **MCP** section in the flow sidebar, click **Add MCP Server**, and select **HTTP/SSE** mode.
2. In the **MCP URL** field, enter your Langflow server's MCP endpoint. All flows available from the targeted server are treated as tools. For authentication and project URLs, see [Use Langflow as an MCP server](https://docs.langflow.org/mcp-server).
  - For project-specific servers: `http://localhost:7860/api/v1/mcp/project/PROJECT_ID/streamable`
  - For global MCP server: `http://localhost:7860/api/v1/mcp/streamable`
  - Default for Langflow Desktop: `http://localhost:7868/`3. Save the server. When the connection succeeds, the server is stored and appears as a tile in the **MCP** sidebar.
4. Add the **MCP Tools** component to the flow.
5. In the [component's header menu](https://docs.langflow.org/concepts-components#component-menus), enable **Tool Mode** so you can use the component with an agent.
6. Connect the **MCP Tools** component's **Toolset** port to an **Agent** component's **Tools** port.
7. If not already present in your flow, make sure you also attach **Chat Input** and **Chat Output** components to the **Agent** component. ![MCP component with HTTP/SSE mode enabled](https://docs.langflow.org/assets/images/component-mcp-sse-mode-2e742342a52231247733d8486ab612fd.png)
8. Test your flow to make sure the agent uses your flows to respond to queries. Open the **Playground**, and then enter a prompt that uses a flow that you connected through the **MCP Tools** component.
9. If you want the agent to be able to use more tools, repeat these steps to add more tools components with different servers or tools.


## MCP Tools parameters [​](https://docs.langflow.org/mcp-client#mcp-tools-parameters)


| Name | Type | Description |
| --- | --- | --- |
| mcp_server | String | Input parameter. The MCP server to connect to. |
| tool | String | Input parameter. The specific tool to execute from the connected MCP server. Leave blank to allow access to all tools. |
| use_cache | Boolean | Input parameter. Enable caching of MCP server and tools to improve performance. Default: `false`. |
| verify_ssl | Boolean | Input parameter. Enable SSL certificate verification for HTTPS connections. Default: `true`. |
| response | Table | Output parameter. [`Table`](https://docs.langflow.org/data-types#table) containing the response from the executed tool. |


## Manage connected MCP servers [​](https://docs.langflow.org/mcp-client#manage-connected-mcp-servers)


To manage MCP server connections for use in flows, open the **MCP** section in the visual editor, and then click **Manage Servers**, or click your profile icon, select **Settings**, and then click **MCP Servers**.


To add a new MCP server, click **Add MCP Server**, register the server, and then select the server on the **MCP Tools** component as described in [Connect to a non-Langflow MCP server](https://docs.langflow.org/mcp-client#mcp-stdio-mode).


Click **More** to edit or delete an MCP server connection.


If your Langflow server administrator has locked MCP server management, you will receive a locked message when you try to add or modify servers. For more information, see [Lock MCP server management](https://docs.langflow.org/mcp-server#restrict-mcp-server-management).


## Modify MCP server environment variables with the API [​](https://docs.langflow.org/mcp-client#mcp-api-tweaks)


You can modify MCP server environment variables at runtime when running flows through the [Langflow API](https://docs.langflow.org/api-reference-api-examples) by tweaking the **MCP Tools** component.


You can include tweaks with any Langflow API request that supports the `tweaks` parameter, such as POST requests to the `/run` or `/webhook` endpoints. For more information, see [Input schema (tweaks)](https://docs.langflow.org/concepts-publish#input-schema).


To modify the **MCP Tools** component's environment variables with tweaks, do the following:


1. Open the flow that contains your **MCP Tools** component.
2. To find the **MCP Tools** component's unique ID, in your **MCP Tools** component, click **Controls**. The component's ID is displayed in the **Controls** pane, such as `MCPTools-Bzahc`.
3. Send a POST request to the Langflow server's `/run` endpoint, and include tweaks to the **MCP Tools** component. The following examples demonstrate a request structure with the `env` object nested under `mcp_server` in the `tweaks` payload: - Python - TypeScript - cURL ```python import requests import os LANGFLOW_SERVER_ADDRESS = "http://localhost:7860" FLOW_ID = "your-flow-id" LANGFLOW_API_KEY = os.getenv("LANGFLOW_API_KEY") MCP_TOOLS_COMPONENT_ID = "MCPTools-Bzahc" url = f"{LANGFLOW_SERVER_ADDRESS}/api/v1/run/{FLOW_ID}?stream=false" headers = { "Content-Type": "application/json", "x-api-key": LANGFLOW_API_KEY } payload = { "output_type": "chat", "input_type": "chat", "input_value": "What sales data is available to me?", "tweaks": { MCP_TOOLS_COMPONENT_ID: { "mcp_server": { "env": { "API_URL": "https://api.example.com", "API_KEY": "your-mcp-server-api-key", "ENVIRONMENT": "production" } } } } } response = requests.post(url, json=payload, headers=headers) print(response.json()) ``` ```ts const LANGFLOW_SERVER_ADDRESS = "http://localhost:7860"; const FLOW_ID = "your-flow-id"; const LANGFLOW_API_KEY = process.env.LANGFLOW_API_KEY || ""; const MCP_TOOLS_COMPONENT_ID = "MCPTools-Bzahc"; const url = `${LANGFLOW_SERVER_ADDRESS}/api/v1/run/${FLOW_ID}?stream=false`; const response = await fetch(url, { method: "POST", headers: { "Content-Type": "application/json", "x-api-key": LANGFLOW_API_KEY, }, body: JSON.stringify({ output_type: "chat", input_type: "chat", input_value: "What sales data is available to me?", tweaks: { [MCP_TOOLS_COMPONENT_ID]: { mcp_server: { env: { API_URL: "https://api.example.com", API_KEY: "your-mcp-server-api-key", ENVIRONMENT: "production", }, }, }, }, }), }); const data = await response.json(); console.log(data); ``` ```bash curl --request POST \ --url "http://LANGFLOW_SERVER_ADDRESS/api/v1/run/FLOW_ID?stream=false" \ --header "Content-Type: application/json" \ --header "x-api-key: LANGFLOW_API_KEY" \ --data '{ "output_type": "chat", "input_type": "chat", "input_value": "What sales data is available to me?", "tweaks": { "MCP_TOOLS_COMPONENT_ID": { "mcp_server": { "env": { "API_URL": "https://api.example.com", "API_KEY": "your-mcp-server-api-key", "ENVIRONMENT": "production" } } } } }' ``` Replace `MCP_TOOLS_COMPONENT_ID`, `LANGFLOW_API_KEY`, `LANGFLOW_SERVER_ADDRESS`, and `FLOW_ID` with the actual values from your Langflow deployment. Langflow doesn't automatically discover or expose which environment variables your MCP server accepts from the **MCP Tools** component. To determine which environment variables your MCP server accepts, see the MCP server's documentation. For example, the [Astra DB MCP server](https://github.com/datastax/astra-db-mcp) requires `ASTRA_DB_APPLICATION_TOKEN` and `ASTRA_DB_API_ENDPOINT`, with an optional variable for `ASTRA_DB_KEYSPACE`, as documented in its repository.


## Use global variables in MCP server headers [​](https://docs.langflow.org/mcp-client#use-global-variables-in-mcp-server-headers)


You can use [global variables](https://docs.langflow.org/configuration-global-variables) in MCP server header values to securely store and reference API keys, authentication tokens, and other sensitive values. This is particularly useful for deployment scenarios where you need to pass user-specific credentials at runtime.


Enter a global variable name as the header value, and Langflow resolves the global variable name to its actual value before making the MCP server request. Langflow only passes the token value to your server; it doesn't validate tokens on behalf of your MCP server.


For example, to create a global variable named `TEST_BEARER_TOKEN` for MCP server bearer authentication, do the following:


1. To open the **Global Variables** pane, click your profile icon, select **Settings**, and then click **Global Variables**.
2. Create a **Credential** global variable named `TEST_BEARER_TOKEN`.
3. In the **Value** field, enter your MCP server's bearer token value. The value must include the `Bearer` prefix with a space, for example: `Bearer eyJhbG...`.
4. Click **Save Variable**.
5. To manage MCP server connections for your Langflow client, click **MCP servers**, and then click **Manage Servers**, or click your profile icon, select **Settings**, and then click **MCP Servers**.
6. Click **Add MCP Server**.
7. Select the following:
  - **Name**: test-mcp-server
  - **Streamable HTTP/SSE URL**: Your MCP server's URL, such as `http://127.0.0.1:8000/mcp`.
  - **Headers**: In the key field, enter the literal string `Authorization`. For the key's value, enter `TEST_BEARER_TOKEN`, or the exact name of your global variable.8. Click **Create Server**. If the connection succeeds, Langflow shows the number of tools exposed by the server. After creating the server and global variable, you can connect to the server with the **MCP Tools** component, as explained in the next steps.
9. Add the **MCP Tools** component to a flow.
10. In the **MCP Tools** component, confirm the **MCP Server** is set to the server you created. The MCP server configuration already includes the headers you configured earlier, so no further configuration is needed in the component. The global variable `TEST_BEARER_TOKEN` is automatically resolved when the component makes requests to the MCP server.
11. Optional: To override headers or add additional headers to the **MCP Tools** component, click the component to view the **Headers** parameter in the [component inspection panel](https://docs.langflow.org/concepts-components#component-menus), and then add header key values. Headers configured in the component take precedence over the headers configured in the MCP server settings.
12. Test your flow to make sure the agent uses your server to respond to queries. Open the **Playground**, and then enter a prompt that uses a tool that you connected through the **MCP Tools** component. Langflow automatically resolves `TEST_BEARER_TOKEN` to its actual value before sending the request to the MCP server. When your MCP server receives the request, the `Authorization` header contains the resolved token value.


## Propagate `x-api-key` to nested MCP servers [​](https://docs.langflow.org/mcp-client#propagate-x-api-key)


When Langflow runs as an MCP server and a flow contains an [**MCP Tools** component](https://docs.langflow.org/mcp-tools) that calls an external server, you can forward the outer client's `x-api-key` or `Authorization` header at runtime.


In the nested server's **Headers** config, set the key and value to the same header name, such as `x-api-key` and `x-api-key`. Langflow reads the matching header from the incoming request and substitutes it before calling the nested server.


If the incoming request does not include the configured header, the literal string is passed through unchanged.


## See also [​](https://docs.langflow.org/mcp-client#see-also)


- [Langflow MCP Client](https://docs.langflow.org/langflow-mcp-client)
- [Use Langflow as an MCP server](https://docs.langflow.org/mcp-server)
- [Use a DataStax Astra DB MCP server with the MCP Tools component](https://docs.langflow.org/mcp-component-astra)


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)

- [Use the MCP tools component](https://docs.langflow.org/mcp-client#use-the-mcp-tools-component)
  - [Connect to a non-Langflow MCP server](https://docs.langflow.org/mcp-client#mcp-stdio-mode)
  - [Connect a Langflow MCP server](https://docs.langflow.org/mcp-client#mcp-http-mode)- [MCP Tools parameters](https://docs.langflow.org/mcp-client#mcp-tools-parameters)
- [Manage connected MCP servers](https://docs.langflow.org/mcp-client#manage-connected-mcp-servers)
- [Modify MCP server environment variables with the API](https://docs.langflow.org/mcp-client#mcp-api-tweaks)
- [Use global variables in MCP server headers](https://docs.langflow.org/mcp-client#use-global-variables-in-mcp-server-headers)
- [Propagate `x-api-key` to nested MCP servers](https://docs.langflow.org/mcp-client#propagate-x-api-key)
- [See also](https://docs.langflow.org/mcp-client#see-also)[Manage Privacy Choices](https://docs.langflow.org/mcp-client#)

---

# Contribute to Langflow | Langflow Documentation

`https://docs.langflow.org/contributing-how-to-contribute`

# Contribute to Langflow

To contribute code or documentation to Langflow, follow the pull request guide.

Copy page ⌥C Version: 1.12.x On this page
## Langflow services overview​
## Install Langflow from source​
*For more information, see the VSCode documentation.*

## Contribute documentation​
## Open a pull request​





This guide is intended to help you start contributing to Langflow. As an open-source codebase in a rapidly developing field, Langflow welcomes contributions, whether it be in the form of a new feature, improved infrastructure, or better documentation.


To contribute code or documentation to Langflow, follow the [pull request guide](https://docs.langflow.org/contributing-how-to-contribute#open-a-pull-request).


## Langflow services overview [​](https://docs.langflow.org/contributing-how-to-contribute#langflow-services-overview)


This overview will help you understand how to set up your development environment.


Langflow consists of two main services:


- Frontend: A React/TypeScript application that provides the user interface.
- Backend: A Python/FastAPI service that handles API requests.


During development, the frontend and backend services run separately on different ports:


- Frontend development server: `http://localhost:3000` (with hot reload).
- Backend API server: `http://localhost:7860`.


When you install Langflow as an end user, the backend serves the frontend internally, making both services available on a single port (`7860` by default).


## Install Langflow from source [​](https://docs.langflow.org/contributing-how-to-contribute#install-langflow-from-source)


Install Langflow from source by forking the repository and setting up your development environment.


### Prerequisites [​](https://docs.langflow.org/contributing-how-to-contribute#prerequisites)


- [Python](https://www.python.org/downloads/) 3.10 to 3.14
- [uv](https://docs.astral.sh/uv/getting-started/installation/) version 0.4 or later
- [Node.js](https://nodejs.org/en/download/package-manager)
- [Make](https://www.gnu.org/software/make/#documentation) (Linux and macOS only)


### Clone the Langflow repository [​](https://docs.langflow.org/contributing-how-to-contribute#clone-the-langflow-repository)


1. Fork the [Langflow GitHub repository](https://github.com/langflow-ai/langflow).
2. Add the new remote to your local repository on your local machine:


```bash
git remote add FORK_NAME https://github.com/GIT_USERNAME/langflow.git
```


Replace the following:


- `FORK_NAME`: A name for your fork of the repository
- `GIT_USERNAME`: Your Git username


### Run Langflow from source [​](https://docs.langflow.org/contributing-how-to-contribute#run-langflow-from-source)


You can run Langflow from source after cloning the repository, even if you aren't contributing to the codebase. This builds the frontend and serves it through the backend on port `7860`.


The instructions below are for running Langflow from source. For development with hot reload, see [Set up development environment](https://docs.langflow.org/contributing-how-to-contribute#set-up-your-langflow-development-environment).


### Set up your Langflow development environment [​](https://docs.langflow.org/contributing-how-to-contribute#set-up-your-langflow-development-environment)


This section is for contributors who want to develop and test code changes with hot reload enabled.


If you just want to run Langflow locally without making code changes, see [Run Langflow from source](https://docs.langflow.org/contributing-how-to-contribute#run-langflow-from-source).


- Linux or macOS
- Windows


1. Set up the Langflow development environment: ```bash make init ``` This command sets up the development environment by doing the following:
  - Checking for uv and npm.
  - Installing backend and frontend dependencies.
  - Installing pre-commit hooks.2. Run the backend and frontend in separate terminals for development: ```bash # Run backend in development mode (includes hot reload) make backend ``` ```bash # In another terminal, run frontend in development mode (includes hot reload) make frontend ``` The `make backend` and `make frontend` commands automatically install dependencies, so you don't need to run install commands separately. The frontend is served at `http://localhost:3000` and the backend at `http://localhost:7860`.
3. Optional: Install pre-commit hooks to help keep your changes clean and well-formatted. With pre-commit hooks installed, you must use `uv run git commit` instead of `git commit` directly. `make init` installs pre-commit hooks automatically, or you can run the following command to install them manually: ```bash uv sync uv run pre-commit install ```
4. To test your changes before pushing commits, run `make lint`, `make format`, and `make unit_tests`. To run all tests, including coverage, unit, and integration, tests, run `make tests`.


Since Windows doesn't include `make`, building and running Langflow from source uses `npm` and `uv`.


To set up the Langflow development environment, run the frontend and backend in separate terminals:


1. To run the frontend development server with hot reload, run the following commands: ```bash cd src/frontend npm install npm run start ```
2. In a separate terminal, run the following command to run the backend: ```bash uv run langflow run --backend-only ```


The frontend is served at `http://localhost:3000` and the backend at `http://localhost:7860`. This setup preserves hot reload for frontend development, with no need to copy build files after every edit.


### Troubleshoot frontend build issues [​](https://docs.langflow.org/contributing-how-to-contribute#troubleshoot-frontend-build-issues)


If you encounter frontend build problems or are upgrading from an older version of Langflow, run `make run_clic` once.


```bash
make run_clic
```


This command cleans the build cache and rebuilds everything from scratch, which resolves most frontend-related issues when switching between versions.


### Debug [​](https://docs.langflow.org/contributing-how-to-contribute#debug)


The repo includes a `.vscode/launch.json` file for debugging the backend in VSCode, which is faster than debugging with Docker Compose.


For more information, see the [VSCode documentation](https://code.visualstudio.com/docs/debugtest/debugging#_start-a-debugging-session).


### Additional contribution guides [​](https://docs.langflow.org/contributing-how-to-contribute#additional-contribution-guides)


- [Contribute bundles](https://docs.langflow.org/contributing-bundles)
- [Contribute components](https://docs.langflow.org/contributing-components)
- [Contribute tests](https://docs.langflow.org/contributing-component-tests)
- [Contribute templates](https://docs.langflow.org/contributing-templates)


## Contribute documentation [​](https://docs.langflow.org/contributing-how-to-contribute#contribute-documentation)


The documentation is built using [Docusaurus](https://docusaurus.io/) and written in [Markdown](https://docusaurus.io/docs/markdown-features). For style guidance, see the [Google Developer Documentation Style Guide](https://developers.google.com/style).


1. Install [Node.js](https://nodejs.org/en/download/package-manager).
2. Fork the [Langflow GitHub repository](https://github.com/langflow-ai/langflow).
3. Add the new remote to your local repository on your local machine: ```bash git remote add FORK_NAME https://github.com/GIT_USERNAME/langflow.git ``` Replace the following:
  - `FORK_NAME`: A name for your fork of the repository
  - `GIT_USERNAME`: Your Git username4. From the root of your local Langflow fork, change to the `/docs` directory: ```bash cd docs ``` If you're using a dev container, run the documentation build from outside the container on your host terminal, not from within the dev container workspace. The documentation build may not work properly when run inside the dev container.
5. Install dependencies and start a local Docusaurus static site with hot reload: ```bash npm install npm run start ``` The documentation is served at `http://localhost:3000`.
6. To edit and create content, work with the `.mdx` files in the `langflow/docs/docs` directory. Create new files in `.mdx` format. Navigation is defined in `langflow/docs/sidebars.js`. Most pages use a `slug` for shorthand cross-referencing, rather than supplying the full or relative directory path. For example, if a page has a `slug` of `/cool-page`, you can link to it with `[Cool page](/cool-page)` from any other `/docs` page.
7. Recommended: After making some changes, run `npm run build` to build the site locally with more robust logging. This can help you find broken links before creating a PR.


## Open a pull request [​](https://docs.langflow.org/contributing-how-to-contribute#open-a-pull-request)


To submit a pull request, do the following:


1. Open a GitHub pull request against the active `release-X.Y.Z` release candidate branch. Do not target `main`. For example, if the latest released version is `1.8.0`, your pull request should target the `release-1.9.0` branch. Include a clear title and description.
2. Ensure the PR title follows semantic commit conventions. For example, features are `feat: add new feature` and fixes are `fix: correct issue with X`.


Some additional guidance on pull request titles:


- Ensure the pull request description clearly describes the problem and solution. If the PR fixes an issue, include a link to the fixed issue in the PR description with `Fixes #1234`.
- Pull request titles appear in Langflow's release notes, so they should explain what the PR does as explicitly as possible.
- Pull requests should strive to fix one thing **only**, and should contain a good description of what is being fixed.


1. A Langflow maintainer will review your pull request and may request changes, so ensure you pay attention to your PRs. Thanks for your contribution!


For more information, see the [Python Developer's Guide](https://devguide.python.org/getting-started/pull-request-lifecycle/index.html#making-good-commits).


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)

- [Langflow services overview](https://docs.langflow.org/contributing-how-to-contribute#langflow-services-overview)
- [Install Langflow from source](https://docs.langflow.org/contributing-how-to-contribute#install-langflow-from-source)
  - [Prerequisites](https://docs.langflow.org/contributing-how-to-contribute#prerequisites)
  - [Clone the Langflow repository](https://docs.langflow.org/contributing-how-to-contribute#clone-the-langflow-repository)
  - [Run Langflow from source](https://docs.langflow.org/contributing-how-to-contribute#run-langflow-from-source)
  - [Set up your Langflow development environment](https://docs.langflow.org/contributing-how-to-contribute#set-up-your-langflow-development-environment)
  - [Troubleshoot frontend build issues](https://docs.langflow.org/contributing-how-to-contribute#troubleshoot-frontend-build-issues)
  - [Debug](https://docs.langflow.org/contributing-how-to-contribute#debug)
  - [Additional contribution guides](https://docs.langflow.org/contributing-how-to-contribute#additional-contribution-guides)- [Contribute documentation](https://docs.langflow.org/contributing-how-to-contribute#contribute-documentation)
- [Open a pull request](https://docs.langflow.org/contributing-how-to-contribute#open-a-pull-request)[Manage Privacy Choices](https://docs.langflow.org/contributing-how-to-contribute#)

---

# Use Langflow as an MCP server | Langflow Documentation

`https://docs.langflow.org/mcp-server`

# Use Langflow as an MCP server
## Prerequisites​
## Serve flows as MCP tools​
## Connect clients to your Langflow MCP server​
## MCP server authentication​
## Deploy your Langflow MCP server externally​
## Use MCP Inspector to test and debug flows​
## Disable the legacy MCP SSE transport​
## Restrict MCP server management to superusers​
## MCP server environment variables​
## Troubleshoot Langflow MCP servers​
## See also​












Langflow integrates with the Model Context Protocol (MCP) as both an MCP server and an MCP client.

Copy page ⌥C Version: 1.12.x On this page

Langflow integrates with the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) as both an MCP server and an MCP client.


This page describes how to use Langflow as an MCP server that exposes your flows as [tools](https://modelcontextprotocol.io/docs/concepts/tools) that [MCP clients](https://modelcontextprotocol.io/clients) can use when generating responses.


Langflow MCP servers support both the **streamable HTTP** transport and **Server-Sent Events (SSE)** as a fallback. The default project MCP server configuration uses streamable HTTP transport at the URL path `/streamable`. To serve only streamable HTTP, see [Disable the legacy MCP SSE transport](https://docs.langflow.org/mcp-server#disable-legacy-sse).


For information about using Langflow as an MCP client and managing MCP server connections within flows, see [Use Langflow as an MCP client](https://docs.langflow.org/mcp-client).


## Prerequisites [​](https://docs.langflow.org/mcp-server#prerequisites)


- A [Langflow project](https://docs.langflow.org/concepts-flows#projects) with at least one flow that has a [**Chat Output** component](https://docs.langflow.org/chat-input-and-output). The **Chat Output** component is required to use a flow as an MCP tool.
- Any LTS version of [Node.js](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) installed on your computer if you want to use MCP Inspector to [test and debug flows](https://docs.langflow.org/mcp-server#test-and-debug-flows).
- [ngrok installed](https://ngrok.com/docs/getting-started/#1-install-ngrok) and an [ngrok authtoken](https://dashboard.ngrok.com/get-started/your-authtoken) if you want to [deploy a public Langflow server](https://docs.langflow.org/deployment-public-server).


## Serve flows as MCP tools [​](https://docs.langflow.org/mcp-server#select-flows-to-serve)


When you create a [Langflow project](https://docs.langflow.org/concepts-flows#projects), Langflow automatically adds the project to your MCP server's configuration and makes the project's flows available as MCP tools.


If your Langflow server has authentication enabled (`AUTO_LOGIN=false`), the project's MCP server is automatically configured with API key authentication, and a new API key is generated specifically for accessing the new project's flows. For more information, see [MCP server authentication](https://docs.langflow.org/mcp-server#authentication).


### Prevent automatic MCP server configuration for Langflow projects [​](https://docs.langflow.org/mcp-server#prevent-automatic-mcp-server-configuration-for-langflow-projects)


To disable automatic MCP server configuration for new projects, set the `LANGFLOW_ADD_PROJECTS_TO_MCP_SERVERS` environment variable to `false`. For more information, see [MCP server environment variables](https://docs.langflow.org/mcp-server#mcp-server-environment-variables).


### Selectively enable and disable MCP servers for Langflow projects [​](https://docs.langflow.org/mcp-server#selectively-enable-and-disable-mcp-servers-for-langflow-projects)


With or without automatic MCP server configuration enabled, you can selectively enable and disable the projects that are exposed as MCP tools:


1. Click the **MCP Server** tab on the [**Projects** page](https://docs.langflow.org/concepts-flows#projects), or, when editing a flow, click **Share**, and then select **MCP Server**. ![MCP server projects page](https://docs.langflow.org/assets/images/mcp-server-53850e4ac7599dec00dd7d01922ba79f.png) The **Flows/Tools** section lists the flows that are currently being served as tools on this MCP server.
2. To toggle exposed flows, click **Edit Tools**, and then select the flows that you want exposed as tools. To prevent a flow from being used as a tool, clear the checkbox in the first column.
3. Close the **MCP Server Tools** dialog to save your changes. ![MCP Server Tools](https://docs.langflow.org/assets/images/mcp-server-tools-ddc0f1dc04109b9f3daf6a2f380073c4.png)


### Edit flow tool names and descriptions [​](https://docs.langflow.org/mcp-server#edit-flow-tool-names-and-descriptions)


Tool names and descriptions help MCP clients determine which actions your flows provide and when to use those actions. It is recommended to provide clear, descriptive names and descriptions for all tools that you serve to MCP clients.


To edit the names and descriptions of flow tools on a Langflow MCP server, do the following:


1. Click the **MCP Server** tab on the [**Projects** page](https://docs.langflow.org/concepts-flows#projects), or, when editing a flow, click **Share**, and then select **MCP Server**.
2. Click **Edit Tools**.
3. Click the **Description** or **Tool** that you want to edit:
  - **Tool name**: Enter a name that makes it clear what the flow does when used as a tool by an agent.
  - **Tool description**: Enter a description that completely and accurately describes the specific actions the flow performs.4. Close the **MCP Server Tools** dialog to save your changes.


#### Importance of tool names and descriptions [​](https://docs.langflow.org/mcp-server#importance-of-tool-names-and-descriptions)


MCP clients use tool names and descriptions to determine which actions to use when generating responses.


Because MCP clients treat your Langflow project as a single MCP server with all of your enabled flows listed as tools, unclear names and descriptions can cause the agent to select tools incorrectly or inconsistently.


For example, a flow's default tool name is the flow ID, such as `adbbf8c7-0a34-493b-90ea-5e8b42f78b66`. This provides no information to an agent about the type of flow or its purpose.


To provide more context about your flows, make sure to name and describe your flows clearly when configuring your Langflow project's MCP server.


Think of these names and descriptions as function names and code comments. Use clear statements to describe the problems your flows solve.


### Configure tool execution timeouts [​](https://docs.langflow.org/mcp-server#configure-tool-execution-timeouts)


There are three ways to set tool execution timeouts: the MCP Tools component timeout setting, a global environment variable, and Langflow's default fallback. How you configure these determines their effect in resolving the actual timeout limit for each tool call.


Langflow times are evaluated in the following order:


1. Per-component timeout is set directly on an MCP Tools component in your flow. To configure per-component timeout in the [**MCP Tools** component](https://docs.langflow.org/mcp-tools), open the advanced settings tab and enter a value in the **Tool Execution Timeout (seconds)** field. A value of `0` disables the per-component override and falls back to the global setting.
2. Global timeout is set with the `LANGFLOW_MCP_TOOL_EXECUTION_TIMEOUT` environment variable. The default is 180 seconds.
3. If neither `LANGFLOW_MCP_TOOL_EXECUTION_TIMEOUT` or `LANGFLOW_MCP_SERVER_TIMEOUT` is configured, Langflow defaults to 180 seconds.


To support tool calls that take longer than 180 seconds, set `LANGFLOW_MCP_TOOL_EXECUTION_TIMEOUT` to a value greater than `180` to raise the global limit, or set the **Tool Execution Timeout (seconds)** field on a specific MCP Tools component to a value greater than `180` to raise the limit for that component only.


If `LANGFLOW_MCP_SERVER_TIMEOUT` is set to a value greater than `LANGFLOW_MCP_TOOL_EXECUTION_TIMEOUT`, the server timeout takes precedence and becomes the actual limit for tool calls.


## Connect clients to your Langflow MCP server [​](https://docs.langflow.org/mcp-server#connect-clients-to-use-the-servers-actions)


Langflow provides automatic installation and code snippets to help you deploy your Langflow MCP servers to your local MCP clients.


- JSON
- Auto install


The JSON option allows you to connect a Langflow MCP server to any local or remote MCP client. You can modify this process for any [MCP-compatible client](https://modelcontextprotocol.io/clients).


1. Install any [MCP-compatible client](https://modelcontextprotocol.io/clients). These steps use Cursor as an example, but the process is generally the same for all clients, with slight differences in client-specific details like file names.
2. In your client, add a new MCP server using the client's UI or configuration file. For example, in Cursor, go to **Cursor Settings**, select **MCP**, and then click **Add New Global MCP Server** to open Cursor's global `mcp.json` configuration file.
3. Recommended: Configure [authentication](https://docs.langflow.org/mcp-server#authentication) for your MCP server.
4. In Langflow, on the **Projects** page, click the **MCP Server** tab.
5. Click the **JSON** tab, copy the code snippet for your operating system, and then paste it into your client's MCP configuration file. For example: ```json { "mcpServers": { "PROJECT_NAME": { "command": "uvx", "args": [ "mcp-proxy", "--transport", "streamablehttp", "http://LANGFLOW_SERVER_ADDRESS/api/v1/mcp/project/PROJECT_ID/streamable" ] } } } ``` The **MCP Server** tab automatically populates the `LANGFLOW_SERVER_ADDRESS` and `PROJECT_ID` values. The default Langflow server address is `http://localhost:7860`. If you are using a [public Langflow server](https://docs.langflow.org/deployment-public-server), the server address is automatically included. If your Langflow server requires authentication, you must include your Langflow API key or OAuth settings in the configuration. For more information, see [MCP server authentication](https://docs.langflow.org/mcp-server#authentication).
6. To include other environment variables with your MCP server command, add an `env` object with key-value pairs of environment variables. For example: ```json { "mcpServers": { "PROJECT_NAME": { "command": "uvx", "args": [ "mcp-proxy", "--transport", "streamablehttp", "http://LANGFLOW_SERVER_ADDRESS/api/v1/mcp/project/PROJECT_ID/streamable" ], "env": { "KEY": "VALUE" } } } } ``` Don't add API keys in the `env` object, as these variables are specifically for the `mcp-proxy` process. Instead, add API keys under `args`. For an example, see [MCP server authentication](https://docs.langflow.org/mcp-server#authentication).
7. Save and close your client's MCP configuration file.
8. Confirm that your Langflow MCP server is on the client's list of MCP servers. If necessary, restart your client to apply the modified configuration file.


1. Install [Cursor](https://docs.cursor.com/get-started/installation), [Claude](https://claude.ai/download), or [Windsurf](https://windsurf.com/download/editor) on the same computer where your Langflow server is running.
2. Recommended: Configure [authentication](https://docs.langflow.org/mcp-server#authentication) for your MCP server.
3. In Langflow, on the **Projects** page, click the **MCP Server** tab.
4. On the **Auto install** tab, find your MCP client provider, and then click **Add**. Your Langflow project's MCP server is automatically added to the configuration file for your local Cursor, Claude, or Windsurf client. For example, with Cursor, the server configuration is added to the `mcp.json` configuration file. Langflow attempts to add this configuration even if the selected client isn't installed. To verify the installation, check the available MCP servers in your client.


Once your MCP client is connected to your Langflow project's MCP server, your flows are registered as tools. Cursor determines when to use tools based on your queries, and requests permissions when necessary. For more information, see the MCP documentation for your client, such as [Cursor's MCP documentation](https://docs.cursor.com/context/model-context-protocol).


## MCP server authentication [​](https://docs.langflow.org/mcp-server#authentication)


Each [Langflow project](https://docs.langflow.org/concepts-flows#projects) has its own MCP server with its own MCP server authentication settings.


When you create a new project, Langflow automatically configures authentication for the project's MCP server based on your Langflow server's authentication settings. If authentication is enabled (`AUTO_LOGIN=false`), the project is automatically configured with API key authentication, and a new API key is generated for accessing the project's flows.


To configure authentication for a Langflow MCP server, go to the **Projects** page in Langflow, click the **MCP Server** tab, click **Edit Auth**, and then select your preferred authentication method:


- API key
- OAuth
- None


When authenticating your MCP server with a Langflow API key, your project's MCP server **JSON** code snippets and **Auto install** configuration automatically include the `--headers` and `x-api-key` arguments in the **args** array (for streamable transport).


Click **Generate API key** to automatically insert a new Langflow API key into the code template. Alternatively, you can replace `YOUR_API_KEY` with an existing Langflow API key.


To add your API key to the configuration, use three separate entries in `args`: `"--headers"`, `"x-api-key"`, and your key value. For example:


```json
{
  "mcpServers": {
    "PROJECT_NAME": {
      "command": "uvx",
      "args": [
        "mcp-proxy",
        "--transport",
        "streamablehttp",
        "--headers",
        "x-api-key",
        "YOUR_API_KEY",
        "http://LANGFLOW_SERVER_ADDRESS/api/v1/mcp/project/PROJECT_ID/streamable"
      ]
    }
  }
}
```


When OAuth is enabled, Langflow automatically starts an [MCP Composer](https://pypi.org/project/mcp-composer) instance for your project, creating a secure client-side proxy between MCP clients and the `mcp-proxy` on your server.


OAuth integration allows your Langflow MCP server to authenticate users and applications through any OAuth 2.0 compliant service. When users or applications connect to your MCP server, they are redirected to your chosen OAuth provider to authenticate. Upon successful authentication, they are granted access to your flows as MCP tools.


Before configuring OAuth in Langflow, you must first set up an OAuth application with an external OAuth 2.0 service provider. You must register your Langflow server as an OAuth client, and then obtain the required values to complete the configuration in Langflow.


The following table describes the required values. [GitHub OAuth](https://github.com/settings/developers) is used for example purposes. Be sure to use the actual values from your own deployment. For more information, see your OAuth provider's documentation.


| Field | Description | Source | Example |
| --- | --- | --- | --- |
| **Host** | OAuth server host | MCP Composer default. | `localhost` |
| **Port** | OAuth server port | MCP Composer default. | `9000` |
| **Server URL** | Full OAuth server URL | Combines the MCP Composer default OAuth host and port. | `http://localhost:9000` |
| **Callback URL** | OAuth callback URL on your server | You define this full URL during OAuth app registration. This must match exactly what you register with your OAuth provider. | `http://localhost:9000/auth/idaas/callback` |
| **Client ID** | Your OAuth client identifier | From your OAuth provider. | `Ov23li9vx2grVL61qjb` |
| **Client Secret** | Your OAuth client secret | From your OAuth provider. | `1234567890abcdef1234567890abcdef12345678` |
| **Authorization URL** | OAuth authorization endpoint | From your OAuth provider. | `https://github.com/login/oauth/authorize` |
| **Token URL** | OAuth token endpoint for getting refresh tokens | From your OAuth provider. | `https://github.com/login/oauth/access_​token` |
| **MCP Scope** | Scope for MCP operations | You define this. As of Langflow 1.6, `user` is the only available value. | `user` |
| **Provider Scope** | OAuth provider scope | You define this. As of Langflow 1.6, `openid` is the only available value. | `openid` |


To configure OAuth authentication:


1. Select **OAuth** as the authentication type.
2. Configure the OAuth settings with the values from your OAuth deployment. All values are required. The OAuth credentials are encrypted and stored securely in your Langflow database.
3. Click **Save**. Your MCP server's **JSON** code snippets and **Auto install** configuration are automatically updated with OAuth values. These are automatically used for new installations after enabling OAuth. However, you must manually update any existing installations, as explained in the next step.
4. If you already installed your Langflow MCP server in your MCP client, you must update your MCP client configuration to use the new OAuth settings after enabling OAuth on your MCP server. The client update method depends on how you installed the server on the client:
  - **Auto install**: Manually update your client's config file using the updated JSON snippet from the **JSON** tab, or repeat the steps in [Auto-install](https://docs.langflow.org/mcp-server#connect-clients-to-use-the-servers-actions) to re-install the client with the updated settings.
  - **JSON option**: Copy the updated JSON snippet from the **JSON** tab and replace your existing configuration.
  - **New connections**: Use either the **Auto install** or **JSON** option. The OAuth settings are included automatically.


After you enable OAuth and update your client configuration, an OAuth callback window opens each time your MCP client attempts to authenticate with the server. A successful authentication returns `Authentication complete. You may close this window.` If your client doesn't open the OAuth window, try restarting the client to retrieve the updated configuration.


When no authentication is configured, your MCP server becomes a public endpoint that anyone can access without providing credentials. Only use this option when Langflow is running in a trusted environment.


## Deploy your Langflow MCP server externally [​](https://docs.langflow.org/mcp-server#deploy-your-server-externally)


To deploy your Langflow MCP server externally, see [Deploy a public Langflow server](https://docs.langflow.org/deployment-public-server).


## Use MCP Inspector to test and debug flows [​](https://docs.langflow.org/mcp-server#test-and-debug-flows)


[MCP Inspector](https://modelcontextprotocol.io/docs/tools/inspector) is a common tool for testing and debugging MCP servers. You can use MCP Inspector to monitor your flows and get insights into how they are being consumed by the MCP server.


1. Install MCP Inspector: ```bash npx @modelcontextprotocol/inspector ``` For more information about configuring MCP Inspector, including specifying a proxy port, see the [MCP Inspector GitHub project](https://github.com/modelcontextprotocol/inspector).
2. Open a web browser and navigate to the MCP Inspector UI. The default address is `http://localhost:6274`.
3. In the MCP Inspector UI, enter the connection details for your Langflow project's MCP server. The field values depend on your server's method of [authentication](https://docs.langflow.org/mcp-server#authentication). - API key - OAuth - None - **Transport Type**: Select **STDIO**. - **Command**: `uvx` - **Arguments**: Enter the following list of arguments, separated by spaces. Replace the values for `YOUR_API_KEY`, `LANGFLOW_SERVER_ADDRESS`, and `PROJECT_ID` with the values from your Langflow MCP server. For example: ```bash mcp-proxy --headers x-api-key YOUR_API_KEY http://LANGFLOW_SERVER_ADDRESS/api/v1/mcp/project/PROJECT_ID/streamable ``` - **Transport Type**: Select **STDIO**. - **Command**: `uvx` - **Arguments**: Enter the following list of arguments, separated by spaces. Replace the value for `OAUTH_SERVER_URL` with the URL of your OAuth server. For example: ```bash mcp-composer --mode stdio --sse-url http://localhost:9000/sse --disable-composer-tools --client_auth_type oauth ``` - **Transport Type**: Select **SSE**. - **URL**: Enter the Langflow MCP server's endpoint. For example: ```bash http://localhost:7860/api/v1/mcp/project/d359cbd4-6fa2-4002-9d53-fa05c645319c/streamable ```
4. Click **Connect**. If the connection was successful, you should see your project's flows in the **Tools** tab. From this tab, you can monitor how your flows are being registered as tools by MCP, as well as test the tools with custom input values.
5. To quit MCP Inspector, press Control+C in the same terminal window where you started it.


## Disable the legacy MCP SSE transport [​](https://docs.langflow.org/mcp-server#disable-legacy-sse)


Set `LANGFLOW_MCP_SSE_ENABLED=false` to return `404` from the legacy SSE transport and its message endpoint. Streamable HTTP is unaffected.


## Restrict MCP server management to superusers [​](https://docs.langflow.org/mcp-server#restrict-mcp-server-management)


To prevent non-superusers from editing MCP server connections, set `LANGFLOW_MCP_SERVERS_LOCKED=true`.


When set to `true`, non-superusers can use existing MCP servers that are already configured, but they cannot configure MCP server connections in the UI or API. Superusers retain full access to MCP server configuration.


Locking the MCP server configuration for users does not disable Langflow's built-in MCP server for serving flows as MCP tools.


## MCP server environment variables [​](https://docs.langflow.org/mcp-server#mcp-server-environment-variables)


The following environment variables set behaviors related to your Langflow projects' MCP servers:


| Variable | Format | Default | Description |
| --- | --- | --- | --- |
| `LANGFLOW_​MCP_​SERVER_​ENABLED` | Boolean | `True` | Whether to initialize an MCP server for each of your Langflow projects. If `false`, Langflow doesn't initialize MCP servers. |
| `LANGFLOW_​MCP_​SSE_​ENABLED` | Boolean | `True` | Whether to serve the legacy SSE transport. If `false`, SSE and its message endpoint return `404`. Streamable HTTP is unaffected. See [Disable the legacy MCP SSE transport](https://docs.langflow.org/mcp-server#disable-legacy-sse). |
| `LANGFLOW_​MCP_​SERVER_​ENABLE_​PROGRESS_​NOTIFICATIONS` | Boolean | `False` | If `true`, Langflow MCP servers send progress notifications. |
| `LANGFLOW_​SKIP_​MCP_​AUTO_​INIT` | Boolean | `False` | If `true`, skip background MCP server auto-initialization on startup. Use this on offline, firewalled, or CI hosts so startup does not wait on outbound MCP connections. |
| `LANGFLOW_​MCP_​COMPOSER_​ENABLED` | Boolean | `True` | Whether to start the MCP Composer service. |
| `LANGFLOW_​MCP_​SERVER_​TIMEOUT` | Integer | `60` | Timeout in seconds for MCP connection setup and tool execution. See [Configure tool execution timeouts](https://docs.langflow.org/mcp-server#configure-tool-execution-timeouts). |
| `LANGFLOW_​MCP_​TOOL_​EXECUTION_​TIMEOUT` | Integer | `180` | Global timeout in seconds for MCP tool calls. See [Configure tool execution timeouts](https://docs.langflow.org/mcp-server#configure-tool-execution-timeouts). |
| `LANGFLOW_​MCP_​MAX_​SESSIONS_​PER_​SERVER` | Integer | `10` | Maximum number of MCP sessions to keep per unique server. |
| `LANGFLOW_​ADD_​PROJECTS_​TO_​MCP_​SERVERS` | Boolean | `True` | Whether to automatically add newly created projects to the user's MCP servers configuration. If `false`, projects must be manually added to MCP servers. |
| `LANGFLOW_​MCP_​SERVERS_​LOCKED` | Boolean | `False` | If `true`, non-superusers cannot add, edit, or remove MCP server connections through the UI or API. Superusers retain full access. For more information, see [Restrict MCP server management to superusers](https://docs.langflow.org/mcp-server#restrict-mcp-server-management). |
| `LANGFLOW_​MCP_​SERVER_​ALLOWED_​PACKAGES` | String | Not set | Comma-separated allowlist of package names that MCP `npx` / `uvx` stdio servers may download and run. Leave unset for single-tenant compatibility. An empty value blocks all package runners. |
| `LANGFLOW_​MCP_​SERVER_​ENV_​ALLOWLIST` | String | Not set | Comma-separated allowlist of environment-variable names an MCP stdio config may set. Leave unset for single-tenant compatibility; production preflight warns when it is unset. An empty value blocks all tenant-supplied environment variables. |
| `LANGFLOW_​MCP_​SERVER_​INTERPRETER_​HARDENING` | Boolean | `False` | If `true`, blocks tenant-controlled Python, Node.js, and shell MCP entrypoints. Package wrappers and the authenticated internal Langflow MCP server still work. |
| `LANGFLOW_​MCP_​SERVER_​DOCKER_​HARDENING` | Boolean | `False` | If `true`, applies a strict argument policy to MCP `docker` stdio servers so tenants cannot mount the host filesystem or use privileged flags. |


## Troubleshoot Langflow MCP servers [​](https://docs.langflow.org/mcp-server#troubleshooting-mcp-server)


For troubleshooting advice for MCP servers and clients, see [Troubleshoot Langflow: MCP issues](https://docs.langflow.org/troubleshoot#mcp).


## See also [​](https://docs.langflow.org/mcp-server#see-also)


- [Use Langflow as an MCP client](https://docs.langflow.org/mcp-client)
- [Use a DataStax Astra DB MCP server](https://docs.langflow.org/mcp-component-astra)
- [MCP server environment variables](https://docs.langflow.org/environment-variables#mcp)


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)

- [Prerequisites](https://docs.langflow.org/mcp-server#prerequisites)
- [Serve flows as MCP tools](https://docs.langflow.org/mcp-server#select-flows-to-serve)
  - [Prevent automatic MCP server configuration for Langflow projects](https://docs.langflow.org/mcp-server#prevent-automatic-mcp-server-configuration-for-langflow-projects)
  - [Selectively enable and disable MCP servers for Langflow projects](https://docs.langflow.org/mcp-server#selectively-enable-and-disable-mcp-servers-for-langflow-projects)
  - [Edit flow tool names and descriptions](https://docs.langflow.org/mcp-server#edit-flow-tool-names-and-descriptions)
  - [Configure tool execution timeouts](https://docs.langflow.org/mcp-server#configure-tool-execution-timeouts)- [Connect clients to your Langflow MCP server](https://docs.langflow.org/mcp-server#connect-clients-to-use-the-servers-actions)
- [MCP server authentication](https://docs.langflow.org/mcp-server#authentication)
- [Deploy your Langflow MCP server externally](https://docs.langflow.org/mcp-server#deploy-your-server-externally)
- [Use MCP Inspector to test and debug flows](https://docs.langflow.org/mcp-server#test-and-debug-flows)
- [Disable the legacy MCP SSE transport](https://docs.langflow.org/mcp-server#disable-legacy-sse)
- [Restrict MCP server management to superusers](https://docs.langflow.org/mcp-server#restrict-mcp-server-management)
- [MCP server environment variables](https://docs.langflow.org/mcp-server#mcp-server-environment-variables)
- [Troubleshoot Langflow MCP servers](https://docs.langflow.org/mcp-server#troubleshooting-mcp-server)
- [See also](https://docs.langflow.org/mcp-server#see-also)[Manage Privacy Choices](https://docs.langflow.org/mcp-server#)

---

# Create custom Python components | Langflow Documentation

`https://docs.langflow.org/components-custom-components`

# Create custom Python components

Use the Custom component quickstart to add an example component to Langflow, and then use the reference guide that follows for more advanced component customization.

Copy page ⌥C Version: 1.12.x On this page
## Custom component quickstart​
## How components execute​
## Inputs and outputs​
*An output is usually an instance of Output from lfx.io.*

*For example, this component has one output that returns a Table:*

*This behavior is controlled by the group_outputs parameter:*

*You can allow a custom component to support Tool Mode by setting tool_mode=True:*

## Typed annotations​
## Enable dynamic fields​
## Error handling and logging​
## Contribute custom components to Langflow​








Create your own custom components to add any functionality you need to Langflow, from API integrations to data processing.


In Langflow's node-based environment, each node is a "component" that performs discrete functions. Custom components in Langflow are built upon:


- The Python class that inherits from `Component`.
- Class-level attributes that identify and describe the component.
- [Input and output lists](https://docs.langflow.org/components-custom-components#inputs-and-outputs) that determine data flow.
- Methods that define the component's behavior and logic.
- Internal variables for [Error handling and logging](https://docs.langflow.org/components-custom-components#error-handling-and-logging)


Use the [Custom component quickstart](https://docs.langflow.org/components-custom-components#quickstart) to add an example component to Langflow, and then use the reference guide that follows for more advanced component customization.


## Custom component quickstart [​](https://docs.langflow.org/components-custom-components#quickstart)


Create a custom `DataFrameProcessor` component by creating a Python file, saving it in the correct folder, including an `__init__.py` file, and loading it into Langflow.


### Create a Python file [​](https://docs.langflow.org/components-custom-components#create-a-python-file)


1. Create a Python file for your component, such as `dataframe_processor.py`.
2. Write your component as an object of the [`Component`](https://github.com/langflow-ai/langflow/blob/main/src/backend/base/langflow/custom/custom_component/component.py) class. Create a new class that inherits from `Component` and override the base class's methods. ```python from typing import Any, Dict, Optional import pandas as pd from lfx.custom.custom_component.component import Component class DataFrameProcessor(Component): """A component that processes pandas DataFrames with various operations.""" ```
3. Define class attributes to provide information about your custom component: ```python from typing import Any, Dict, Optional import pandas as pd from lfx.custom.custom_component.component import Component class DataFrameProcessor(Component): """A component that processes pandas DataFrames with various operations.""" display_name: str = "DataFrame Processor" description: str = "Process and transform pandas DataFrames with various operations like filtering, sorting, and aggregation." documentation: str = "https://docs.langflow.org/components-dataframe-processor" icon: str = "DataframeIcon" priority: int = 100 name: str = "dataframe_processor" ```
  - `display_name`: A user-friendly name shown in the visual editor.
  - `description`: A brief description of what your component does.
  - `documentation`: A link to detailed documentation.
  - `icon`: An emoji or icon identifier for visual representation. Langflow uses [Lucide](https://lucide.dev/icons) for icons. To assign an icon to your component, set the icon attribute to the name of a Lucide icon as a string, such as `icon = "file-text"`. Langflow renders icons from the Lucide library automatically. For more information, see [Contributing bundles](https://docs.langflow.org/contributing-bundles#add-the-bundle-to-the-frontend-folder).
  - `priority`: An optional integer to control display order. Lower numbers appear first.
  - `name`: An optional internal identifier that defaults to class name.4. Define the component's interface by specifying its inputs, outputs, and the method that will process them. The method name must match the `method` field in your outputs list, as this is how Langflow knows which method to call to generate each output. This example creates a minimal custom component skeleton. ```python from typing import Any, Dict, Optional import pandas as pd from lfx.custom.custom_component.component import Component class DataFrameProcessor(Component): """A component that processes pandas DataFrames with various operations.""" display_name: str = "DataFrame Processor" description: str = "Process and transform pandas DataFrames with various operations like filtering, sorting, and aggregation." documentation: str = "https://docs.langflow.org/components-dataframe-processor" icon: str = "DataframeIcon" priority: int = 100 name: str = "dataframe_processor" # input and output lists inputs = [] outputs = [] # method def some_output_method(self): return ... ```


### Save the custom component [​](https://docs.langflow.org/components-custom-components#custom-component-path)


Save the custom component in the Langflow directory where the UI will discover and load it.


By default, Langflow looks for custom components in the `src/lfx/src/lfx/components` directory.


When saving components in the default directory, components must be organized in a specific directory structure to be properly loaded and displayed in the visual editor.


Components must be placed inside category folders, not directly in the base directory.


The category folder name determines where the component appears in the Langflow **Core components** menu. For example, to add the example `DataFrameProcessor` component to the **Data** category, place it in the `data` subfolder:


```text
src/lfx/src/lfx/components/
    └── data/                      # Category folder (determines menu location)
        ├── __init__.py            # Required - makes it a Python package
        └── dataframe_processor.py # Your custom component file
```


If you're creating custom components in a different location using the `LANGFLOW_COMPONENTS_PATH` [environment variable](https://docs.langflow.org/environment-variables), components must be similarly organized in a specific directory structure to be displayed in the visual editor.


```text
/your/custom/components/path/    # Base directory set by LANGFLOW_COMPONENTS_PATH
    └── category_name/
        ├── __init__.py
        └── custom_component.py
```


You can have multiple category folders to organize components into different categories, with multiple components inside each folder:


```text
/app/custom_components/
    ├── data/
    │   ├── __init__.py
    │   ├── custom_component.py
    │   └── dataframe_processor.py
    └── tools/
        ├── __init__.py
        └── custom_tool.py
```


### Create the `__init__.py` file [​](https://docs.langflow.org/components-custom-components#create-the-__init__py-file)


Each category directory **must** contain an `__init__.py` file for Langflow to properly recognize and load the components. This is a Python package requirement that ensures the directory is treated as a module.


To include the `DataFrameProcessor` component, create a file named `__init__.py` in your component's directory with the following content.


```python
from .dataframe_processor import DataFrameProcessor

__all__ = ["DataFrameProcessor"]
```


### Load your component [​](https://docs.langflow.org/components-custom-components#load-your-component)


Ensure the application builds your component.


1. To rebuild the backend and frontend, run `make install_frontend && make build_frontend && make install_backend && uv run langflow run --port 7860`.
2. Refresh the frontend application. Your new `DataFrameProcessor` component is available in the **Core components** menu under the **Data** category in the visual editor.


### Docker deployment [​](https://docs.langflow.org/components-custom-components#docker-deployment)


When running Langflow in Docker, mount your custom components directory and set the `LANGFLOW_COMPONENTS_PATH` environment variable in the `docker run` command to point to the custom components directory.


```bash
docker run -d \
  --name langflow \
  -p 7860:7860 \
  -v ./custom_components:/app/custom_components \
  -e LANGFLOW_COMPONENTS_PATH=/app/custom_components \
  langflowai/langflow:latest
```


Create the same custom components directory structure as the example in [Save the custom component](https://docs.langflow.org/components-custom-components#custom-component-path).


```text
/app/custom_components/          # LANGFLOW_COMPONENTS_PATH
    └── data/
        ├── __init__.py
        └── dataframe_processor.py
```


## How components execute [​](https://docs.langflow.org/components-custom-components#how-components-execute)


Langflow's engine manages:


1. **Instantiation**: A component is created and internal structures are initialized.
2. **Assigning Inputs**: Values from the visual editor or connections are assigned to component fields.
3. **Validation and Setup**: Optional hooks like `_pre_run_setup`.
4. **Outputs Generation**: `run()` or `build_results()` triggers output methods.


You can customize execution by overriding these optional hooks in your custom component code.


- **`_pre_run_setup()`** - Used during **Validation and Setup**. Add this method inside your component class to initialize component state before execution begins: ```python class MyComponent(Component): # ... your inputs, outputs, and other attributes ... def _pre_run_setup(self): if not hasattr(self, "_initialized"): self._initialized = True self.iteration = 0 ```
- **Override `run` or `_run`** - Used during **Outputs Generation**. Add this method inside your component class to customize the main execution logic: ```python class MyComponent(Component): async def_run(self): # Custom execution logic here # This runs instead of the default output method calls pass ```
- **Store data in `self.ctx`**. Use `self.ctx` in any of your component methods to share data between method calls. ```python class MyComponent(Component): def _pre_run_setup(self): # Initialize counter in setup self.ctx["processed_items"] = 0 def process_data(self) -> Data: # Increment counter during processing self.ctx["processed_items"] += 1 return Data(data={"item": f"processed {self.ctx['processed_items']}"}) def get_summary(self) -> Data: # Access counter in different method total = self.ctx["processed_items"] return Data(data={"summary": f"Processed {total} items total"}) ```


## Inputs and outputs [​](https://docs.langflow.org/components-custom-components#inputs-and-outputs)


Inputs and outputs are **class-level configurations** that define how data flows through the component, how it appears in the visual editor, and how connections to other components are validated.


### Inputs [​](https://docs.langflow.org/components-custom-components#inputs)


Inputs are defined in a class-level `inputs` list. When Langflow loads the component, it uses this list to render component fields and [ports](https://docs.langflow.org/concepts-components#component-ports) in the visual editor. Users or other components provide values or connections to fill these inputs.


An input is usually an instance of a class from `lfx.io` (such as `StrInput`, `DataInput`, or `MessageTextInput`).


For example, this component has three inputs: a text field (`StrInput`), a Boolean toggle (`BoolInput`), and a dropdown selection (`DropdownInput`).


```python
from lfx.io import StrInput, BoolInput, DropdownInput

inputs = [
    StrInput(name="title", display_name="Title"),
    BoolInput(name="enabled", display_name="Enabled", value=True),
    DropdownInput(name="mode", display_name="Mode", options=["Fast", "Safe", "Experimental"], value="Safe")
]
```


The `StrInput` creates a single-line text field for entering text. The `name="title"` parameter means you access this value in your component methods with `self.title`, while `display_name="Title"` shows "Title" as the label in the visual editor.


The `BoolInput` creates a boolean toggle that's enabled by default with `value=True`. Users can turn this on or off, and you access the current state with `self.enabled`.


The `DropdownInput` provides a selection menu with three predefined options: "Fast", "Safe", and "Experimental". The `value="Safe"` sets "Safe" as the default selection, and you access the user's choice with `self.mode`.


For a list of all available parameters, see the [BaseInputMixin definition](https://github.com/langflow-ai/langflow/blob/main/src/lfx/src/lfx/inputs/input_mixin.py) in the Langflow codebase.


For a list of all available input types, see the [input type definitions](https://github.com/langflow-ai/langflow/blob/main/src/lfx/src/lfx/inputs/inputs.py) in the Langflow codebase.


```python
from lfx.io import StrInput, DataInput, MultilineInput, IntInput, BoolInput, DropdownInput, FileInput, CodeInput, ModelInput, HandleInput, Output
```


### Outputs [​](https://docs.langflow.org/components-custom-components#outputs)


Outputs are defined in a class-level `outputs` list. When Langflow renders a component, each output becomes a connector point in the visual editor. When you connect something to an output, Langflow automatically calls the corresponding method and passes the returned object to the next component.


An output is usually an instance of `Output` from `lfx.io`.


For example, this component has one `output` that returns a `Table`:


```python
from lfx.io import Output
from lfx.schema import DataFrame

outputs = [
    Output(
        name="df_out",
        display_name="DataFrame Output",
        method="build_df"
    )
]

def build_df(self) -> DataFrame:
    # Process data and return DataFrame
    df = DataFrame({"col1": [1, 2], "col2": [3, 4]})
    self.status = f"Built DataFrame with {len(df)} rows."
    return df
```


The `Output` creates a connector point in the visual editor labeled **DataFrame Output**. The `name="df_out"` parameter identifies this output, while `display_name="DataFrame Output"` shows the label in the UI. The `method="build_df"` parameter tells Langflow to call the `build_df` method when this output is connected to another component.


The `build_df` method processes data and returns a `Table`. The `-> DataFrame` type annotation helps Langflow validate connections and provides color-coding in the visual editor. You can also set `self.status` to show progress messages in the UI.


For a complete list of all available parameters, see the [Output class definition](https://github.com/langflow-ai/langflow/blob/main/src/lfx/src/lfx/template/field/base.py) in the Langflow codebase. Common parameters include:


**Additional return types:**


- **`Message`**: Structured chat messages
- **`JSON`**: Flexible object with `.data` and optional `.text`
- **`Table`**: Tabular data (pandas DataFrame subclass)
- **Primitive types**: `str`, `int`, `bool`, not recommended for type consistency


#### Associated methods [​](https://docs.langflow.org/components-custom-components#associated-methods)


Each output is linked to a method where the output method name must match the method name. The method typically returns objects like `Message`, `JSON`, or `Table`, and can use inputs with `self.<input_name>`.


For example, the `Output` defines a connector point called `file_contents` that will call the `read_file` method when connected. The `read_file` method accesses the filename input with `self.filename`, reads the file content, sets a status message, and returns the content wrapped in a `JSON` object.


```python
Output(
    name="file_contents",
    display_name="File Contents",
    method="read_file"
)

def read_file(self) -> Data:
    path = self.filename
    with open(path, "r") as f:
        content = f.read()
    self.status = f"Read {len(content)} chars from {path}"
    return Data(data={"content": content})
```


#### Components with multiple outputs [​](https://docs.langflow.org/components-custom-components#components-with-multiple-outputs)


A component can define multiple outputs. Each output can have a different corresponding method.


For example:


```python
outputs = [
    Output(display_name="Processed Data", name="processed_data", method="process_data"),
    Output(display_name="Debug Info", name="debug_info", method="provide_debug_info"),
]
```


By default, components in Langflow that produce multiple outputs only allow one output selection in the visual editor. The component will have only one output port where the user can select the preferred output type.


This behavior is controlled by the `group_outputs` parameter:


- **`group_outputs=False` (default)**: When a component has more than one output and `group_outputs` is `false` or not set, the outputs are grouped in the visual editor, and the user must select one. Use this option when the component is expected to return only one type of output when used in a flow.
- **`group_outputs=True`**: All outputs are available simultaneously in the visual editor. The component has one output port for each output, and the user can connect zero or more outputs to other components. Use this option when the component is expected to return multiple values that are used in parallel by downstream components or processes.


- False or not set
- True


In this example, the visual editor provides a single output port, and the user can select one of the outputs. Since `group_outputs=False` is the default behavior, it doesn't need to be explicitly set in the component, as shown in this example.


```python
outputs = [
    Output(
        name="structured_output",
        display_name="Structured Output",
        method="build_structured_output",
    ),
    Output(
        name="dataframe_output",
        display_name="DataFrame Output",
        method="build_structured_dataframe",
    ),
]
```


In this example, all outputs are available simultaneously in the visual editor.


```python
outputs = [
    Output(
        name="true_result",
        display_name="True",
        method="true_response",
        group_outputs=True,
    ),
    Output(
        name="false_result",
        display_name="False",
        method="false_response",
        group_outputs=True,
    ),
]
```


### Tool mode [​](https://docs.langflow.org/components-custom-components#tool-mode)


Components that support **Tool Mode** can be used as standalone components (when *not* in **Tool Mode**) or as tools for other components with a **Tools** input, such as **Agent** components.


You can allow a custom component to support **Tool Mode** by setting `tool_mode=True`:


```python
inputs = [
    MessageTextInput(
        name="message",
        display_name="Mensage",
        info="Enter the message that will be processed directly by the tool",
        tool_mode=True,
    ),
]
```


## Typed annotations [​](https://docs.langflow.org/components-custom-components#typed-annotations)


In Langflow, typed annotations allow Langflow to visually guide users and maintain flow consistency. Always annotate your output methods with return types like `-> Data`, `-> Message`, or `-> DataFrame` to enable proper visual editor color-coding and validation. Use `JSON`, `Message`, or `Table` wrappers instead of returning plain structures for better consistency. Stay consistent with types across your components to make flows predictable and easier to build.


Typed annotations provide color-coding where outputs like `-> Data` or `-> Message` get distinct colors, automatic validation that blocks incompatible connections, and improved readability for users to quickly understand data flow between components.


### Common return types [​](https://docs.langflow.org/components-custom-components#common-return-types)


- Message
- Data
- DataFrame
- Primitive Types


For chat-style outputs. Connects to any of several `Message` -compatible inputs.


```python
def produce_message(self) -> Message:
    return Message(text="Hello! from typed method!", sender="System")
```


For structured data like dicts or partial texts. Connects only to `DataInput` (ports that accept `JSON`).


```python
def get_processed_data(self) -> Data:
    processed = {"key1": "value1", "key2": 123}
    return Data(data=processed)
```


For tabular data. Connects only to `DataFrameInput` (ports that accept `Table`).


```python
def build_df(self) -> DataFrame:
    pdf = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
    return DataFrame(pdf)
```


Returning primitives is allowed, but wrapping in `JSON` or `Message` is recommended for better consistency in the visual editor.


```python
def compute_sum(self) -> int:
    return sum(self.numbers)
```


## Enable dynamic fields [​](https://docs.langflow.org/components-custom-components#enable-dynamic-fields)


In **Langflow**, dynamic fields allow inputs to change or appear based on user interactions. You can make an input dynamic by setting `dynamic=True`. Optionally, setting `real_time_refresh=True` triggers the `update_build_config` method to adjust the input's visibility or properties in real time, creating a contextual visual editor experience that only exposes relevant fields based on the user's choices.


In this example, the operator field triggers updates with `real_time_refresh=True`. The `regex_pattern` field is initially hidden and controlled with `dynamic=True`.


```python
from lfx.custom import Component
from lfx.io import DropdownInput, StrInput

class RegexRouter(Component):
    display_name = "Regex Router"
    description = "Demonstrates dynamic fields for regex input."

    inputs = [
        DropdownInput(
            name="operator",
            display_name="Operator",
            options=["equals", "contains", "regex"],
            value="equals",
            real_time_refresh=True,
        ),
        StrInput(
            name="regex_pattern",
            display_name="Regex Pattern",
            info="Used if operator='regex'",
            dynamic=True,
            show=False,
        ),
    ]
```


### Show or hide fields based on user selections [​](https://docs.langflow.org/components-custom-components#show-or-hide-fields-based-on-user-selections)


When a user changes a field with `real_time_refresh=True`, Langflow calls your `update_build_config` method.


This method lets you show, hide, or modify other fields based on what the user selected.


This example shows the `regex_pattern` field only when the user selects "regex" from the operator dropdown.


```python
def update_build_config(self, build_config: dict, field_value: str, field_name: str | None = None) -> dict:
    if field_name == "operator":
        if field_value == "regex":
            build_config["regex_pattern"]["show"] = True
        else:
            build_config["regex_pattern"]["show"] = False
    return build_config
```


You can modify additional field properties in `update_build_config` other than just `show` and `hide`.


- **`required`**: Make fields required or optional dynamically ```python if field_value == "regex": build_config["regex_pattern"]["required"] = True else: build_config["regex_pattern"]["required"] = False ```
- **`advanced`**: Move fields to the "Advanced" section ```python if field_value == "experimental": build_config["regex_pattern"]["advanced"] = False # Show in main section else: build_config["regex_pattern"]["advanced"] = True # Hide in advanced ```
- **`options`**: Change dropdown options based on other selections ```python if field_value == "regex": build_config["operator"]["options"] = ["regex", "contains", "starts_with"] else: build_config["operator"]["options"] = ["equals", "contains", "not_equals"] ```


## Error handling and logging [​](https://docs.langflow.org/components-custom-components#error-handling-and-logging)


You can raise standard Python exceptions such as `ValueError` or specialized exceptions like `ToolException` when validation fails. Langflow automatically catches these and displays appropriate error messages in the visual editor, helping users quickly identify what went wrong.


```python
def compute_result(self) -> str:
    if not self.user_input:
        raise ValueError("No input provided.")
    # ...
```


Alternatively, instead of stopping a flow abruptly, you can return a `JSON` object containing an `"error"` field. This approach allows the flow to continue operating and enables downstream components to detect and handle the error gracefully.


```python
def run_model(self) -> Data:
    try:
        # ...
    except Exception as e:
        return Data(data={"error": str(e)})
```


Langflow provides several tools to help you debug and manage component execution. You can use `self.status` to display short messages about execution results directly in the visual editor, making troubleshooting easier for users.


```python
def parse_data(self) -> Data:
# ...
self.status = f"Parsed {len(rows)} rows successfully."
return Data(data={"rows": rows})
```


You can halt individual output paths when certain conditions fail using `self.stop()`, without stopping other outputs from the same component.


This example stops the output if the user input is empty, preventing the component from processing invalid data.


```python
def some_output(self) -> Data:
if not self.user_input or len(self.user_input.strip()) == 0:
    self.stop("some_output")
    return Data(data={"error": "Empty input provided"})
```


You can log key execution details inside components using `self.log()`. These logs are stored as structured data and displayed in the "Logs" or "Events" section of the component's detail view, and can be accessed later through the **Logs** button in the visual editor or exported files.


Component logs are distinct from Langflow's main application logging system. `self.log()` creates component-specific logs that appear in the UI, while Langflow's main logging system uses [structlog](https://www.structlog.org) for application-level logging that outputs to `langflow.log` files. For more information, see [Logs](https://docs.langflow.org/logging).


This example logs a message when the component starts processing a file.


```python
def process_file(self, file_path: str):
self.log(f"Processing file {file_path}")
```


## Contribute custom components to Langflow [​](https://docs.langflow.org/components-custom-components#contribute-custom-components-to-langflow)


To contribute your custom component to the Langflow project, see [Contribute components](https://docs.langflow.org/contributing-components).


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)

- [Custom component quickstart](https://docs.langflow.org/components-custom-components#quickstart)
  - [Create a Python file](https://docs.langflow.org/components-custom-components#create-a-python-file)
  - [Save the custom component](https://docs.langflow.org/components-custom-components#custom-component-path)
  - [Create the `__init__.py` file](https://docs.langflow.org/components-custom-components#create-the-__init__py-file)
  - [Load your component](https://docs.langflow.org/components-custom-components#load-your-component)
  - [Docker deployment](https://docs.langflow.org/components-custom-components#docker-deployment)- [How components execute](https://docs.langflow.org/components-custom-components#how-components-execute)
- [Inputs and outputs](https://docs.langflow.org/components-custom-components#inputs-and-outputs)
  - [Inputs](https://docs.langflow.org/components-custom-components#inputs)
  - [Outputs](https://docs.langflow.org/components-custom-components#outputs)
  - [Tool mode](https://docs.langflow.org/components-custom-components#tool-mode)- [Typed annotations](https://docs.langflow.org/components-custom-components#typed-annotations)
  - [Common return types](https://docs.langflow.org/components-custom-components#common-return-types)- [Enable dynamic fields](https://docs.langflow.org/components-custom-components#enable-dynamic-fields)
  - [Show or hide fields based on user selections](https://docs.langflow.org/components-custom-components#show-or-hide-fields-based-on-user-selections)- [Error handling and logging](https://docs.langflow.org/components-custom-components#error-handling-and-logging)
- [Contribute custom components to Langflow](https://docs.langflow.org/components-custom-components#contribute-custom-components-to-langflow)[Manage Privacy Choices](https://docs.langflow.org/components-custom-components#)

---

# Install custom dependencies | Langflow Documentation

`https://docs.langflow.org/install-custom-dependencies`

Copy page ⌥C Version: 1.12.x On this page
## Install custom dependencies in Langflow Desktop​
## Install custom dependencies in Langflow OSS​
*The base executable is langflow; there is no langflow-base command.*

## Add dependencies to the Langflow codebase​
*To add a dependency to the base package, navigate to src/backend/base and run:*

*You can optionally use make add instead of uv add:*

## See also​





Langflow provides optional dependency groups and support for custom dependencies to extend Langflow functionality. This guide covers how to add dependencies for different Langflow installations, including Langflow Desktop and Langflow OSS.


The Langflow codebase uses three package layers:


- The minimal application (`langflow-base`) is managed at `src/backend/base/pyproject.toml`. As of Langflow 1.12, it is a complete Langflow install: UI, API, platform services, built-in components, and the `langflow` command, without provider extensions. It is version-aligned with `langflow`, and depends on `lfx`. There is no `langflow-core` package.
- The full package (`langflow`) is managed by the root-level `pyproject.toml`. It depends on the same `langflow-base` version and adds the curated standalone `lfx-*` provider extensions.
- The `lfx` package is managed at `src/lfx/pyproject.toml`. LFX is a lightweight CLI tool for executing and serving Langflow flows. The `lfx` package does not provide optional dependency groups for end users.


## Install custom dependencies in Langflow Desktop [​](https://docs.langflow.org/install-custom-dependencies#langflow-desktop)


To add dependencies to Langflow Desktop, add an entry for the package to the application's `requirements.txt` file:


- On macOS, the file is located at `/Users/USER/.langflow/data/requirements.txt`.
- On Windows, the file is located at `C:\Users\USER\AppData\Roaming\com.Langflow\data\requirements.txt`.


Add each dependency to `requirements.txt` on its own line in the format `DEPENDENCY==VERSION`, such as `matplotlib==3.10.0`.


Restart Langflow Desktop to install the dependencies.


If you need to change or uninstall custom dependencies, edit the `requirements.txt` file, and then restart Langflow Desktop.


## Install custom dependencies in Langflow OSS [​](https://docs.langflow.org/install-custom-dependencies#install-custom-dependencies-in-langflow-oss)


To install your own custom dependencies in your Langflow environment, add them with your package manager.


If you're working within a cloned Langflow repository, add dependencies with `uv add` because there is already a `pyproject.toml` file for uv to reference:


```bash
uv add DEPENDENCY
```


### Install optional dependency groups for `langflow` [​](https://docs.langflow.org/install-custom-dependencies#install-optional-dependency-groups-for-langflow)


The `langflow` package (main) provides optional dependency groups that extend its functionality.


By default, installing `langflow` without any extras includes all dependencies listed in the `[project.dependencies]` section. Optional dependency groups are not installed by default and must be explicitly requested.


These optional dependencies are listed in the [langflow `pyproject.toml`](https://github.com/langflow-ai/langflow/blob/main/pyproject.toml) file under `[project.optional-dependencies]`.


Install dependency groups using pip's `[extras]` syntax. For example, to install `langflow` with the `postgresql` dependency group, enter the following command:


```bash
uv pip install "langflow[postgresql]"
```


To install multiple extras, use commas to separate each dependency group:


```bash
uv pip install "langflow[postgresql,audio]"
```


Use the `bundles` extra to install the non-PyTorch providers from `lfx-bundles` plus the opt-in standalone packages listed in [Additional bundles](https://docs.langflow.org/extensions-bundle-list#additional-bundles):


```bash
uv pip install "langflow[bundles]"
```


### Install optional dependency groups for `langflow-base` [​](https://docs.langflow.org/install-custom-dependencies#install-optional-dependency-groups-for-langflow-base)


`langflow-base` is the minimal workable Langflow: the UI, API, platform services, and built-in components, without provider extensions. It is version-aligned with `langflow` starting with version 1.12.0. It includes platform services such as Redis, Chroma, MCP, Kubernetes, object storage, and tracing support. The `langflow` package depends on this same version of `langflow-base` and adds curated standalone extensions.


The `langflow-base` package provides its own optional dependency groups that are separate from those in the `langflow` package. The `langflow-base` package can be installed as a standalone package with these optional dependency groups.


By default, installing `langflow-base` without any extras includes all dependencies listed in the `[project.dependencies]` section. Optional dependency groups are not installed by default and must be explicitly requested. These optional dependency groups are listed in the [langflow-base `pyproject.toml`](https://github.com/langflow-ai/langflow/blob/main/src/backend/base/pyproject.toml) file under `[project.optional-dependencies]`.


Install `langflow-base` with optional dependency groups using pip's `[extras]` syntax. For example, to install `langflow-base` with the `postgresql` dependency group:


```bash
uv pip install "langflow-base[postgresql]"
```


To install multiple extras, use commas to separate each dependency group:


```bash
uv pip install "langflow-base[postgresql,cassandra]"
```


Provider components are installed as extensions. For example, install `lfx-openai` beside `langflow-base`, or use `langflow` to install the curated provider set:


```bash
uv pip install langflow-base lfx-openai
```


The base executable is `langflow`; there is no `langflow-base` command.


### Use a virtual environment to test custom dependencies [​](https://docs.langflow.org/install-custom-dependencies#use-a-virtual-environment-to-test-custom-dependencies)


When testing locally, use a virtual environment to isolate your dependencies and prevent conflicts with other Python projects.


For example, if you want to experiment with a custom dependency like `matplotlib` with Langflow:


```bash
# Create and activate a virtual environment
uv venv YOUR_LANGFLOW_VENV
source YOUR_LANGFLOW_VENV/bin/activate

# Install langflow and your additional dependency
uv pip install langflow matplotlib
```


You can also install `langflow-base` with specific optional dependency groups in your virtual environment:


```bash
# Install runnable base with selected compatibility extras
uv pip install "langflow-base[postgresql,cassandra]" matplotlib
```


If you're working within a cloned Langflow repository, add dependencies with `uv add` to reference the existing `pyproject.toml` files:


```bash
uv add matplotlib
```


The `uv add` command automatically updates the `uv.lock` file in the appropriate location.


## Add dependencies to the Langflow codebase [​](https://docs.langflow.org/install-custom-dependencies#add-dependencies-to-the-langflow-codebase)


When contributing to the Langflow codebase, you might need to add dependencies to Langflow.


To add a dependency to the `main` package, run `uv add DEPENDENCY` from the project root. For example:


```bash
uv add matplotlib
```


Dependencies can be added to the `main` package as regular dependencies at `[project.dependencies]` or optional dependencies at `[project.optional-dependencies]`.


To add a dependency to the `base` package, navigate to `src/backend/base` and run:


```bash
uv add DEPENDENCY
```


To add a development dependency for testing, linting, or debugging, navigate to `src/backend/base` and run:


```bash
cd src/backend/base && uv add --group dev DEPENDENCY
```


Dependencies can be added to the `base` package as regular dependencies at `[project.dependencies]`, development dependencies at `[dependency-groups.dev]`, or optional dependencies at `[project.optional-dependencies]`.


You can optionally use `make add` instead of `uv add`:


```bash
# Equivalent to: uv add matplotlib
make add main="matplotlib"

# Equivalent to: cd src/backend/base && uv add --group dev matplotlib
make add devel="matplotlib"

# Equivalent to: cd src/backend/base && uv add matplotlib
make add base="matplotlib"
```


Alternatively, you can add these dependencies manually to the appropriate `pyproject.toml` file:


```text
[project]
dependencies = [
    "matplotlib>=3.8.0"
]
```


Or as an optional dependency in the main package:


```text
[project.optional-dependencies]
plotting = [
    "matplotlib>=3.8.0",
]
```


Or as a development dependency in the base package:


```text
[dependency-groups]
dev = [
    "matplotlib>=3.8.0",
]
```


## See also [​](https://docs.langflow.org/install-custom-dependencies#see-also)


- [Containerize a Langflow application](https://docs.langflow.org/develop-application)
- [Create custom Python components](https://docs.langflow.org/components-custom-components)


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)

- [Install custom dependencies in Langflow Desktop](https://docs.langflow.org/install-custom-dependencies#langflow-desktop)
- [Install custom dependencies in Langflow OSS](https://docs.langflow.org/install-custom-dependencies#install-custom-dependencies-in-langflow-oss)
  - [Install optional dependency groups for `langflow`](https://docs.langflow.org/install-custom-dependencies#install-optional-dependency-groups-for-langflow)
  - [Install optional dependency groups for `langflow-base`](https://docs.langflow.org/install-custom-dependencies#install-optional-dependency-groups-for-langflow-base)
  - [Use a virtual environment to test custom dependencies](https://docs.langflow.org/install-custom-dependencies#use-a-virtual-environment-to-test-custom-dependencies)- [Add dependencies to the Langflow codebase](https://docs.langflow.org/install-custom-dependencies#add-dependencies-to-the-langflow-codebase)
- [See also](https://docs.langflow.org/install-custom-dependencies#see-also)[Manage Privacy Choices](https://docs.langflow.org/install-custom-dependencies#)

---

# Langflow release notes | Langflow Documentation

`https://docs.langflow.org/release-notes`

# Langflow release notes
## Prepare to upgrade​
## 1.12.x​
## 1.11.x​
*For 1.11.x release notes, see the 1.11.x documentation.*

## 1.10.x​
*For 1.10.x release notes, see the 1.10.x documentation.*

## 1.9.x​
*For 1.9.x release notes, see the 1.9.x documentation.*

## 1.8.x​
*For 1.8.x release notes, see the 1.8.x documentation.*

## Earlier releases​








This page summarizes significant changes to Langflow in each release. For all changes, see the Changelog.

Copy page ⌥C Version: 1.12.x On this page

This page summarizes significant changes to Langflow in each release. For all changes, see the [Changelog](https://github.com/langflow-ai/langflow/releases/latest).


Due to strict SemVer requirements, Langflow Desktop can have different patch versions than the core Langflow OSS Python package, but the major and minor versions are aligned.


## Prepare to upgrade [​](https://docs.langflow.org/release-notes#prepare-to-upgrade)


To avoid the impact of potential breaking changes and test new versions, the Langflow team recommends the following upgrade process:


1. Recommended: [Export your projects](https://docs.langflow.org/api-projects#export-a-project) to create backups of your flows: ```bash curl -X GET \ "$LANGFLOW_SERVER_URL/api/v1/projects/download/$PROJECT_ID" \ -H "accept: application/json" \ -H "x-api-key: $LANGFLOW_API_KEY" ``` To export flows from the visual editor, see [Import and export flows](https://docs.langflow.org/concepts-flows-import).
2. Install the new version:
  - **Langflow OSS Python package**: Install the new version in a new virtual environment. For instructions, see [Install and run the Langflow OSS Python package](https://docs.langflow.org/get-started-installation#install-and-run-the-langflow-oss-python-package).
  - **Langflow Docker image**: Run the new image in a separate container, or upgrade your existing image. For more information, see [Upgrade the Langflow Docker image](https://docs.langflow.org/deployment-docker#upgrade-the-langflow-docker-image).
  - **Langflow Desktop**: To upgrade in place, open Langflow Desktop, and then click **Upgrade Available** in the Langflow header. If you want to isolate the new version, you must install Langflow Desktop on a separate physical or virtual machine, and then [import your flows](https://docs.langflow.org/concepts-flows-import) to the new installation.3. [Import your flows](https://docs.langflow.org/concepts-flows-import) to test them in the new version, [upgrading components](https://docs.langflow.org/concepts-components#component-versions) as needed. When upgrading components, you can use the **Create backup flow before updating** option if you didn't previously export your flows.
4. If you installed the new version in isolation, upgrade your primary installation after testing the new version. If you made changes to your flows in the isolated installation, you might want to export and import those flows back to your upgraded primary installation so you don't have to repeat the component upgrade process.


## 1.12.x [​](https://docs.langflow.org/release-notes#112x)


Highlights of this release include the following changes. For all changes, see the [Changelog](https://github.com/langflow-ai/langflow/releases/latest).


### Breaking changes [​](https://docs.langflow.org/release-notes#breaking-changes)


- Connector security (1.12.4) Update the server or the database URL before you upgrade if the connection matches one of these cases. If PGVector connects to `localhost` or `127.0.0.1`, add that host to `LANGFLOW_SSRF_ALLOWED_HOSTS`. For example, `LANGFLOW_SSRF_ALLOWED_HOSTS=localhost,127.0.0.1`. Do the same for a private or container hostname, such as `postgres`. A public hostname needs no entry. MongoDB and Couchbase SRV targets must be allowlisted by their own hostnames, or by a wildcard such as `*.cluster.internal`. For more information, see [SSRF protection](https://docs.langflow.org/api-keys-and-authentication#ssrf-protection). If an SQL Database URL starts with `mysql+mysqlconnector://`, add `allow_local_infile=false` to the query string. If it starts with `mariadb+mariadbconnector://`, add `local_infile=false`. Use `?` when the URL has no query string, and `&` when it already has one: `mysql+mysqlconnector://user:password@db.example.com/app?allow_local_infile=false`. On a trusted single-tenant server, `LANGFLOW_RESTRICT_LOCAL_FILE_ACCESS=false` keeps the previous URLs working and also lets flows read local server files. For more information, see [component hardening](https://docs.langflow.org/api-keys-and-authentication#multi-tenant-component-hardening). If the URL points at a TLS certificate or key on the server, copy the file into a directory only an administrator can change, set `LANGFLOW_DATABASE_TLS_FILES_DIR` to that directory, and point the URL at the new path. For example, set `LANGFLOW_DATABASE_TLS_FILES_DIR=/etc/langflow/db-tls` and use `postgresql://user:password@db.example.com/app?sslrootcert=/etc/langflow/db-tls/ca.pem`. PostgreSQL `sslrootcert`, `sslcert`, and `sslkey`, and MySQL or MariaDB `ssl_ca`, `ssl_cert`, and `ssl_key`, can use files in that directory. For more information, see [component hardening](https://docs.langflow.org/api-keys-and-authentication#multi-tenant-component-hardening).
- Custom component input names (1.12.4) A custom component input `name` can no longer match a method name on `Component` or `CustomComponent`, or a method defined by the custom component class. Names that commonly collide include `index`, `start`, `stop`, `run`, `log`, `validate`, and `variables`. Components that previously ran without reading `self.<name>` will also fail to load. To fix the collision, rename the custom component's input `name` and update any connections that target it. The display name is not affected. For more information, see [Inputs](https://docs.langflow.org/components-custom-components#inputs).
- MCP stdio Node.js launch options (1.12.4) MCP stdio configurations can no longer place Node.js runtime options or `inspect` before a server script, even when `LANGFLOW_MCP_SERVER_INTERPRETER_HARDENING` is `false`. For example, `node --no-warnings server.js` must be changed to `node server.js`. Options intended for the server may still follow its script, such as `node server.js --server-option`. Shell wrappers also reject sh/bash glob and brace expansion, and cmd variable, caret, or double-quote syntax. Use an approved launcher directly with separate command and arguments for those payloads.
- `langflow-base` is now the minimal install Langflow 1.12 makes `langflow-base` a complete, version-aligned installation of the Langflow application. Replace any `langflow-base~=0.x` pins with `langflow-base~=1.12.0` pins.
- Ongoing breaking change: bundle separation Bundle separation concludes in 1.12. `uv pip install langflow` no longer installs all provider bundles, and includes only a curated list of providers. Saved flows continue to operate as expected, and existing component class names remain compatible. If a required provider package is not installed, the component is visible in the visual editor, but the flow won't build or run until you install the package. Langflow displays an error that names the missing package, so you can install it. To install a package, such as Exa, run `uv pip install lfx-exa` in your virtual environment. For more information, see [Additional bundles](https://docs.langflow.org/extensions-bundle-list#additional-bundles).
- Admin Page removed Langflow OSS no longer includes an **Admin Page**. The `/admin` route, the account-menu **Admin Page** link, and the user-management page are gone. Superusers can no longer manage users or passwords in the visual editor. To manage users, use the [Users API](https://docs.langflow.org/api-users). `/login/admin` is still the admin sign-in endpoint and page. For more information, see [Manage users as an administrator](https://docs.langflow.org/api-keys-and-authentication#manage-users-as-an-administrator).


### New features [​](https://docs.langflow.org/release-notes#new-features)


- OpenTelemetry export Langflow can export health traces, metrics, and logs over OTLP to your own backend. For more information, see [OpenTelemetry](https://docs.langflow.org/observability-opentelemetry), [New Relic](https://docs.langflow.org/observability-new-relic), and [Instana](https://docs.langflow.org/observability-instana).
- Python Interpreter microVM sandbox Set `LANGFLOW_SANDBOX_BACKEND=exec-sandbox` to run the [**Python Interpreter** component](https://docs.langflow.org/python-interpreter) in a dedicated [QEMU microVM](https://www.qemu.org/docs/master/system/i386/microvm.html) instead of in the Langflow server process. The microVM is not included in a default `uv pip install langflow` installation. To install it, run `uv pip install 'langflow[sandbox]'`. For more information, see [Isolate executions in a microVM](https://docs.langflow.org/python-interpreter#sandbox).
- Production preflight checks Set `LANGFLOW_DEPLOYMENT_PROFILE=prod` to probe your Langflow deployment before any workers start. The default remains `dev`, which skips prod checks. For more information, see [Production preflight checks](https://docs.langflow.org/deployment-prod-best-practices#production-preflight).
- Disable the legacy MCP SSE transport Set `LANGFLOW_MCP_SSE_ENABLED=false` to return a `404` from the legacy SSE transport endpoint. Streamable HTTP is not affected. For more information, see [Disable the legacy MCP SSE transport](https://docs.langflow.org/mcp-server#disable-legacy-sse).
- OrcaRouter bundle The **OrcaRouter** bundle adds an OrcaRouter language model component. For more information, see [OrcaRouter](https://docs.langflow.org/bundles-orcarouter).
- IBM Confluent bundle The **IBM Confluent** bundle adds Kafka, Tableflow, and Real-Time Context Engine components. For more information, see [IBM Confluent](https://docs.langflow.org/bundles-confluent).
- Deployment tweak policy Set `LANGFLOW_TWEAKS_POLICY` to control which component fields an API caller can override at run time. For more information, see [Restrict API tweaks](https://docs.langflow.org/deployment-tweaks-policy).
- Catalog and model policy APIs Superusers can block or allow components, starter templates, model providers, and specific models. For more information, see [Catalog and model policy](https://docs.langflow.org/api-governance-policy).


## 1.11.x [​](https://docs.langflow.org/release-notes#111x)


For 1.11.x release notes, see the [1.11.x documentation](https://docs.langflow.org/1.11.0/release-notes).


## 1.10.x [​](https://docs.langflow.org/release-notes#110x)


For 1.10.x release notes, see the [1.10.x documentation](https://docs.langflow.org/1.10.0/release-notes).


## 1.9.x [​](https://docs.langflow.org/release-notes#19x)


For 1.9.x release notes, see the [1.9.x documentation](https://docs.langflow.org/1.9.0/release-notes).


## 1.8.x [​](https://docs.langflow.org/release-notes#18x)


For 1.8.x release notes, see the [1.8.x documentation](https://docs.langflow.org/1.8.0/release-notes).


## Earlier releases [​](https://docs.langflow.org/release-notes#earlier-releases)


See the [Changelog](https://github.com/langflow-ai/langflow/releases).


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)

- [Prepare to upgrade](https://docs.langflow.org/release-notes#prepare-to-upgrade)
- [1.12.x](https://docs.langflow.org/release-notes#112x)
  - [Breaking changes](https://docs.langflow.org/release-notes#breaking-changes)
  - [New features](https://docs.langflow.org/release-notes#new-features)- [1.11.x](https://docs.langflow.org/release-notes#111x)
- [1.10.x](https://docs.langflow.org/release-notes#110x)
- [1.9.x](https://docs.langflow.org/release-notes#19x)
- [1.8.x](https://docs.langflow.org/release-notes#18x)
- [Earlier releases](https://docs.langflow.org/release-notes#earlier-releases)[Manage Privacy Choices](https://docs.langflow.org/release-notes#)

---

# Deploy Langflow on Docker | Langflow Documentation

`https://docs.langflow.org/deployment-docker`

# Deploy Langflow on Docker
## Quickstart​
*By default, the official Docker images set LANGFLOW_AUTO_LOGIN=false by default.*

*Replace SUPERUSER_PASSWORD with a strong password for the Langflow superuser.*

*For more information, see Docker image defaults.*

*Then, access Langflow at http://localhost:7860/.*

## Use Docker Compose​
## Customize the Docker Compose file​
*Configure a container's database credentials using a .env file.*

## Build and run the Docker image from source​
*To override these values, edit docker/dev.docker-compose.yml directly.*

## Upgrade the Langflow Docker image​
## Docker image defaults​







Podman can be used instead of Docker for all commands shown here. For more information, see the Podman documentation.

Copy page ⌥C Version: 1.12.x On this page


Running applications in Docker containers ensures consistent behavior across different systems and eliminates dependency conflicts.


Langflow publishes base, default, and extended application images with different provider inventories. Before deploying, see [Choose a Langflow Docker image](https://docs.langflow.org/deployment/docker-image-profiles) for the canonical tags, composition, version-pinning, migration, and rollback guidance.


This guide demonstrates several ways to run Langflow with [Docker](https://docs.docker.com/) and [Docker Compose](https://docs.docker.com/compose/):


- [Quickstart](https://docs.langflow.org/deployment-docker#quickstart): Start a Langflow container with default values.
- [Use Docker Compose](https://docs.langflow.org/deployment-docker#docker-compose): Run Langflow with a persistent PostgreSQL database and configurable environment variables.
- [Customize the Docker Compose file](https://docs.langflow.org/deployment-docker#customize): Package a flow or add your own code into a custom image built on top of the official Langflow image.
- [Build and run the Docker image from source](https://docs.langflow.org/deployment-docker#build-from-source): Build a Docker image from a local clone of the repo, or start a full development environment with hot reload on both frontend and backend.
- [Upgrade the Langflow Docker image](https://docs.langflow.org/deployment-docker#upgrade-the-langflow-docker-image): Upgrade to a newer image without losing your database or flows.
- [Docker image defaults](https://docs.langflow.org/deployment-docker#docker-image-security-defaults): Environment variables included in the Langflow image and how to override them.


## Quickstart [​](https://docs.langflow.org/deployment-docker#quickstart)


With Docker installed and running on your system, run the following command:


```bash
docker run -p 7860:7860 \
  -e LANGFLOW_AUTO_LOGIN=false \
  -e LANGFLOW_SUPERUSER_PASSWORD=SUPERUSER_PASSWORD \
  langflowai/langflow:latest
```


By default, the official Docker images set `LANGFLOW_AUTO_LOGIN=false` by default.


Replace `SUPERUSER_PASSWORD` with a strong password for the Langflow superuser.


For more information, see [Docker image defaults](https://docs.langflow.org/deployment-docker#docker-image-security-defaults).


Then, access Langflow at `http://localhost:7860/`.


This starts a pre-built Docker image with automatic login enabled for local development. For more control over the configuration, see [Use Docker Compose](https://docs.langflow.org/deployment-docker#docker-compose).


## Use Docker Compose [​](https://docs.langflow.org/deployment-docker#docker-compose)


Docker Compose gives you more control over your configuration, such as setting environment variables, using a persistent PostgreSQL database instead of the default SQLite database, and including custom dependencies.


The Langflow repo includes a ready-to-use Compose file at `docker_example/docker-compose.yml` that pulls the latest Langflow image from Docker Hub and includes persistent volume storage with PostgreSQL.


1. Clone the Langflow repository: ```bash git clone https://github.com/langflow-ai/langflow.git ```
2. Navigate to the `docker_example` directory: ```bash cd langflow/docker_example ```
3. Run the Docker Compose file: ```bash docker compose up ```
4. Access Langflow at `http://localhost:7860/`.


## Customize the Docker Compose file [​](https://docs.langflow.org/deployment-docker#customize)


Customize the Docker Compose file to fit your deployment's requirements.


### Include environment variables [​](https://docs.langflow.org/deployment-docker#include-environment-variables)


Configure a container's database credentials using a `.env` file.


1. Create a `.env` file with your database credentials in the same directory as `docker-compose.yml`: ```text # Database credentials POSTGRES_USER=myuser POSTGRES_PASSWORD=mypassword POSTGRES_DB=langflow # Langflow configuration LANGFLOW_DATABASE_URL=postgresql://myuser:mypassword@postgres:5432/langflow LANGFLOW_CONFIG_DIR=/app/langflow LANGFLOW_SUPERUSER_PASSWORD=SUPERUSER_PASSWORD ``` Replace `SUPERUSER_PASSWORD` with a strong password for the Langflow superuser.
2. Edit `docker-compose.yml` to replace the hardcoded values with variable references for both the `langflow` and `postgres` services: ```yaml services: langflow: environment: - LANGFLOW_DATABASE_URL=${LANGFLOW_DATABASE_URL} - LANGFLOW_CONFIG_DIR=${LANGFLOW_CONFIG_DIR} - LANGFLOW_SUPERUSER_PASSWORD=${LANGFLOW_SUPERUSER_PASSWORD} postgres: environment: - POSTGRES_USER=${POSTGRES_USER} - POSTGRES_PASSWORD=${POSTGRES_PASSWORD} - POSTGRES_DB=${POSTGRES_DB} ``` With variable references in place, Docker Compose reads the values from your `.env` file at startup.


For a complete list of available environment variables, see [Langflow environment variables](https://docs.langflow.org/environment-variables).


### Package a flow into the image [​](https://docs.langflow.org/deployment-docker#package-your-flow-as-a-docker-image)


Embed a flow JSON directly into a Docker image. This is useful for distributing a specific flow as a standalone container or deploying it to environments like Kubernetes.


1. Create a project directory and change into it: ```bash mkdir langflow-custom && cd langflow-custom ```
2. Add your flow's JSON file to the directory. You can download an example, or use your own: ```bash # Download an example flow wget https://raw.githubusercontent.com/langflow-ai/langflow-helm-charts/refs/heads/main/examples/flows/basic-prompting-hello-world.json # Or copy your own flow file cp /path/to/your/flow.json . ```
3. Create a `Dockerfile`: ```dockerfile FROM langflowai/langflow:latest RUN mkdir /app/flows COPY ./*.json /app/flows/ ENV LANGFLOW_LOAD_FLOWS_PATH=/app/flows ```
4. Build, test, and optionally push your image: ```bash docker build -t myuser/langflow-custom:1.0.0 . docker run -p 7860:7860 -e LANGFLOW_AUTO_LOGIN=true myuser/langflow-custom:1.0.0 docker push myuser/langflow-custom:1.0.0 # optional ```


For Kubernetes deployment, see [Deploy the Langflow production environment on Kubernetes](https://docs.langflow.org/deployment-kubernetes-prod).


### Add custom code or dependencies [​](https://docs.langflow.org/deployment-docker#customize-the-langflow-docker-image)


Patch custom code into the pre-built image's installation. This is useful when you need to add custom Python packages, replace a built-in component, or make targeted changes without a [full source build](https://docs.langflow.org/deployment-docker#build-from-source).


This example replaces the built-in **Message History** component, but the same pattern applies to any component or file.


1. Create a directory for your custom Langflow setup: ```bash mkdir langflow-custom && cd langflow-custom ```
2. Create the directory structure that mirrors the component path: ```bash mkdir -p src/lfx/src/lfx/components/models_and_agents ```
3. Place your modified `memory.py` file in that directory.
4. Create a `Dockerfile`: ```dockerfile FROM langflowai/langflow:latest WORKDIR /app COPY src/lfx/src/lfx/components/models_and_agents/memory.py /tmp/memory.py RUN python -c "import site; print(site.getsitepackages()[0])" > /tmp/site_packages.txt RUN SITE_PACKAGES=$(cat /tmp/site_packages.txt) && \ mkdir -p "$SITE_PACKAGES/lfx/components/models_and_agents" && \ cp /tmp/memory.py "$SITE_PACKAGES/lfx/components/models_and_agents/" RUN SITE_PACKAGES=$(cat /tmp/site_packages.txt) && \ find "$SITE_PACKAGES" -name "*.pyc" -delete && \ find "$SITE_PACKAGES" -name "__pycache__" -type d -exec rm -rf {} + EXPOSE 7860 CMD ["python", "-m", "langflow", "run", "--host", "0.0.0.0", "--port", "7860"] ```
5. Build and run the image: ```bash docker build -t myuser/langflow-custom:1.0.0 . docker run -p 7860:7860 -e LANGFLOW_AUTO_LOGIN=true myuser/langflow-custom:1.0.0 ```


## Build and run the Docker image from source [​](https://docs.langflow.org/deployment-docker#build-from-source)


If you've cloned the Langflow repository and want to build and run your local changes inside a Docker container, run:


```bash
make docker_build
```


This builds `docker/build_and_push.Dockerfile` and tags the result `langflow:<version>`.


To run the image after building, run:


```bash
docker run -p 7860:7860 \
  -e LANGFLOW_SUPERUSER_PASSWORD=SUPERUSER_PASSWORD \
  langflow:VERSION
```


Replace the following:


- `SUPERUSER_PASSWORD`: a strong password for the Langflow superuser
- `VERSION`: the version in `pyproject.toml` at the repo root


The image sets `LANGFLOW_AUTO_LOGIN=false`, so a superuser password is required unless you set `LANGFLOW_AUTO_LOGIN=true`. For more information, see [Docker image defaults](https://docs.langflow.org/deployment-docker#docker-image-security-defaults).


To build only the LFX executor CLI image instead of the full Langflow application, run:


```bash
make lfx_docker_build
```


This builds `src/lfx/docker/Dockerfile` and tags the result `lfx:latest`. It produces a lightweight Alpine-based image that contains only the `lfx` CLI tool, with no frontend or Langflow UI.


The build context is the repo root, not `src/lfx/`. The Dockerfile copies from `pyproject.toml`, `uv.lock`, `src/lfx/`, and `src/sdk/`, so the full workspace is sent to the daemon. A root `.dockerignore` file partially mitigates this, but the first build will be slower than you might expect for a small CLI image.


### Write a custom source-based Dockerfile [​](https://docs.langflow.org/deployment-docker#write-a-custom-source-based-dockerfile)


When writing a source-based Dockerfile, you must copy the manifest files (`pyproject.toml`, `README.md`, and `uv.lock` where present) for the workspace members that `uv sync` needs to resolve dependencies before source is available. The workspace members are defined in `[tool.uv.workspace]` in the root `pyproject.toml`. You do not need to copy manifests for members like `src/langflow-stepflow` that are not required for the initial dependency-only sync. The full source is copied later with `COPY ./src`, which brings those omitted members into the image before the second `uv sync`.


1. To copy all manifest files to your Dockerfile, include the following: ```dockerfile COPY ./uv.lock /app/uv.lock COPY ./README.md /app/README.md COPY ./pyproject.toml /app/pyproject.toml COPY ./src/backend/base/README.md /app/src/backend/base/README.md COPY ./src/backend/base/pyproject.toml /app/src/backend/base/pyproject.toml COPY ./src/lfx/README.md /app/src/lfx/README.md COPY ./src/lfx/pyproject.toml /app/src/lfx/pyproject.toml COPY ./src/sdk/README.md /app/src/sdk/README.md COPY ./src/sdk/pyproject.toml /app/src/sdk/pyproject.toml COPY ./src/bundles /app/src/bundles ```
2. To install dependencies and copy the source, include the following: ```dockerfile RUN --mount=type=cache,target=/root/.cache/uv \ uv sync --frozen --no-install-project --no-editable --extra postgresql --no-group dev COPY ./src /app/src RUN --mount=type=cache,target=/root/.cache/uv \ uv sync --frozen --no-editable --extra postgresql --no-group dev ``` The first `uv sync` installs only dependencies before the source is copied, so that Docker can cache that layer. The second `uv sync` installs the project packages (`langflow`, `lfx`) from the copied source. Both calls are required. Omitting the second will produce a container with all dependencies present but the project packages missing, which fails at runtime.


The supported source build uses [`docker/build_and_push.Dockerfile`](https://github.com/langflow-ai/langflow/blob/main/docker/build_and_push.Dockerfile). Build its `base` target for the bundle-free application, `full` for the normal curated distribution, or `full-bundles` for the extended provider inventory.


### Start a development environment with `make dcdev_up` [​](https://docs.langflow.org/deployment-docker#start-a-development-environment-with-make-dcdev_up)


`make dcdev_up` starts a full development environment from source using [`docker/dev.docker-compose.yml`](https://github.com/langflow-ai/langflow/blob/main/docker/dev.docker-compose.yml). This is useful if you want to work on the Langflow codebase within a container.


To build the Langflow dcdev image, run:


```bash
make dcdev_up
```


Access the backend and Langflow UI at `http://localhost:7860/`. Access the frontend dev server at `http://localhost:3000/`.


The following environment variables are set by default:


| Variable | Default value | Description |
| --- | --- | --- |
| `LANGFLOW_​DATABASE_​URL` | `postgresql://langflow:langflow@postgres:5432/langflow` | PostgreSQL connection string |
| `LANGFLOW_​SUPERUSER` | `langflow` | Initial admin username |
| `LANGFLOW_​CONFIG_​DIR` | `/var/lib/langflow` | Directory for Langflow config and data |


`LANGFLOW_SUPERUSER_PASSWORD` is not set in the compose file. With the default `LANGFLOW_AUTO_LOGIN=true`, Langflow generates a random bootstrap password for the auto-login account. If you set `LANGFLOW_AUTO_LOGIN=false`, you must set `LANGFLOW_SUPERUSER_PASSWORD` to a strong password before startup. The legacy value `langflow` is not allowed.


To override these values, edit `docker/dev.docker-compose.yml` directly.


`docker/dev.docker-compose.yml` uses literal values in its `environment:` block, such as `- LANGFLOW_SUPERUSER=langflow`. Docker Compose v2 gives `environment:` block literal values higher precedence than shell-exported variables and `env_file:`, so neither `export LANGFLOW_SUPERUSER=myadmin` or a `.env` file will override them. Edit the file directly instead.


## Upgrade the Langflow Docker image [​](https://docs.langflow.org/deployment-docker#upgrade-the-langflow-docker-image)


To upgrade a Langflow Docker deployment without losing your database or flows, do the following:


1. Keep data on persistent volumes, so when you upgrade Langflow, you will replace only the container image. Use Docker volumes or bind mounts for Langflow data and the database so they persist outside of the container. For example, this Docker Compose file uses a bind mount for Langflow data (`./langflow-data` on the host) and a named volume for the PostgreSQL database (`langflow-postgres`): ```yaml services: langflow: image: langflowai/langflow:1.11.0 environment: - LANGFLOW_CONFIG_DIR=/app/langflow - LANGFLOW_SUPERUSER_PASSWORD=${LANGFLOW_SUPERUSER_PASSWORD} volumes: - ./langflow-data:/app/langflow postgres: # Pinned to a specific Debian base (trixie) so the postgres:16 tag does # not silently roll its OS, which triggers a glibc collation mismatch # warning on existing volumes. See https://github.com/langflow-ai/langflow/issues/9608 image: postgres:16-trixie volumes: - langflow-postgres:/var/lib/postgresql/data volumes: langflow-postgres: ``` For additional examples, see the [Docker Compose configuration](https://docs.langflow.org/deployment-docker#docker-compose) and the [docker_example compose file](https://github.com/langflow-ai/langflow/blob/main/docker_example/docker-compose.yml).
2. Pull the new image and update the image tag in your `docker-compose.yml` or `docker run` command. With Docker Compose, set the image in your compose file, such as `image: langflowai/langflow:1.11.0`, and then pull: ```bash docker compose pull ``` With `docker run`, pull the image: ```bash docker pull langflowai/langflow:1.11.0 ```
3. Restart the container. The same volumes will be reattached, so your database and flows are preserved. With Docker Compose: ```bash docker compose up -d ``` With `docker run`, use the same volume mount and the new image tag: ```bash docker run -p 7860:7860 \ -v langflow-data:/app/langflow \ -e LANGFLOW_SUPERUSER_PASSWORD=SUPERUSER_PASSWORD \ langflowai/langflow:1.11.0 ``` Replace `SUPERUSER_PASSWORD` with a strong password for the Langflow superuser.


This approach keeps the persistent volumes separate from the Langflow container, so you can upgrade the Langflow application without losing data.


If you need to upgrade to a custom image based on a Langflow release, such as to add `uv` in `1.8.0`, first build a derived image from the official image, and then follow the same steps above. Set the custom image in your compose file or `docker run`, and then pull and restart.


For a minimal Dockerfile that adds `uv` to the 1.8.0 image, see the [release notes](https://docs.langflow.org/release-notes) ("Docker image no longer includes uv or uvx").


## Docker image defaults [​](https://docs.langflow.org/deployment-docker#docker-image-security-defaults)


As of Langflow 1.11.x, official Langflow Docker images set `LANGFLOW_AUTO_LOGIN=false` at image build time. The Langflow application default for non-Docker installs remains `true`.


Because auto-login is disabled, you must set `LANGFLOW_SUPERUSER_PASSWORD` (and optionally `LANGFLOW_SUPERUSER`) unless you explicitly set `LANGFLOW_AUTO_LOGIN=true`.


```bash
docker run -p 7860:7860 \
  -e LANGFLOW_AUTO_LOGIN=true \
  -e LANGFLOW_SUPERUSER_PASSWORD=SUPERUSER_PASSWORD \
  langflowai/langflow:latest
```


For more information, see [Component hardening for untrusted users](https://docs.langflow.org/api-keys-and-authentication#multi-tenant-component-hardening) and [Block custom components](https://docs.langflow.org/deployment-block-custom-components).


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)

- [Quickstart](https://docs.langflow.org/deployment-docker#quickstart)
- [Use Docker Compose](https://docs.langflow.org/deployment-docker#docker-compose)
- [Customize the Docker Compose file](https://docs.langflow.org/deployment-docker#customize)
  - [Include environment variables](https://docs.langflow.org/deployment-docker#include-environment-variables)
  - [Package a flow into the image](https://docs.langflow.org/deployment-docker#package-your-flow-as-a-docker-image)
  - [Add custom code or dependencies](https://docs.langflow.org/deployment-docker#customize-the-langflow-docker-image)- [Build and run the Docker image from source](https://docs.langflow.org/deployment-docker#build-from-source)
  - [Write a custom source-based Dockerfile](https://docs.langflow.org/deployment-docker#write-a-custom-source-based-dockerfile)
  - [Start a development environment with `make dcdev_up`](https://docs.langflow.org/deployment-docker#start-a-development-environment-with-make-dcdev_up)- [Upgrade the Langflow Docker image](https://docs.langflow.org/deployment-docker#upgrade-the-langflow-docker-image)
- [Docker image defaults](https://docs.langflow.org/deployment-docker#docker-image-security-defaults)[Manage Privacy Choices](https://docs.langflow.org/deployment-docker#)

---

# Troubleshoot Langflow | Langflow Documentation

`https://docs.langflow.org/troubleshoot`

# Troubleshoot Langflow

If a component appears to be missing from the Core components and menus, try the following:

Copy page ⌥C Version: 1.12.x On this page
## Missing components​
## No input in the Playground​
*For more information, see Test flows in the Playground.*

## Missing key, no key found, or invalid API key​
## Langflow installation issues​
## Langflow Desktop installation issues​
*To view Langflow Desktop logs, see Desktop logs.*

*To resolve this issue, install protoc using brew install protobuf.*

*To resolve this error, see Python environment failed.*

## Uninstall Langflow​
## Langflow startup issues​
*For more information, see Start Langflow Server with authentication enabled.*

## Langflow upgrade issues​
*For information about managing Langflow versions, see Install Langflow.*

## Langflow MCP issues​
*For more information, see Connect clients to your Langflow MCP server.*

## Token length limit errors in Embedding Model components​
## Document processing errors in Docker containers​
## Custom components and integrations issues​
## Multi-worker deployments​
*For setup instructions, see Deploy Langflow with multiple workers.*

## Voice mode​
## Intel Mac issues​
*For more information, see Workarounds for Intel Mac users.*

## See also​

















This page provides troubleshooting advice for issues you might encounter when using Langflow or contributing to Langflow.


## Missing components [​](https://docs.langflow.org/troubleshoot#missing-components)


As Langflow development continues, components are often recategorized or deprecated for better alignment or to prepare for new components.


If a component appears to be missing from the **Core components** and menus, try the following:


- **Search** for the component.
- Check other component categories and [**Bundles**](https://docs.langflow.org/components-bundle-components).
- Check [legacy components](https://docs.langflow.org/concepts-components#legacy-components), which are hidden by default.
- Check the [Changelog](https://github.com/langflow-ai/langflow/releases/latest) for component changes in recent releases.
- Make sure the component isn't already present in your flow if it is a single-use component.


If you still cannot locate the component, see [Langflow GitHub Issues and Discussions](https://docs.langflow.org/contributing-github-issues).


## No input in the Playground [​](https://docs.langflow.org/troubleshoot#no-input-in-the-playground)


If there is no message input field in the **Playground**, make sure your flow has a [**Chat Input** component](https://docs.langflow.org/chat-input-and-output) that is connected, directly or indirectly, to the **Input** port of a **Language Model** or **Agent** component.


Because the **Playground** is designed for flows that use an LLM in a query-and-response format, such as chatbots and agents, a flow must have **Chat Input**, **Language Model** / **Agent**, and **Chat Output** components to be fully supported by the **Playground** chat interface.


For more information, see [Test flows in the Playground](https://docs.langflow.org/concepts-playground).


## Missing key, no key found, or invalid API key [​](https://docs.langflow.org/troubleshoot#missing-key-no-key-found-or-invalid-api-key)


If you get an API key error when running a flow, try the following:


- For all components that require credentials, make sure those components have a valid credential in the component's settings, such as the **API Key** field.
- If you store your credentials in [Langflow global variables](https://docs.langflow.org/configuration-global-variables), make sure you selected the correct global variable and that the variable contains a valid credential.
- Make sure the provided credentials are active, have the required permissions, and, if applicable, have sufficient funds in the account to execute the required action. For example, model providers require credits to use their LLMs.


## Langflow installation issues [​](https://docs.langflow.org/troubleshoot#langflow-installation-issues)


The following issues can occur when installing Langflow.


### Langflow installation freezes at pip dependency resolution [​](https://docs.langflow.org/troubleshoot#langflow-installation-freezes-at-pip-dependency-resolution)


Installing Langflow OSS with `pip install langflow` slowly fails with this error message:


```text
pip is looking at multiple versions of <<library>> to determine which version is compatible with other requirements. This could take a while.
```


To work around this issue, install Langflow with `uv` instead of `pip`, as explained in [Install and run the Langflow OSS Python package](https://docs.langflow.org/get-started-installation#install-and-run-the-langflow-oss-python-package).


### Linux installation fails to build required package [​](https://docs.langflow.org/troubleshoot#linux-installation-fails-to-build-required-package)


When you try to install Langflow OSS on Linux, installation fails because of outdated or missing packages:


```bash
Resolved 455 packages in 18.92s
  × Failed to build `webrtcvad==2.0.10`
  ├─▶ The build backend returned an error
  ╰─▶ Call to `setuptools.build_meta:__legacy__.build_wheel` failed (exit status: 1)
```


To resolve this error, install the required build dependencies, and then retry the Langflow installation:


```bash
sudo apt-get update
sudo apt-get install build-essential python3-dev
```


If upgrading your packages doesn't fix the issue, install `gcc` separately, and then retry the Langflow installation:


```bash
sudo apt-get install gcc
```


### Installation failure from `webrtcvad` package [​](https://docs.langflow.org/troubleshoot#installation-failure-from-webrtcvad-package)


If you experience an error from the `webrtcvad` package, run `uv pip install webrtcvad-wheels` in your virtual environment, and then retry the Langflow installation.


### `get_body_field` error after installing Langflow [​](https://docs.langflow.org/troubleshoot#get_body_field-error-after-installing-langflow)


After installing Langflow OSS with `pip install langflow` or `uv pip install langflow`, Langflow fails to start with an error that mentions `get_body_field`, such as:


```text
ImportError: cannot import name 'get_body_field' from 'fastapi.dependencies.utils'
```


or:


```text
NameError: name 'get_body_field' is not defined
```


This happens when the resolver installs FastAPI `0.140.5` or later, which removed `get_body_field`.


Langflow 1.11.0 allows FastAPI `>=0.139.0,<1.0.0`, so a fresh install can pull an incompatible FastAPI 0.140.x release.


To work around this, pin FastAPI below 0.140.


To pin FastAPI when installing Langflow:


```bash
uv pip install langflow "fastapi<0.140"
```


To pin FastAPI in an environment where Langflow is already installed:


```bash
uv pip install "fastapi<0.140"
```


Langflow version 1.11.1 resolves a compatible FastAPI 0.140.x and `fastapi-pagination` 0.15.16 pair on a new install, so it does not require this pin. If you constrain these dependencies yourself, use `fastapi-pagination>=0.15.16` with `fastapi>=0.140.5`.


## Langflow Desktop installation issues [​](https://docs.langflow.org/troubleshoot#langflow-desktop-installation-issues)


The following issues can occur when Langflow Desktop installs or updates its bundled Langflow OSS instance.


To view Langflow Desktop logs, see [Desktop logs](https://docs.langflow.org/logging#desktop-logs).


### Protocol buffers (protoc) required for Intel-based Macs [​](https://docs.langflow.org/troubleshoot#protocol-buffers-protoc-required-for-intel-based-macs)


If you're installing Langflow on an Intel-based Mac, you may encounter installation errors if Protocol Buffers Compiler (`protoc`) is not installed.


This requirement doesn't apply to Apple Silicon Macs on ARM64.


To resolve this issue, install `protoc` using `brew install protobuf`.


For more information, including alternative installation methods, see the [Protocol buffers installation documentation](https://protobuf.dev/installation/).


### Langflow installation failed [​](https://docs.langflow.org/troubleshoot#langflow-installation-failed)


Langflow Desktop installed Langflow OSS but couldn't verify the installation. You might see an error dialog with the title `Langflow Installation Failed` and the message `Langflow installation failed. Please check your internet connection and try again. If the problem persists, restart the application.`


To resolve this error, clear Langflow Desktop's Python virtual environment:


1. Close Langflow Desktop.
2. Navigate to Langflow Desktop's data directory at `%LOCALAPPDATA%\com.LangflowDesktop` on Windows, or `~/Library/Application Support/com.LangflowDesktop` on macOS.
3. Delete the `venv` or `python_env` folder.
4. Restart Langflow Desktop.


If the issue persists, ensure you have installed Python version 3.10 or later, and it is accessible by your Langflow installation. If the Python version is correct, try reinstalling Langflow Desktop from [langflow.org/desktop](https://langflow.org/desktop).


### Langflow startup failed [​](https://docs.langflow.org/troubleshoot#langflow-startup-failed)


Langflow Desktop installed Langflow OSS but the OSS backend isn't responding to health checks. You might see an error dialog with the title `Langflow Startup Failed` and the message `Langflow failed to start properly. Please restart the application and try again.`


To resolve this error, do the following:


1. Check if another process is using Langflow Desktop's default port `7860`.
  - On Windows, run `netstat -ano | findstr :7860`.
  - On macOS or Linux, run `lsof -i :7860`.2. If another process is using the port, stop that process or [configure Langflow Desktop to use a different port](https://docs.langflow.org/environment-variables#set-environment-variables-for-langflow-desktop).


### Failed to install uv or unable to find uv [​](https://docs.langflow.org/troubleshoot#failed-to-install-uv-or-unable-to-find-uv)


Langflow Desktop can't locate or install the `uv` executable. You might see an error dialog with the title `UV Installation Failed` and the message `UV installation failed. Please check your internet connection and try again. If the problem persists, restart the application.`


To resolve this error, do the following:


1. In a terminal verify `uv` is installed by running `uv --version`.
2. Based on the output, install `uv` or add it to your PATH: - uv is not installed (command not found) - uv is installed but not found by Langflow Desktop Install `uv` using one of the following methods: - Windows (PowerShell): ```powershell powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex" ``` - macOS or Linux: ```bash curl -LsSf https://astral.sh/uv/install.sh | sh ``` - Any platform (pip): ```bash pip install uv ``` Add `uv` to your PATH so Langflow Desktop can locate it: - Windows: In PowerShell, run: ```powershell [System.Environment]::SetEnvironmentVariable("Path", $env:Path + ";$env:USERPROFILE\.cargo\bin", "User") ``` - macOS or Linux: Add `~/.local/bin` to your PATH in `~/.bashrc` or `~/.zshrc`.
3. Restart Langflow Desktop.


### Python environment failed [​](https://docs.langflow.org/troubleshoot#python-environment-failed)


Langflow Desktop failed to create the Python virtual environment required for Langflow OSS. You might see an error dialog with the title `Python Environment Failed` and the message `Python environment setup failed. Please ensure you have sufficient disk space and try again.`


To resolve this error, do the following:


1. Ensure you have sufficient disk space available (at least 2 GB free).
2. Ensure that you have write permissions in the Langflow Desktop data directory:
  - On Windows: `%LOCALAPPDATA%\com.LangflowDesktop`
  - On macOS: `~/Library/Application Support/com.LangflowDesktop`3. Close Langflow Desktop.
4. Delete the `venv` or `python_env` folder in the Langflow Desktop data directory.
5. Restart Langflow Desktop.


If the issue persists, ensure Python version 3.10 or later is installed and accessible, or reinstall Langflow Desktop from [langflow.org/desktop](https://langflow.org/desktop).


### Python environment failed: Python check failed [​](https://docs.langflow.org/troubleshoot#python-environment-failed-python-check-failed)


Langflow Desktop created the Python virtual environment but couldn't verify that Python is working correctly. You might see an error dialog with the title `Python Environment Failed` and a message about Python verification.


To resolve this error, see [Python environment failed](https://docs.langflow.org/troubleshoot#python-environment-failed).


### Xcode Command Line Tools required [​](https://docs.langflow.org/troubleshoot#xcode-command-line-tools-required)


Langflow Desktop requires [Xcode Command Line Tools](https://developer.apple.com/xcode/resources/) to install Langflow OSS on macOS. You might see an error dialog with the title `Xcode Command Line Tools required!` and instructions to run `xcode-select --install`.


To resolve this error, do the following:


1. Install [Xcode Command Line Tools](https://developer.apple.com/xcode/resources/).
2. Launch Xcode at least once. Xcode performs additional setup on first startup that other tools such as Git, VS Code, and Langflow Desktop depend on.
3. Restart Langflow Desktop.


### C++ build tools required [​](https://docs.langflow.org/troubleshoot#c-build-tools-required)


Microsoft Windows installations of Langflow Desktop require a C++ compiler that might not be present on your system. You might see an error dialog with the title `C++ Build Tools required!` with instructions to install Microsoft C++ Build Tools. Follow the on-screen prompt, or install [Microsoft Visual Studio](https://visualstudio.microsoft.com/downloads/).


### Manual UV installation required [​](https://docs.langflow.org/troubleshoot#manual-uv-installation-required)


Langflow Desktop tried multiple methods to automatically install `uv` but all attempts failed. Desktop requires `uv` to manage Python packages and virtual environments. You might see an error dialog with the title `Manual UV Installation Required` and instructions to install `uv` manually.


To resolve this error, do the following:


1. Install `uv` manually using PowerShell: ```powershell powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex" ``` Or install using pip: ```bash pip install uv ```
2. Verify the installation by running `uv --version` in a new PowerShell or Command Prompt window. If `uv` is not found, add it to your PATH. In PowerShell, run: ```powershell [System.Environment]::SetEnvironmentVariable("Path", $env:Path + ";$env:USERPROFILE\.cargo\bin", "User") ```
3. Restart Langflow Desktop.


## Uninstall Langflow [​](https://docs.langflow.org/troubleshoot#uninstall-langflow)


Uninstalling Langflow depends on how it was installed, and on which operating system.


If you reinstall Langflow after uninstalling, any data you didn't delete will be picked up automatically by the new installation. Delete the data directories listed below if you want a completely fresh start.


### Uninstall the Langflow OSS Python package [​](https://docs.langflow.org/troubleshoot#uninstall-the-langflow-oss-python-package)


1. To uninstall the Langflow OSS Python package, run the following command in the virtual environment where Langflow is installed: ```bash uv pip uninstall langflow ```
2. To remove the Langflow data directory, which contains your flows, settings, and cache, run: - macOS / Linux - Windows ```bash rm -rf ~/.langflow ``` ```powershell Remove-Item -Recurse -Force "$env:USERPROFILE\.langflow" ```


### Uninstall Langflow Desktop [​](https://docs.langflow.org/troubleshoot#uninstall-langflow-desktop)


To uninstall Langflow Desktop, uninstall the application with your OS package manager, and then manually delete the remaining data directories.


- macOS
- Windows


1. Drag `Langflow.app` from `/Applications` to the Trash, or right-click and select **Move to Trash**.
2. Empty the **Trash** to remove the application file.
3. To remove the Langflow data directory, run the following command: ```bash rm -rf ~/.langflow ```
4. To remove the Desktop app support files, run the following commands: ```bash rm -rf ~/Library/Application\ Support/com.LangflowDesktop rm -rf ~/Library/Caches/com.LangflowDesktop rm -rf ~/Library/Logs/com.LangflowDesktop rm -f ~/Library/Preferences/com.LangflowDesktop.plist rm -rf ~/Library/WebKit/com.LangflowDesktop ```


1. Open **Settings** > **Apps** > **Installed apps**.
2. Find **Langflow** in the list, click the menu (**...**), and select **Uninstall**.
3. Follow the on-screen prompts to complete the uninstallation.
4. To remove the Langflow data directory, run the following command: ```powershell Remove-Item -Recurse -Force "$env:LOCALAPPDATA\com.LangflowDesktop" ```


## Langflow startup issues [​](https://docs.langflow.org/troubleshoot#langflow-startup-issues)


The following issues can occur when attempting to start Langflow.


### No `langflow.__main__` module [​](https://docs.langflow.org/troubleshoot#no-langflow__main__-module)


When you try to run Langflow with the command `langflow run`, you encounter the following error:


```bash
> No module named 'langflow.__main__'
```


To resolve this issue, do the following:


1. Run `uv run langflow run` instead of `langflow run`.
2. If that doesn't work, reinstall the latest Langflow version with `uv pip install langflow -U`.
3. If that doesn't work, reinstall Langflow and its dependencies with `uv pip install langflow --pre -U --force-reinstall`.


### Langflow runTraceback [​](https://docs.langflow.org/troubleshoot#langflow-runtraceback)


When you try to run Langflow using the command `langflow run`, you encounter the following error:


```bash
> langflow runTraceback (most recent call last): File ".../langflow", line 5, in <module>  from langflow.__main__ import mainModuleNotFoundError: No module named 'langflow.__main__'
```


There are two possible reasons for this error:


- **Multiple Langflow installations**: You installed Langflow using `pip install langflow` but you already had a previous version of Langflow installed in your system. In this case, you might be running the wrong executable. To solve this issue, run the correct executable by running `python -m langflow run` instead of `langflow run`. If that doesn't work, try uninstalling and reinstalling Langflow with `uv pip install langflow --pre -U`.
- **Version conflict during installation**: Some version conflicts might have occurred during the installation process. To resolve this issue, reinstall Langflow and its dependencies by running `python -m pip install langflow --pre -U --force-reinstall`.


### Environment variables not available from terminal [​](https://docs.langflow.org/troubleshoot#environment-variables-not-available-from-terminal)


Environment variables set in your terminal aren't automatically available to GUI-based applications like Langflow Desktop when launched through the Finder or the Start Menu. To set environment variables for Langflow Desktop, see [Set environment variables for Langflow Desktop](https://docs.langflow.org/environment-variables#set-environment-variables-for-langflow-desktop).


### Access Langflow Desktop startup logs [​](https://docs.langflow.org/troubleshoot#access-langflow-desktop-startup-logs)


If you encounter issues with Langflow Desktop, you might need to [access Langflow Desktop startup logs](https://docs.langflow.org/logging#desktop-logs) for debugging.


### User not found or inactive when running multiple flows [​](https://docs.langflow.org/troubleshoot#user-not-found-or-inactive-when-running-multiple-flows)


When running multiple local Langflow OSS instances on different ports, such as `localhost:7860` and `localhost:7861`, you might see authentication errors in the logs. For example:


```text
[07/22/25 10:57:07] INFO     2025-07-22 10:57:07 - INFO     - User not found
[07/22/25 10:57:07] INFO     2025-07-22 10:57:07 - INFO     - User is inactive
```


To resolve this error, use separate browser instances or browser profiles to access each Langflow instance.


### Package is not installed [​](https://docs.langflow.org/troubleshoot#package-is-not-installed)


In Langflow OSS, you can follow the error message's instructions to install the missing dependency.


To manage dependencies in Langflow Desktop, see [Install custom dependencies in Langflow Desktop](https://docs.langflow.org/install-custom-dependencies#langflow-desktop).


### PostgreSQL asyncpg driver compatibility issue [​](https://docs.langflow.org/troubleshoot#postgresql-asyncpg-driver-compatibility-issue)


The following error can occur when initializing Langflow with a PostgreSQL database:


```text
sqlalchemy.exc.DBAPIError: (sqlalchemy.dialects.postgresql.asyncpg.Error) <class 'asyncpg.exceptions.DataError'>: invalid input for query argument $7: datetime.datetime(2025, 10, 31, 14, 8, 5... (can't subtract offset-naive and offset-aware datetimes)
```


This error occurs because `asyncpg` has stricter timezone handling than `psycopg2`, and is not fully compatible with Langflow's current database schema.


To resolve this issue, remove `asyncpg` from your installation and use `psycopg2` instead.


### PostgreSQL version mismatch: `UNIQUE NULLS DISTINCT` syntax error [​](https://docs.langflow.org/troubleshoot#postgresql-version-mismatch-unique-nulls-distinct-syntax-error)


The following error can occur when initializing Langflow with a PostgreSQL database. Langflow logs a clear message and then exits:


```text
Langflow requires PostgreSQL 15 or higher when using PostgreSQL as the database. The current PostgreSQL version does not support the syntax used by Langflow's schema. Please upgrade your PostgreSQL instance to version 15 or higher.
```


You may also see the underlying SQL error in the traceback:


```text
(psycopg.errors.SyntaxError) syntax error at or near "NULLS"
LINE 13:  CONSTRAINT file_name_user_id_key UNIQUE NULLS DISTINCT (nam...
```


This occurs when you're using a PostgreSQL version prior to version 15. These versions don't support the `UNIQUE NULLS DISTINCT` syntax used by Langflow's database schema. Langflow requires PostgreSQL 15 or higher when configured to use PostgreSQL.


To resolve this issue, upgrade your PostgreSQL instance to version 15 or higher, and then restart Langflow.


### An API key must be passed as query or header [​](https://docs.langflow.org/troubleshoot#an-api-key-must-be-passed-as-query-or-header)


The following error can occur when attempting to sign up on the Langflow sign in page: `An API key must be passed as query or header`.


This means that `LANGFLOW_AUTO_LOGIN` is set to `false`, and only superusers can create and activate non-superuser accounts. Therefore, you are locked out of this Langflow instance.


If you aren't an administrator, then a superuser must create and activate a non-superuser account before you can sign in.


If you are the administrator, sign in with a superuser account, and then create and activate users with the [Users API](https://docs.langflow.org/api-users). Alternatively, restart Langflow with `LANGFLOW_AUTO_LOGIN=true`.


For more information, see [Start Langflow Server with authentication enabled](https://docs.langflow.org/api-keys-and-authentication#start-a-langflow-server-with-authentication-enabled).


### PermissionError on `/app/langflow/secret_key` at startup [​](https://docs.langflow.org/troubleshoot#permissionerror-on-applangflowsecret_key-at-startup)


The Langflow container runs as a non-root user (`uid=1000`). The Langflow image pre-creates `/app/langflow` with that user as the owner, so a new `langflow-data` named volume inherits the correct ownership. If you ran an earlier image build that did not pre-create this directory, the named volume was initialized as `root:root` and the non-root container user cannot write `secret_key` into it, and the error `PermissionError: [Errno 13]` on `/app/langflow/secret_key` appears.


This commonly affects rootful Docker daemons such as Docker Desktop. Podman with rootless user-namespace mapping does not reproduce the issue.


To preserve the `langflow-postgres` data while resetting only the `langflow-data` volume, do the following:


1. Stop the container and find the exact volume name for `langflow-data`. This command lists the volumes, and then searches for `langflow-data`. ```bash docker compose down docker compose config --volumes docker volume ls | grep langflow-data ```
2. Once you have confirmed the exact volume name, remove only that volume: ```bash docker volume rm LANGFLOW_DATA_VOLUME_NAME docker compose pull docker compose up -d ```


Alternatively, if you don't need to preserve the `langflow-postgres` data volume, you can pull the latest container image instead.


```bash
docker compose down -v
docker compose pull
docker compose up -d
```


## Langflow upgrade issues [​](https://docs.langflow.org/troubleshoot#langflow-upgrade-issues)


The following issues can occur when upgrading your Langflow version.


For information about managing Langflow versions, see [Install Langflow](https://docs.langflow.org/get-started-installation).


### There's a mismatch between the models and the database [​](https://docs.langflow.org/troubleshoot#theres-a-mismatch-between-the-models-and-the-database)


The following error can occur during Langflow upgrades when the database schema doesn't match the current version's models:


```bash
There's a mismatch between the models and the database.
```


Back up your database first, and then run the migration fix command:


```bash
uv run langflow migration --fix
```


If the migration fix doesn't resolve the issue, clear the cache by deleting the contents of your Langflow cache folder. The filepath depends on your operating system, installation type, and configuration options. For more information and default filepaths, see [Memory management options](https://docs.langflow.org/memory).


### Langflow Desktop says it is running the latest version, but it is actually behind [​](https://docs.langflow.org/troubleshoot#langflow-desktop-says-it-is-running-the-latest-version-but-it-is-actually-behind)


If you are running Langflow Desktop version 1.4.2 or earlier, the UI might incorrectly report that you are on the latest version when a newer version is available.


This happens because the automatic update feature in the UI was introduced in version 1.4.2. Earlier versions can't automatically detect or apply updates.


To resolve this issue, uninstall Langflow Desktop, and then [download and install the latest version of Langflow Desktop](https://langflow.org/desktop).


### 422 error when freezing components after upgrading Pydantic/FastAPI dependencies [​](https://docs.langflow.org/troubleshoot#422-error-when-freezing-components-after-upgrading-pydanticfastapi-dependencies)


If you locally upgrade your Pydantic and FastAPI dependencies, you may encounter a 422 error when trying to freeze components.


This error occurs due to changes in how request bodies are handled in newer versions of these dependencies.


If you're experiencing this issue, update your Langflow installation to version 1.6.5 or later, which includes a fix for this issue.


```bash
uv pip install langflow -U
```


## Langflow MCP issues [​](https://docs.langflow.org/troubleshoot#mcp)


The following issues can occur when using Langflow as an MCP server or client.


### Default project MCP server only works when authentication is None [​](https://docs.langflow.org/troubleshoot#default-project-mcp-server-only-works-when-authentication-is-none)


If the default project MCP server works without authentication, but fails after adding an API key to the server configuration, the API key might have been added to the wrong section of the configuration.


The default MCP server uses streamable HTTP transport. The API key must be added to the `args` array that is passed to `mcp-proxy`, not the `env` object.


Your `args` array must include `"--headers"`, `"x-api-key"`, and your key value. For example:


```json
{
  "mcpServers": {
    "PROJECT_NAME": {
      "command": "uvx",
      "args": [
        "mcp-proxy",
        "--transport",
        "streamablehttp",
        "--headers",
        "x-api-key",
        "YOUR_API_KEY",
        "http://LANGFLOW_SERVER_ADDRESS/api/v1/mcp/project/PROJECT_ID/streamable"
      ]
    }
  }
}
```


For more information, see [Connect clients to your Langflow MCP server](https://docs.langflow.org/mcp-server#connect-clients-to-use-the-servers-actions).


### Claude for Desktop doesn't use MCP server tools correctly [​](https://docs.langflow.org/troubleshoot#claude-for-desktop-doesnt-use-mcp-server-tools-correctly)


If Claude for Desktop doesn't use your server's tools correctly, try explicitly defining the path to your local `uvx` or `npx` executable file in the `claude_desktop_config.json` configuration file:


1. To find your `uvx` path, run `which uvx`. To find your `npx` path, run `which npx`.
2. In your `claude_desktop_config.json` file, add the path to your Langflow MCP server configuration, as shown in the following examples. - uvx - npx ```json { "mcpServers": { "PROJECT_NAME": { "command": "PATH_TO_UVX", "args": [ "mcp-proxy", "http://LANGFLOW_SERVER_ADDRESS/api/v1/mcp/project/PROJECT_ID/streamable" ] } } } ``` ```json { "mcpServers": { "PROJECT_NAME": { "command": "PATH_TO_NPX", "args": [ "-y", "supergateway", "--sse", "http://LANGFLOW_SERVER_ADDRESS/api/v1/mcp/project/PROJECT_ID/streamable" ] } } } ```


### MCP browser-based flows don't open a browser on Windows [​](https://docs.langflow.org/troubleshoot#mcp-browser-based-flows-dont-open-a-browser-on-windows)


This is a known issue when using MCP Tools with browser navigation actions, such as Playwright, on Windows: The agent can execute the tool successfully but the browser tab or window doesn't open.


This issue occurs because the MCP server runs from a Python process, which prevents it from opening browser windows in WSL or Windows.


To work around this issue, use the standalone MCP server approach documented in the [Playwright MCP repository](https://github.com/microsoft/playwright-mcp?tab=readme-ov-file#standalone-mcp-server). After the server is up and running, you can add it as an HTTP/SSE server in Langflow.


For other browser navigation tools, see the provider's documentation for specific troubleshooting guidance.


### "No tools or prompts connected" on MCP servers in mixed Windows/WSL environments [​](https://docs.langflow.org/troubleshoot#no-tools-or-prompts-connected-on-mcp-servers-in-mixed-windowswsl-environments)


If you encounter "No tools or prompts connected" errors or connection failures when using Langflow Desktop as an MCP server with clients running in different environments, such as Langflow on a Windows host and an MCP client in WSL, this is due to network isolation between Windows and WSL environments.


WSL cannot directly access Windows localhost services, and Langflow running on a Windows host is not accessible from WSL clients at `localhost:7860`.


To work around this issue, run the server and host in the same operating environment.


Alternatively, configure Langflow Desktop to accept connections from WSL at the default Windows IP address of `10.255.255.254:7860` instead of `localhost`.


### MCP Tools component loses Tool Mode option after upgrading flows [​](https://docs.langflow.org/troubleshoot#mcp-tools-component-loses-tool-mode-option-after-upgrading-flows)


If you upgrade an existing flow that uses the [**MCP Tools** component](https://docs.langflow.org/mcp-tools) in **Tool Mode**, the component might lose its **Tool Mode** setting after upgrading the flow. This can break flows that rely on the component's **Tool Mode** to expose MCP tools to agents.


If you experience this when upgrading a flow that you created in Langflow version 1.7.1 or earlier, do the following:


1. Select the **MCP Tools** component in your flow.
2. Click **Code** to open the component's code editor.
3. In the component's template structure, locate the `tool_mode` field under `inputs`. The field can be either missing or set to `false`.
4. Add the `tool_mode` field if it's missing, and set it to `true`: ```python tool_mode = True ```
5. Click **Check & Save** to apply the code changes.


## Token length limit errors in Embedding Model components [​](https://docs.langflow.org/troubleshoot#token-length-limit-errors-in-embedding-model-components)


Token length errors can happen if your chunking strategy doesn't align with your embedding model's tokenization limits. For more information, see [Tokenization errors due to chunk size](https://docs.langflow.org/split-text#chunk-size).


## Document processing errors in Docker containers [​](https://docs.langflow.org/troubleshoot#document-processing-errors-in-docker-containers)


If you're running Langflow in a Docker container, you might encounter errors when using components that handle files or images, such as the [**Read File** component](https://docs.langflow.org/read-file) or [**Docling** components](https://docs.langflow.org/bundles-docling). To resolve these errors, you might need to install additional system dependencies.


When running Langflow in a Linux-based Docker container, Docling requires system libraries that aren't included in the base Docker image. If you see errors related to document or image processing, add the following to your Dockerfile:


```dockerfile
RUN apt-get update && apt-get install -y libgl1 libglib2.0-0
```


These dependencies are required by Docling for document processing operations.


For more information about customizing Docker images, see [Customize the Langflow Docker image with your own code](https://docs.langflow.org/deployment-docker#customize-the-langflow-docker-image).


## Custom components and integrations issues [​](https://docs.langflow.org/troubleshoot#custom-components-and-integrations-issues)


For troubleshooting advice for a third-party integration, see the information about that integration in the Langflow documentation and the provider's documentation.


If you are building a custom component, see [Error handling and logging for custom Python components](https://docs.langflow.org/components-custom-components#error-handling-and-logging).


### Custom components not appearing in the visual editor [​](https://docs.langflow.org/troubleshoot#custom-components-not-appearing-in-the-visual-editor)


If your custom components are not appearing in the Langflow visual editor, try the following troubleshooting steps:


1. Ensure your components follow the [required directory structure](https://docs.langflow.org/components-custom-components#directory-structure-requirements). ```text /your/custom/components/path/ # Base directory set by LANGFLOW_COMPONENTS_PATH └── category_name/ # Required category subfolder that determines menu name ├── __init__.py # Required └── custom_component.py # Component file ```
2. Verify each category directory includes an `__init__.py` file. This is required for Python to recognize the directory as a module.
3. Use the command line argument instead of the environment variable for `LANGFLOW_COMPONENTS_PATH`. If you're using the `LANGFLOW_COMPONENTS_PATH` environment variable and components aren't loading, try the `--components-path` command line argument instead: ```bash uv run langflow run --components-path /path/to/your/custom/components ```


If you continue to experience issues, please [report them on GitHub](https://github.com/langflow-ai/langflow/issues) with details about your directory structure and component setup.


## Multi-worker deployments [​](https://docs.langflow.org/troubleshoot#multi-worker-deployments)


### Workers report `JobQueueNotFoundError` [​](https://docs.langflow.org/troubleshoot#workers-report-jobqueuenotfounderror)


The load balancer is routing poll or stream requests to a different worker than the one that started the build.


To resolve this issue:


- Ensure `LANGFLOW_JOB_QUEUE_TYPE=redis` is set on **all** workers, not just some. Mixed-mode deployments (some workers using `asyncio`, others using `redis`) are not supported.
- Verify all workers can reach the same Redis instance.


For setup instructions, see [Deploy Langflow with multiple workers](https://docs.langflow.org/deployment-multi-worker).


### Redis connection refused or auth errors [​](https://docs.langflow.org/troubleshoot#redis-connection-refused-or-auth-errors)


If your Redis instance requires a password or TLS, you must use `LANGFLOW_REDIS_QUEUE_URL` (for example, `rediss://user:password@host:6380/1`). The individual `LANGFLOW_REDIS_QUEUE_HOST` and `LANGFLOW_REDIS_QUEUE_PORT` settings construct a plain unauthenticated connection and do not support auth or TLS. Managed Redis services such as AWS ElastiCache with AUTH, Google MemoryStore with TLS, and Upstash all require the URL form.


### Cache and queue keys colliding [​](https://docs.langflow.org/troubleshoot#cache-and-queue-keys-colliding)


If `LANGFLOW_REDIS_QUEUE_DB` is set to the same database index used by the Langflow cache, keys from both systems will mix and produce unpredictable behavior.


The cache defaults to DB `0` and the job queue defaults to DB `1`. Verify both settings point to different database indices.


### Server refuses to start with multiple workers and `LANGFLOW_JOB_QUEUE_TYPE=asyncio` [​](https://docs.langflow.org/troubleshoot#server-refuses-to-start-with-multiple-workers-and-langflow_job_queue_typeasyncio)


Startup fails with a `RuntimeError` that explains the in-memory job queue is worker-local.


Polling and streaming delivery use a follow-up `GET /api/v1/build/<job_id>/events` request after the initial build POST, and the load balancer can route those requests to different workers, which produces intermittent "Job not found" errors.


Set `LANGFLOW_JOB_QUEUE_TYPE=redis` on all workers so queue state is shared. This supports all `LANGFLOW_EVENT_DELIVERY` modes.


If the deployment is headless and never uses the visual editor or MCP over SSE, you can set `LANGFLOW_DANGEROUSLY_ALLOW_MULTI_WORKER_WITHOUT_SHARED_QUEUE=true` to start anyway. This is unsupported with the Langflow UI and with MCP over SSE, and several subsystems become per-worker. Read [Run multiple workers without Redis](https://docs.langflow.org/deployment-multi-worker#run-multiple-workers-without-redis) before enabling it.


### Builds are cancelled unexpectedly [​](https://docs.langflow.org/troubleshoot#builds-are-cancelled-unexpectedly)


The polling watchdog reclaims builds whose client heartbeat has gone stale. The default threshold is 90 seconds (`LANGFLOW_REDIS_QUEUE_POLLING_STALE_THRESHOLD_S=90`). If legitimate long-running builds are being cancelled, increase this value or set it to `0` to disable the watchdog entirely.


## Voice mode [​](https://docs.langflow.org/troubleshoot#voice-mode)


Voice mode is deprecated as of Langflow 1.10. The Playground microphone now provides speech-to-text only.


For setup, remaining WebSocket endpoints, and current behavior, see [Use voice mode](https://docs.langflow.org/concepts-voice-mode).


## Intel Mac issues [​](https://docs.langflow.org/troubleshoot#intel-mac-issues)


The following issues can occur when running Langflow on Intel-based Macs.


### "No matching distribution found" errors on Intel Mac [​](https://docs.langflow.org/troubleshoot#no-matching-distribution-found-errors-on-intel-mac)


If you see errors about missing packages after installing Langflow on an Intel Mac, such as:


```text
ERROR: Could not find a version that satisfies the requirement torch
ERROR: No matching distribution found for torch
```


This is expected behavior. ML packages such as PyTorch are intentionally excluded on Intel Macs because PyTorch dropped support for macOS x86_64 starting with version 2.3.0.


To verify your architecture and understand which features are available, run:


```bash
python -c "import platform; print(platform.machine())"
# x86_64 = Intel, arm64 = Apple Silicon
```


Use core Langflow features or API-based alternatives instead of local ML models. For details on which features are available and workarounds, see [macOS support](https://docs.langflow.org/macos-support).


### Performance issues on Intel Mac [​](https://docs.langflow.org/troubleshoot#performance-issues-on-intel-mac)


If Langflow feels slow on an Intel Mac:


1. Ensure you are not trying to run ML workloads locally, as these are not supported on Intel Macs.
2. Use API-based providers for embeddings and completions instead of local models.
3. Consider upgrading to Apple Silicon for better performance with ML features.


For more information, see [Workarounds for Intel Mac users](https://docs.langflow.org/macos-support#workarounds-for-intel-mac-users).


## See also [​](https://docs.langflow.org/troubleshoot#see-also)


- [Langflow GitHub Issues and Discussions](https://docs.langflow.org/contributing-github-issues)
- [Langflow telemetry](https://docs.langflow.org/contributing-telemetry)


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)

- [Missing components](https://docs.langflow.org/troubleshoot#missing-components)
- [No input in the Playground](https://docs.langflow.org/troubleshoot#no-input-in-the-playground)
- [Missing key, no key found, or invalid API key](https://docs.langflow.org/troubleshoot#missing-key-no-key-found-or-invalid-api-key)
- [Langflow installation issues](https://docs.langflow.org/troubleshoot#langflow-installation-issues)
  - [Langflow installation freezes at pip dependency resolution](https://docs.langflow.org/troubleshoot#langflow-installation-freezes-at-pip-dependency-resolution)
  - [Linux installation fails to build required package](https://docs.langflow.org/troubleshoot#linux-installation-fails-to-build-required-package)
  - [Installation failure from `webrtcvad` package](https://docs.langflow.org/troubleshoot#installation-failure-from-webrtcvad-package)
  - [`get_body_field` error after installing Langflow](https://docs.langflow.org/troubleshoot#get_body_field-error-after-installing-langflow)- [Langflow Desktop installation issues](https://docs.langflow.org/troubleshoot#langflow-desktop-installation-issues)
  - [Protocol buffers (protoc) required for Intel-based Macs](https://docs.langflow.org/troubleshoot#protocol-buffers-protoc-required-for-intel-based-macs)
  - [Langflow installation failed](https://docs.langflow.org/troubleshoot#langflow-installation-failed)
  - [Langflow startup failed](https://docs.langflow.org/troubleshoot#langflow-startup-failed)
  - [Failed to install uv or unable to find uv](https://docs.langflow.org/troubleshoot#failed-to-install-uv-or-unable-to-find-uv)
  - [Python environment failed](https://docs.langflow.org/troubleshoot#python-environment-failed)
  - [Python environment failed: Python check failed](https://docs.langflow.org/troubleshoot#python-environment-failed-python-check-failed)
  - [Xcode Command Line Tools required](https://docs.langflow.org/troubleshoot#xcode-command-line-tools-required)
  - [C++ build tools required](https://docs.langflow.org/troubleshoot#c-build-tools-required)
  - [Manual UV installation required](https://docs.langflow.org/troubleshoot#manual-uv-installation-required)- [Uninstall Langflow](https://docs.langflow.org/troubleshoot#uninstall-langflow)
  - [Uninstall the Langflow OSS Python package](https://docs.langflow.org/troubleshoot#uninstall-the-langflow-oss-python-package)
  - [Uninstall Langflow Desktop](https://docs.langflow.org/troubleshoot#uninstall-langflow-desktop)- [Langflow startup issues](https://docs.langflow.org/troubleshoot#langflow-startup-issues)
  - [No `langflow.__main__` module](https://docs.langflow.org/troubleshoot#no-langflow__main__-module)
  - [Langflow runTraceback](https://docs.langflow.org/troubleshoot#langflow-runtraceback)
  - [Environment variables not available from terminal](https://docs.langflow.org/troubleshoot#environment-variables-not-available-from-terminal)
  - [Access Langflow Desktop startup logs](https://docs.langflow.org/troubleshoot#access-langflow-desktop-startup-logs)
  - [User not found or inactive when running multiple flows](https://docs.langflow.org/troubleshoot#user-not-found-or-inactive-when-running-multiple-flows)
  - [Package is not installed](https://docs.langflow.org/troubleshoot#package-is-not-installed)
  - [PostgreSQL asyncpg driver compatibility issue](https://docs.langflow.org/troubleshoot#postgresql-asyncpg-driver-compatibility-issue)
  - [PostgreSQL version mismatch: `UNIQUE NULLS DISTINCT` syntax error](https://docs.langflow.org/troubleshoot#postgresql-version-mismatch-unique-nulls-distinct-syntax-error)
  - [An API key must be passed as query or header](https://docs.langflow.org/troubleshoot#an-api-key-must-be-passed-as-query-or-header)
  - [PermissionError on `/app/langflow/secret_key` at startup](https://docs.langflow.org/troubleshoot#permissionerror-on-applangflowsecret_key-at-startup)- [Langflow upgrade issues](https://docs.langflow.org/troubleshoot#langflow-upgrade-issues)
  - [There's a mismatch between the models and the database](https://docs.langflow.org/troubleshoot#theres-a-mismatch-between-the-models-and-the-database)
  - [Langflow Desktop says it is running the latest version, but it is actually behind](https://docs.langflow.org/troubleshoot#langflow-desktop-says-it-is-running-the-latest-version-but-it-is-actually-behind)
  - [422 error when freezing components after upgrading Pydantic/FastAPI dependencies](https://docs.langflow.org/troubleshoot#422-error-when-freezing-components-after-upgrading-pydanticfastapi-dependencies)- [Langflow MCP issues](https://docs.langflow.org/troubleshoot#mcp)
  - [Default project MCP server only works when authentication is None](https://docs.langflow.org/troubleshoot#default-project-mcp-server-only-works-when-authentication-is-none)
  - [Claude for Desktop doesn't use MCP server tools correctly](https://docs.langflow.org/troubleshoot#claude-for-desktop-doesnt-use-mcp-server-tools-correctly)
  - [MCP browser-based flows don't open a browser on Windows](https://docs.langflow.org/troubleshoot#mcp-browser-based-flows-dont-open-a-browser-on-windows)
  - ["No tools or prompts connected" on MCP servers in mixed Windows/WSL environments](https://docs.langflow.org/troubleshoot#no-tools-or-prompts-connected-on-mcp-servers-in-mixed-windowswsl-environments)
  - [MCP Tools component loses Tool Mode option after upgrading flows](https://docs.langflow.org/troubleshoot#mcp-tools-component-loses-tool-mode-option-after-upgrading-flows)- [Token length limit errors in Embedding Model components](https://docs.langflow.org/troubleshoot#token-length-limit-errors-in-embedding-model-components)
- [Document processing errors in Docker containers](https://docs.langflow.org/troubleshoot#document-processing-errors-in-docker-containers)
- [Custom components and integrations issues](https://docs.langflow.org/troubleshoot#custom-components-and-integrations-issues)
  - [Custom components not appearing in the visual editor](https://docs.langflow.org/troubleshoot#custom-components-not-appearing-in-the-visual-editor)- [Multi-worker deployments](https://docs.langflow.org/troubleshoot#multi-worker-deployments)
  - [Workers report `JobQueueNotFoundError`](https://docs.langflow.org/troubleshoot#workers-report-jobqueuenotfounderror)
  - [Redis connection refused or auth errors](https://docs.langflow.org/troubleshoot#redis-connection-refused-or-auth-errors)
  - [Cache and queue keys colliding](https://docs.langflow.org/troubleshoot#cache-and-queue-keys-colliding)
  - [Server refuses to start with multiple workers and `LANGFLOW_JOB_QUEUE_TYPE=asyncio`](https://docs.langflow.org/troubleshoot#server-refuses-to-start-with-multiple-workers-and-langflow_job_queue_typeasyncio)
  - [Builds are cancelled unexpectedly](https://docs.langflow.org/troubleshoot#builds-are-cancelled-unexpectedly)- [Voice mode](https://docs.langflow.org/troubleshoot#voice-mode)
- [Intel Mac issues](https://docs.langflow.org/troubleshoot#intel-mac-issues)
  - ["No matching distribution found" errors on Intel Mac](https://docs.langflow.org/troubleshoot#no-matching-distribution-found-errors-on-intel-mac)
  - [Performance issues on Intel Mac](https://docs.langflow.org/troubleshoot#performance-issues-on-intel-mac)- [See also](https://docs.langflow.org/troubleshoot#see-also)[Manage Privacy Choices](https://docs.langflow.org/troubleshoot#)

---

# API keys and authentication | Langflow Documentation

`https://docs.langflow.org/api-keys-and-authentication`

# API keys and authentication
## Langflow API keys​
## Component API keys​
## Authentication environment variables​
*To generate a secret encryption key for LANGFLOW_SECRET_KEY, do the following:*

*For more information, see Secret Key Rotation in the Langflow Security Policy.*

*When LANGFLOW_NEW_USER_IS_ACTIVE=True, new accounts are automatically activated.*

*For more information, see Docker image defaults.*

*Pair these settings with the SSRF settings to reduce common escape hatches.*

## Configure JWT token signing​
*To explicitly set the algorithm in your .env:*

## Start a Langflow server with authentication enabled​
## See also​







This page documents Langflow's built-in authentication, including user accounts, Langflow API keys, and the environment variables that control access to your server. To connect Langflow to an external identity provider or SSO system, see SSO and external authentication.

Copy page ⌥C Version: 1.12.x On this page

This page documents Langflow's built-in authentication, including user accounts, Langflow API keys, and the environment variables that control access to your server. To connect Langflow to an external identity provider or SSO system, see [SSO and external authentication](https://docs.langflow.org/external-authentication).


Authentication credentials help prevent unauthorized access to your Langflow server, flows, and services connected through components.


There are three types of credentials that you use in Langflow:


- [Langflow API keys](https://docs.langflow.org/api-keys-and-authentication#langflow-api-keys): For authentication with the Langflow API and authorizing server-side Langflow actions like running flows and uploading files.
- [Component API keys](https://docs.langflow.org/api-keys-and-authentication#component-api-keys): For authentication between Langflow and a service connected through a component, such as a model provider or third-party API.
- [Authentication environment variables](https://docs.langflow.org/api-keys-and-authentication#authentication-environment-variables): These environment variables configure how Langflow handles user authentication and authorization.


## Langflow API keys [​](https://docs.langflow.org/api-keys-and-authentication#langflow-api-keys)


You can use Langflow API keys to interact with Langflow programmatically.


By default, most Langflow API endpoints, such as `/v1/run/$FLOW_ID`, require authentication with a Langflow API key.


Langflow validates API keys against keys stored in the database, but you can configure Langflow to validate API keys against an environment variable instead. For more information, see [`LANGFLOW_API_KEY_SOURCE`](https://docs.langflow.org/api-keys-and-authentication#langflow-api-key-source).


Webhook endpoints require API key authentication by default. To disable authentication for webhook endpoints, use the [`LANGFLOW_WEBHOOK_AUTH_ENABLE`](https://docs.langflow.org/webhook#require-authentication-for-webhooks) environment variable. To configure authentication for Langflow MCP servers, see [Use Langflow as an MCP server](https://docs.langflow.org/mcp-server).


### Langflow API key permissions [​](https://docs.langflow.org/api-keys-and-authentication#langflow-api-key-permissions)


A Langflow API key adopts the privileges of the user who created it. This means that API keys you create have the same permissions and access that you do, including access to your flows, components, and Langflow database. A Langflow API key cannot be used to access resources outside of your own Langflow server.


In single-user environments, you are always a superuser, and your Langflow API keys always have superuser privileges.


In multi-user environments, users who aren't superusers cannot use their API keys to access other users' resources. Superusers can only run their own flows, and cannot run flows owned by other users. You must [start your Langflow server with authentication enabled](https://docs.langflow.org/api-keys-and-authentication#start-a-langflow-server-with-authentication-enabled) to allow superusers to manage users and create non-superuser accounts.


### Create a Langflow API key [​](https://docs.langflow.org/api-keys-and-authentication#create-a-langflow-api-key)


You can generate a Langflow API key in your Langflow **Settings** or with the Langflow CLI.


The CLI option is required if your Langflow server is running in `--backend-only` mode.


- Langflow Settings
- Langflow CLI


1. In the Langflow header, click your profile icon, and then select **Settings**.
2. Click **Langflow API Keys**, and then click **Add New**.
3. Name your key, and then click **Create API Key**.
4. Copy the API key and store it securely.


If you're serving your flow with `--backend-only=true`, you can't create API keys in your Langflow **Settings** because the frontend isn't running. In this case, you must create API keys with the Langflow CLI.


1. Recommended: [Start your Langflow server with authentication enabled](https://docs.langflow.org/api-keys-and-authentication#start-a-langflow-server-with-authentication-enabled). The Langflow team recommends enabling authentication for security reasons to prevent unauthorized creation of API keys and superusers, especially in production environments. If authentication isn't enabled (`LANGFLOW_AUTO_LOGIN=True`), all users are effectively superusers, and they can create API keys with the Langflow CLI.
2. Create an API key with [`langflow api-key`](https://docs.langflow.org/configuration-cli#langflow-api-key): ```bash uv run langflow api-key ``` All API keys created with the Langflow CLI have superuser privileges because the command requires superuser authentication, and Langflow API keys adopt the privileges of the user who created them.


### Use a Langflow API key [​](https://docs.langflow.org/api-keys-and-authentication#use-a-langflow-api-key)


To authenticate Langflow API requests, pass your Langflow API key an `x-api-key` header or query parameter.


- HTTP header
- Query parameter


```bash
curl -X POST \
  "http://$LANGFLOW_SERVER_ADDRESS/api/v1/run/$FLOW_ID?stream=false" \
  -H "Content-Type: application/json" \
  -H "x-api-key: $LANGFLOW_API_KEY" \
  -d '{"inputs": {"text":""}, "tweaks": {}}'
```


```bash
curl -X POST \
  "http://$LANGFLOW_SERVER_ADDRESS/api/v1/run/$FLOW_ID?x-api-key=$LANGFLOW_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"inputs": {"text":""}, "tweaks": {}}'
```


For more information about forming Langflow API requests, see [Get started with the Langflow API](https://docs.langflow.org/api-reference-api-examples) and [Trigger flows with the Langflow API](https://docs.langflow.org/concepts-publish).


### Track API key usage [​](https://docs.langflow.org/api-keys-and-authentication#track-api-key-usage)


By default, Langflow tracks API key usage through `total_uses` and `last_used_at` records in your [Langflow database](https://docs.langflow.org/memory).


To disable API key tracking, set `LANGFLOW_DISABLE_TRACK_APIKEY_USAGE=True` in your [Langflow environment variables](https://docs.langflow.org/environment-variables). This can help avoid database contention during periods of high concurrency.


### Revoke an API key [​](https://docs.langflow.org/api-keys-and-authentication#revoke-an-api-key)


To revoke and delete an API key, do the following:


1. In the Langflow header, click your profile icon, and then select **Settings**.
2. Click **Langflow API Keys**.
3. Select the keys you want to delete, and then click **Delete**.


This action immediately invalidates the key and prevents it from being used again.


## Component API keys [​](https://docs.langflow.org/api-keys-and-authentication#component-api-keys)


Component API keys authorize access to external services that are called by components in your flows, such as model providers, databases, or third-party APIs. These aren't Langflow API keys or general application credentials.


In Langflow, you can store component API keys in global variables in your **Settings** or import them from your runtime environment. For more information, see [Global variables](https://docs.langflow.org/configuration-global-variables).


You create and manage component API keys within the service provider's platform. Langflow only stores the encrypted key value or a secure reference to a key stored elsewhere; it doesn't manage the actual credentials at the source. This means that deleting a global variable from Langflow doesn't delete or invalidate the actual API key in the service provider's system. You must delete or rotate component API keys directly using the service provider's interface or API.


For added security, you can set `LANGFLOW_REMOVE_API_KEYS=True` to omit API keys and tokens from flow data in your [Langflow database](https://docs.langflow.org/memory). Additionally, when [exporting flows](https://docs.langflow.org/concepts-flows-import), you can choose to omit API keys from the exported flow JSON.


## Authentication environment variables [​](https://docs.langflow.org/api-keys-and-authentication#authentication-environment-variables)


This section describes the available authentication configuration variables.


You can use the [`.env.example`](https://github.com/langflow-ai/langflow/blob/main/.env.example) file in the Langflow repository as a template for your own `.env` file.


For JWT token signing configuration, including algorithm selection and key management, see [Configure JWT token signing](https://docs.langflow.org/api-keys-and-authentication#configure-jwt-token-signing).


### LANGFLOW_AUTO_LOGIN [​](https://docs.langflow.org/api-keys-and-authentication#langflow-auto-login)


This variable controls whether the visual editor uses automatic login or requires users to sign in.


- If `LANGFLOW_AUTO_LOGIN=False`, automatic login is disabled. Users must sign in to the visual editor, authenticate as a superuser to run certain Langflow CLI commands, and use a Langflow API key for Langflow API requests. You must explicitly set [`LANGFLOW_SUPERUSER_PASSWORD`](https://docs.langflow.org/api-keys-and-authentication#langflow-superuser) before startup. Set [`LANGFLOW_SUPERUSER`](https://docs.langflow.org/api-keys-and-authentication#langflow-superuser) only if you want to override the default superuser username (`langflow`).
- If `LANGFLOW_AUTO_LOGIN=True`, the visual editor automatically signs in all users as the configured superuser, and Langflow uses that username with a configured or generated bootstrap password. All users share the same visual editor environment without password protection, and they can run Langflow CLI commands as superusers. API requests still require a Langflow API key unless you also set [`LANGFLOW_SKIP_AUTH_AUTO_LOGIN`](https://docs.langflow.org/api-keys-and-authentication#langflow-skip-auth-auto-login) to `true`.


The Langflow application default is `True`. Official Langflow Docker images set `false`. For more information, see [Docker image defaults](https://docs.langflow.org/deployment-docker#docker-image-security-defaults).


#### LANGFLOW_SKIP_AUTH_AUTO_LOGIN [​](https://docs.langflow.org/api-keys-and-authentication#langflow-skip-auth-auto-login)


When `LANGFLOW_AUTO_LOGIN=true`, set `LANGFLOW_SKIP_AUTH_AUTO_LOGIN=true` to also skip API key authentication for API requests. The default is `false`, so API keys are still required even when auto-login is enabled. This variable will be removed in a future release.


### LANGFLOW_ENABLE_SUPERUSER_CLI [​](https://docs.langflow.org/api-keys-and-authentication#langflow-enable-superuser-cli)


Controls the availability of the `langflow superuser` command in the Langflow CLI. The default is `true`, but `false` is recommended to prevent unrestricted superuser creation. For more information, see [`langflow superuser`](https://docs.langflow.org/configuration-cli#langflow-superuser).


### LANGFLOW_SUPERUSER and LANGFLOW_SUPERUSER_PASSWORD [​](https://docs.langflow.org/api-keys-and-authentication#langflow-superuser)


These variables specify the username and password for the Langflow server's superuser.


```text
LANGFLOW_SUPERUSER=administrator
LANGFLOW_SUPERUSER_PASSWORD=securepassword
```


`LANGFLOW_SUPERUSER_PASSWORD` is required if `LANGFLOW_AUTO_LOGIN=False`. `LANGFLOW_SUPERUSER` is optional and defaults to `langflow`. `LANGFLOW_SUPERUSER_PASSWORD` can't use the legacy default value `langflow`; startup fails closed instead. When `LANGFLOW_AUTO_LOGIN=True`, `LANGFLOW_SUPERUSER` selects the auto-login account username and `LANGFLOW_SUPERUSER_PASSWORD` is optional. If the password isn't set, Langflow generates an unknown bootstrap password for the auto-login account.


When you [start a Langflow server with authentication enabled](https://docs.langflow.org/api-keys-and-authentication#start-a-langflow-server-with-authentication-enabled), if the required password is *not* set, then startup fails instead of creating a default password. These defaults don't apply when using the Langflow CLI command [`langflow superuser`](https://docs.langflow.org/configuration-cli#langflow-superuser).


### LANGFLOW_SECRET_KEY [​](https://docs.langflow.org/api-keys-and-authentication#langflow-secret-key)


This environment variable stores a secret key used for encrypting sensitive data like API keys and for JWT signing when using the HS256 algorithm. Langflow uses the [Fernet](https://pypi.org/project/cryptography/) library for secret key encryption. For JWT-specific configuration, see [Configure JWT token signing](https://docs.langflow.org/api-keys-and-authentication#configure-jwt-token-signing).


If no secret key is provided, Langflow automatically generates one.


However, you should generate and explicitly set your own key in production environments. This is particularly important for multi-instance deployments like Kubernetes to ensure consistent encryption across instances.


To generate a secret encryption key for `LANGFLOW_SECRET_KEY`, do the following:


1. Run the command to generate and copy a secret to the clipboard. - macOS or Linux - Windows - **macOS**: Generate a secret key and copy it to the clipboard: ```bash python3 -c "from secrets import token_urlsafe; print(f'LANGFLOW_SECRET_KEY={token_urlsafe(32)}')" | pbcopy ``` - **Linux**: Generate a secret key and copy it to the clipboard: ```bash python3 -c "from secrets import token_urlsafe; print(f'LANGFLOW_SECRET_KEY={token_urlsafe(32)}')" | xclip -selection clipboard ``` - **Unix**: Generate a secret key and print it to the terminal to manually copy it: ```bash python3 -c "from secrets import token_urlsafe; print(f'LANGFLOW_SECRET_KEY={token_urlsafe(32)}')" ``` - Generate a secret key and copy it to the clipboard: ```bash python -c "from secrets import token_urlsafe; print(f'LANGFLOW_SECRET_KEY={token_urlsafe(32)}')" ``` - Generate a secret key and print it to the terminal to manually copy it: ```bash # Or just print python -c "from secrets import token_urlsafe; print(f'LANGFLOW_SECRET_KEY={token_urlsafe(32)}')" ```
2. Paste the value into your `.env` file: ```text LANGFLOW_SECRET_KEY=dBuu...2kM2_fb ``` If you're running Langflow on Docker, reference the `LANGFLOW_SECRET_KEY` from your `.env` file in the `docker-compose.yml` file like this: ```yaml environment: - LANGFLOW_SECRET_KEY=${LANGFLOW_SECRET_KEY} ```


#### Rotate the secret key [​](https://docs.langflow.org/api-keys-and-authentication#rotating-the-secret-key)


Rotate `LANGFLOW_SECRET_KEY` if the key might have been compromised and as part of your routine credential management practices. Langflow provides a migration script that re-encrypts stored credentials and other sensitive data with a new key so you can rotate without losing access.


For more information, see [Secret Key Rotation](https://github.com/langflow-ai/langflow/blob/main/SECURITY.md#secret-key-rotation) in the Langflow Security Policy.


### LANGFLOW_NEW_USER_IS_ACTIVE [​](https://docs.langflow.org/api-keys-and-authentication#langflow-new-user-is-active)


When `LANGFLOW_NEW_USER_IS_ACTIVE=False` (default), new accounts are inactive until a superuser activates them with the [Users API](https://docs.langflow.org/api-users). Inactive users cannot sign in to the visual editor. The superuser can also deactivate an account with the same API.


When `LANGFLOW_NEW_USER_IS_ACTIVE=True`, new accounts are automatically activated.


```text
LANGFLOW_NEW_USER_IS_ACTIVE=False
```


Only superusers can manage user accounts for a Langflow server through the [Users API](https://docs.langflow.org/api-users). For more information, see [Start a Langflow server with authentication enabled](https://docs.langflow.org/api-keys-and-authentication#start-a-langflow-server-with-authentication-enabled).


### LANGFLOW_ENABLE_SIGNUP [​](https://docs.langflow.org/api-keys-and-authentication#langflow-enable-signup)


This variable controls whether public self-registration is allowed at the `POST /api/v1/users/` endpoint.


| Value | Description |
| --- | --- |
| `True` (default) | Anyone can create a new Langflow account by calling the registration endpoint directly. |
| `False` | Public registration is disabled. Only superusers can create new accounts with the [Users API](https://docs.langflow.org/api-users). |


Self-registration is always disabled when `LANGFLOW_AUTO_LOGIN=True`, because single-user mode has no multi-account concept. Superusers can create accounts regardless of this setting.


### LANGFLOW_API_KEY_SOURCE [​](https://docs.langflow.org/api-keys-and-authentication#langflow-api-key-source)


This variable controls how Langflow validates API keys.


| Value | Description |
| --- | --- |
| `db` (default) | Validates API keys against [Langflow API keys](https://docs.langflow.org/api-keys-and-authentication#langflow-api-keys) stored in the database. This is the standard behavior where users create and manage API keys through the Langflow UI or CLI. |
| `env` | Validates API keys against the `LANGFLOW_​API_​KEY` environment variable. Useful for Kubernetes deployments, CI/CD pipelines, or any environment where you want to inject a pre-defined API key without database configuration. |


By default, Langflow validates the `x-api-key` header against the Langflow database with `LANGFLOW_API_KEY_SOURCE=db`. When using database-based validation, you can create multiple keys with per-user permissions, track usage, and manage keys through the Langflow UI or CLI.


When `LANGFLOW_API_KEY_SOURCE=env`, Langflow validates the `x-api-key` header against the value of the `LANGFLOW_API_KEY` environment variable. This means Langflow runs securely in stateless environments, such as with LFX or Kubernetes secrets.


When `LANGFLOW_API_KEY_SOURCE=env`, only a single API key can be used for the deployment. All authenticated requests use the same API key, and successful authentication grants superuser privileges. This mode is designed for single-tenant deployments or automated systems, not multi-user environments where different users need different access levels. To rotate your keys, update the environment variable and restart the Langflow server.


To enable environment-based API key validation:


1. In the Langflow `.env` file, set the API key source to `env`: ```text LANGFLOW_API_KEY_SOURCE=env ```
2. In the Langflow `.env` file, set the API key value: ```text LANGFLOW_API_KEY=your-secure-api-key ```
3. Use the API key in your requests: ```bash curl -X POST \ "http://LANGFLOW_SERVER_ADDRESS/api/v1/run/FLOW_ID?stream=false" \ -H "Content-Type: application/json" \ -H "x-api-key: LANGFLOW_API_KEY" \ -d '{"inputs": {"text":""}, "tweaks": {}}' ``` Replace `LANGFLOW_SERVER_ADDRESS`, `FLOW_ID`, and `LANGFLOW_API_KEY` with the values from your deployment.


### LANGFLOW_CORS_* [​](https://docs.langflow.org/api-keys-and-authentication#cors-configuration-for-authentication)


Cross-Origin Resource Sharing (CORS) configuration controls how authentication credentials are handled when your Langflow frontend and backend are served from different origins. The following `LANGFLOW_CORS_*` environment variables are available:


| Variable | Format | Default | Description |
| --- | --- | --- | --- |
| `LANGFLOW_​CORS_​ALLOW_​CREDENTIALS` | Boolean | `True` | Whether to allow credentials, such as cookies and authorization headers, in CORS requests. |
| `LANGFLOW_​CORS_​ALLOW_​HEADERS` | List[String] or String | `*` | The allowed headers for CORS requests. Provide a comma-separated list of headers or use `*` to allow all headers. |
| `LANGFLOW_​CORS_​ALLOW_​METHODS` | List[String] or String | `*` | The allowed HTTP methods for CORS requests. Provide a comma-separated list of methods or use `*` to allow all methods. |
| `LANGFLOW_​CORS_​ORIGINS` | String | `*` | The allowed CORS origins. Provide a comma-separated list of origins or use `*` for all origins. |


The default configuration enables CORS credentials and uses wildcards (`*`) to allow all origins, headers, and methods:


```text
LANGFLOW_CORS_ORIGINS=*
LANGFLOW_CORS_ALLOW_CREDENTIALS=True
LANGFLOW_CORS_ALLOW_HEADERS=*
LANGFLOW_CORS_ALLOW_METHODS=*
```


### LANGFLOW_ACCESS_* and LANGFLOW_REFRESH_* [​](https://docs.langflow.org/api-keys-and-authentication#session-cookie-hardening)


For a shared or public deployment served over HTTPS, harden the session cookies. `Secure` and `SameSite` default to values that support local HTTP development. Both the access and refresh cookies are `HttpOnly` by default; the browser sends them automatically with requests.


Set both `LANGFLOW_ACCESS_SECURE` and `LANGFLOW_REFRESH_SECURE` to `True` for HTTPS deployments. Cross-site HTTPS deployments must also set `LANGFLOW_REFRESH_SAME_SITE=none`.


| Variable | Format | Default | Description |
| --- | --- | --- | --- |
| `LANGFLOW_​ACCESS_​SECURE` | Boolean | `False` | When `true`, the `access_​token_​lf` cookie is sent only over HTTPS. Recommended `true` for any HTTPS deployment. |
| `LANGFLOW_​ACCESS_​HTTPONLY` | Boolean | `True` | When `true`, the `access_​token_​lf` cookie is not readable by JavaScript. Set to `false` only if a client must read this cookie in JavaScript. |
| `LANGFLOW_​ACCESS_​SAME_​SITE` | String | `lax` | The `SameSite` attribute of the access-token cookie (`lax`, `strict`, or `none`). |
| `LANGFLOW_​REFRESH_​SECURE` | Boolean | `False` | When `true`, the `refresh_​token_​lf` cookie is sent only over HTTPS. Set this to `true` for any HTTPS deployment. |
| `LANGFLOW_​REFRESH_​HTTPONLY` | Boolean | `True` | When `true`, the `refresh_​token_​lf` cookie is not readable by JavaScript. |
| `LANGFLOW_​REFRESH_​SAME_​SITE` | String | `lax` | The `SameSite` attribute of the refresh-token cookie (`lax`, `strict`, or `none`). |
| `LANGFLOW_​COOKIE_​DOMAIN` | String | Not set | Domain attribute for the access and refresh cookies. Leave unset for host-only cookies. Set to a parent domain, such as `.example.com`, when the frontend and API are on different subdomains. |


### Anonymous public-flow authorization [​](https://docs.langflow.org/api-keys-and-authentication#anonymous-public-flow-authorization)


Anonymous public-flow links are direct-link capabilities, not discovery grants. Langflow accepts a canonical `PUBLIC` authorization share and preserves existing links derived from `Flow.access_type=PUBLIC` or an A2A folder with `auth_type=none`. Public shares never appear in general flow or shared-with-me listings.


A canonical `PUBLIC` share takes precedence over both compatibility grants. For flows, the shares API accepts only `permission_level=execute` at `PUBLIC` scope; execution includes the scrubbed direct-link read needed to load the playground. The API rejects `read`, `write`, and `admin` because there is no read-only, writable, or administrative anonymous flow surface. Deleting the share row removes the canonical grant and any still-set legacy setting becomes the effective grant again, so revoke access entirely by clearing the legacy setting as well.


An anonymous link grants only resource read and flow execution. It never grants create, write, delete, deploy, or administration actions, and callers cannot submit flow data or component tweaks. Public execution uses a stable non-user principal, so owner credentials, variables, files, and knowledge bases are unavailable unless a dependency has its own public authorization path. Errors are sanitized, and A2A HITL resumes recheck the current grant. Revocation blocks subsequent starts and resumes; it does not terminate work that is already running.


When `LANGFLOW_AUTHZ_ENABLED=true`, anonymous access also requires an authorization plugin that opts into public principals, maps request hosts through a deployment-owned allowlist, resolves a tenant from that mapping and server-derived domain context, and allows the action. The OSS public-principal plugin seam defaults to deny and never performs cross-tenant discovery. Plugins must not treat the raw `Host` header as a trusted tenant identity.


For A2A, `auth_type=none` applies this contract to both the direct agent card and execution routes. API-key and OAuth agent cards remain anonymously readable by direct link for A2A protocol discovery, but their JSON-RPC execution routes retain owner-key admission and owner execution.


### LANGFLOW_RATE_LIMIT_* [​](https://docs.langflow.org/api-keys-and-authentication#login-rate-limiting)


The following environment variables configure IP-based rate limiting to protect against brute-force attacks on the `/login` endpoint and abuse of public flow endpoints. When the limit is exceeded, Langflow returns HTTP 429 with a `Retry-After: 60` header.


| Variable | Format | Default | Description |
| --- | --- | --- | --- |
| `LANGFLOW_​RATE_​LIMIT_​ENABLED` | Boolean | `True` | Enable rate limiting on the `/login` and `/api/v2/workflows/public` endpoints. Set to False to disable those limits (not recommended in production). |
| `LANGFLOW_​RATE_​LIMIT_​PER_​MINUTE` | Integer | `5` | Maximum number of login attempts allowed per minute from a single IP address. |
| `LANGFLOW_​RATE_​LIMIT_​STORAGE_​URI` | String | `memory://` | Storage backend for rate limit counters. Use `memory://` for single-server deployments or `redis://host:port` for multi-server deployments where the limit should be shared across instances. |
| `LANGFLOW_​RATE_​LIMIT_​TRUST_​PROXY` | Boolean | `False` | When `true`, Langflow reads the client IP from the rightmost `X-Forwarded-For` header entry instead of the direct connection IP. Enable only when Langflow is behind a trusted reverse proxy or load balancer. Do not enable if users can reach Langflow directly, as this allows header spoofing. |
| `LANGFLOW_​PUBLIC_​FLOW_​RATE_​LIMIT_​PER_​MINUTE` | Integer | `20` | Maximum number of unauthenticated public-flow runs allowed per minute from a single IP address. Public flows consume resources under an isolated anonymous principal, so they are rate-limited separately from the `/login` endpoint. |


### LANGFLOW_SSRF_* and LANGFLOW_CONNECTOR_SSRF_* [​](https://docs.langflow.org/api-keys-and-authentication#ssrf-protection)


The following environment variables configure Server-Side Request Forgery (SSRF) protection for the [**API Request** component](https://docs.langflow.org/api-request) and for connector components that take a tenant-controlled host or URL. SSRF protection prevents requests to internal or private network resources, such as private IP ranges, loopback addresses, and cloud metadata endpoints.


In a shared server where users you do not fully trust can build flows, set `LANGFLOW_CONNECTOR_SSRF_VALIDATION_ENABLED=true`, `LANGFLOW_SSRF_PROTECTION_ENABLED=true`, and `LANGFLOW_CONNECTOR_SSRF_ALLOW_LOOPBACK=false`, and then allowlist your own internal hosts with `LANGFLOW_SSRF_ALLOWED_HOSTS`.


| Variable | Format | Default | Description |
| --- | --- | --- | --- |
| `LANGFLOW_​SSRF_​PROTECTION_​ENABLED` | Boolean | `True` | Enable SSRF protection for the **API Request** component. When enabled, the component blocks requests to private IP addresses. When disabled, requests are not blocked. |
| `LANGFLOW_​SSRF_​ALLOWED_​HOSTS` | List[String] | Not set | A comma-separated list of allowed hosts, IP addresses, or CIDR ranges that can bypass SSRF protection checks. For example: `192.168.1.0/24,10.0.0.5,*.internal.company.local`. |
| `LANGFLOW_​CONNECTOR_​SSRF_​VALIDATION_​ENABLED` | Boolean | `True` | Apply SSRF host validation to connector components that take a tenant-controlled host or URL. Uses `LANGFLOW_​SSRF_​PROTECTION_​ENABLED` and `LANGFLOW_​SSRF_​ALLOWED_​HOSTS` for the host policy. Set to `false`, or allowlist specific hosts, only when a trusted single-tenant deployment intentionally connects to private-network services. |
| `LANGFLOW_​CONNECTOR_​SSRF_​ALLOW_​LOOPBACK` | Boolean | `True` | When connector SSRF validation is enabled, allow literal loopback hosts (`localhost`, `127.0.0.0/8`, `::1`) so local Ollama, LM Studio, and similar services keep working. Multi-tenant deployments where a tenant must not reach the server's loopback should set this to `false`. |


### Component hardening for untrusted users [​](https://docs.langflow.org/api-keys-and-authentication#multi-tenant-component-hardening)


Use these variables when users who can build or run flows on your server should not get host-level code execution, arbitrary file reads, or MCP mounts.


For more information, see [Docker image defaults](https://docs.langflow.org/deployment-docker#docker-image-security-defaults).


| Variable | Format | Default | Description |
| --- | --- | --- | --- |
| `LANGFLOW_​BLOCK_​CODE_​INTERPRETER_​COMPONENTS` | Boolean | `False` | When `true`, blocks execution of any flow containing a built-in arbitrary-code-execution component, including the [**Python Interpreter**](https://docs.langflow.org/python-interpreter), Python REPL/Code tools, [**Smart Transform**](https://docs.langflow.org/smart-transform), [**CSV Agent**](https://docs.langflow.org/bundles-langchain#csv-agent), and code-running agents such as [**CodeAct**](https://docs.langflow.org/bundles-codeagents#codeact-agent-smolagents), [**CUGA**](https://docs.langflow.org/bundles-cuga), and [**OpenDsStar**](https://docs.langflow.org/bundles-codeagents#opendstar-agent). |
| `LANGFLOW_​RESTRICT_​LOCAL_​FILE_​ACCESS` | Boolean | `False` | When `true`, built-in file-reading components, including the [**File**](https://docs.langflow.org/read-file), [**Directory**](https://docs.langflow.org/legacy-core-components#legacy-data-components), [**JSON/CSV-to-Data**](https://docs.langflow.org/legacy-core-components#legacy-data-components), and the [**CSV Agent**](https://docs.langflow.org/bundles-langchain#csv-agent), [**JSON Agent**](https://docs.langflow.org/bundles-langchain#legacy-langchain-components), and [**OpenAPI Agent**](https://docs.langflow.org/bundles-langchain#openapi-agent) can only read and write paths inside the [`LANGFLOW_​CONFIG_​DIR`](https://docs.langflow.org/memory) storage directory. This also blocks `sqlite` and `duckdb` dialects in the [**SQL Database**](https://docs.langflow.org/sql-database) components and local-filesystem Git clones. |
| `LANGFLOW_​MCP_​SERVER_​DOCKER_​HARDENING` | Boolean | `False` | When `true`, applies a strict Docker-argument policy to MCP stdio servers that use the `docker` transport. Rejects host filesystem or device mounts, `host/another-container` namespaces, non-default networks, privilege flags, and sandbox-disabling `--security-opt` values. Forms such as `--network none` / `bridge` and `--security-opt no-new-privileges` remain allowed. |
| `LANGFLOW_​TWEAKS_​POLICY` | String | `permissive` | Which component fields a run request may set through `tweaks`. For more information, see [Restrict API tweaks](https://docs.langflow.org/deployment-tweaks-policy). |


Enable these flags when untrusted users can build flows on this server.


The `LANGFLOW_ALLOW_CUSTOM_COMPONENTS` and `LANGFLOW_BLOCK_CODE_INTERPRETER_COMPONENTS` flags support two deployment modes. `LANGFLOW_ALLOW_CUSTOM_COMPONENTS=false` blocks user-authored component code and registered built-in code-execution components at runtime. Set `LANGFLOW_BLOCK_CODE_INTERPRETER_COMPONENTS=true` independently when custom components should remain enabled but built-in code execution should be disabled.


To enable these flags, set the following:


- `LANGFLOW_ALLOW_CUSTOM_COMPONENTS=false`: blocks user-authored component code and registered built-in code-execution components. See [Block custom components](https://docs.langflow.org/deployment-block-custom-components).
- `LANGFLOW_BLOCK_CODE_INTERPRETER_COMPONENTS=true`: blocks built-in code-execution components.
- `LANGFLOW_RESTRICT_LOCAL_FILE_ACCESS=true`: confines built-in file access to the upload sandbox.
- `LANGFLOW_MCP_SERVER_DOCKER_HARDENING=true`: tightens Docker MCP server arguments.
- `LANGFLOW_TWEAKS_POLICY=declared` or `off`: limits which component fields an API caller can override at run time. See [Restrict API tweaks](https://docs.langflow.org/deployment-tweaks-policy).


To block named built-in components, starter templates, model providers, or models across the install, use the [catalog and model policy APIs](https://docs.langflow.org/api-governance-policy).


Pair these settings with the [SSRF settings](https://docs.langflow.org/api-keys-and-authentication#ssrf-protection) to reduce common escape hatches.


These settings **do not** provide full user isolation. For more information, see [Security](https://docs.langflow.org/security).


### LANGFLOW_WEBHOOK_AUTH_ENABLE [​](https://docs.langflow.org/api-keys-and-authentication#langflow-webhook-auth-enable)


This variable controls whether API key authentication is required for webhook endpoints.


| Variable | Format | Default | Description |
| --- | --- | --- | --- |
| `LANGFLOW_​WEBHOOK_​AUTH_​ENABLE` | Boolean | `True` | When `True`, webhook endpoints require API key authentication and validate that the authenticated user owns the flow being executed. When `False`, no Langflow API key is required and all requests to the webhook endpoint are treated as being sent by the flow owner. |


By default, webhooks require API key authentication with `LANGFLOW_WEBHOOK_AUTH_ENABLE=True`.


To allow webhooks to run without authentication (not recommended; use only in trusted environments), in your Langflow `.env` file, set `LANGFLOW_WEBHOOK_AUTH_ENABLE=False`.


When webhook authentication is enabled, you must provide a Langflow API key with each webhook request as an HTTP header or query parameter. For more information, see [Require authentication for webhooks](https://docs.langflow.org/webhook#require-authentication-for-webhooks).


## Configure JWT token signing [​](https://docs.langflow.org/api-keys-and-authentication#configure-jwt-token-signing)


Langflow issues short-lived JSON Web Tokens (JWTs) when a user logs in. The default HS256 algorithm works for most deployments. Switch to RS256 or RS512 for production deployments that require asymmetric keys or need to share the public key with other services.


The following environment variables control JWT signing. `LANGFLOW_SECRET_KEY` is also used for data encryption and is documented separately in [`LANGFLOW_SECRET_KEY`](https://docs.langflow.org/api-keys-and-authentication#langflow-secret-key).


| Variable | Description | Default |
| --- | --- | --- |
| `LANGFLOW_​ALGORITHM` | JWT signing algorithm: `HS256`, `RS256`, or `RS512` | `HS256` |
| `LANGFLOW_​PRIVATE_​KEY` | RSA private key for RS256/RS512 signing | Auto-generated |
| `LANGFLOW_​PUBLIC_​KEY` | RSA public key for RS256/RS512 verification | Derived from private key |
| `LANGFLOW_​ACCESS_​TOKEN_​EXPIRE_​SECONDS` | Access token expiration time | `3600` (1 hour) |
| `LANGFLOW_​REFRESH_​TOKEN_​EXPIRE_​SECONDS` | Refresh token expiration time | `604800` (7 days) |


### HS256 (default) [​](https://docs.langflow.org/api-keys-and-authentication#hs256-default)


HS256 is the default JWT algorithm, suitable for single-server deployments. Langflow automatically generates and persists a secret key via `LANGFLOW_SECRET_KEY`. No configuration is necessary beyond what is already covered in the [`LANGFLOW_SECRET_KEY`](https://docs.langflow.org/api-keys-and-authentication#langflow-secret-key) section above.


To explicitly set the algorithm in your `.env`:


```bash
LANGFLOW_ALGORITHM=HS256
LANGFLOW_SECRET_KEY="your-custom-secret-key"
```


### RS256 [​](https://docs.langflow.org/api-keys-and-authentication#rs256)


RS256 uses an RSA private/public key pair. The private key signs tokens; the public key verifies them. Use RS256 for production deployments or multi-instance setups where you want to share the public key with other services.


To automatically generate a key pair, set the algorithm and Langflow creates and persists the keys in [`LANGFLOW_CONFIG_DIR`](https://docs.langflow.org/logging) on startup:


```bash
LANGFLOW_ALGORITHM=RS256
```


To supply your own private key (public key is derived automatically):


```bash
LANGFLOW_ALGORITHM=RS256
LANGFLOW_PRIVATE_KEY="-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEF...
-----END PRIVATE KEY-----"
```


To supply a full key pair:


```bash
LANGFLOW_ALGORITHM=RS256
LANGFLOW_PRIVATE_KEY="-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEF...
-----END PRIVATE KEY-----"
LANGFLOW_PUBLIC_KEY="-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOC...
-----END PUBLIC KEY-----"
```


To generate an RSA key pair manually:


1. Generate a 2048-bit private key: ```bash openssl genrsa -out private_key.pem 2048 ```
2. Extract the public key: ```bash openssl rsa -in private_key.pem -pubout -out public_key.pem ```


### RS512 [​](https://docs.langflow.org/api-keys-and-authentication#rs512)


RS512 uses the same RSA key format as RS256 but with SHA-512 hashing for greater cryptographic strength. Key generation and configuration follow the same pattern as RS256 — substitute `RS512` for `RS256` in all the examples above.


### Configure Docker and Kubernetes deployments [​](https://docs.langflow.org/api-keys-and-authentication#configure-docker-and-kubernetes-deployments)


**Docker with HS256** — for single-server or development deployments:


```yaml
services:
  langflow:
    image: langflowai/langflow:latest
    environment:
      - LANGFLOW_ALGORITHM=HS256
      - LANGFLOW_SECRET_KEY=${LANGFLOW_SECRET_KEY}
    volumes:
      - langflow_data:/app/langflow
volumes:
  langflow_data:
```


**Docker with RS256** — auto-generated keys (persisted in the volume):


```yaml
services:
  langflow:
    image: langflowai/langflow:latest
    environment:
      - LANGFLOW_ALGORITHM=RS256
    volumes:
      - langflow_data:/app/langflow
volumes:
  langflow_data:
```


**Docker with RS256** — mount an existing key pair:


```yaml
services:
  langflow:
    image: langflowai/langflow:latest
    environment:
      - LANGFLOW_ALGORITHM=RS256
    volumes:
      - ./keys/private_key.pem:/app/langflow/private_key.pem:ro
      - ./keys/public_key.pem:/app/langflow/public_key.pem:ro
      - langflow_data:/app/langflow
volumes:
  langflow_data:
```


**Kubernetes with RS256** — store keys as Secrets:


```yaml
# jwt-secret.yaml
apiVersion: v1
kind: Secret
metadata:
  name: langflow-jwt-keys
type: Opaque
stringData:
  algorithm: "RS256"
  private-key: |
    -----BEGIN PRIVATE KEY-----
    MIIEvgIBADANBgkqhkiG9w0BAQEF...
    -----END PRIVATE KEY-----
  public-key: |
    -----BEGIN PUBLIC KEY-----
    MIIBIjANBgkqhkiG9w0BAQEFAAOC...
    -----END PUBLIC KEY-----
---
# langflow-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: langflow
spec:
  template:
    spec:
      containers:
        - name: langflow
          image: langflowai/langflow:latest
          env:
            - name: LANGFLOW_ALGORITHM
              valueFrom:
                secretKeyRef:
                  name: langflow-jwt-keys
                  key: algorithm
            - name: LANGFLOW_PRIVATE_KEY
              valueFrom:
                secretKeyRef:
                  name: langflow-jwt-keys
                  key: private-key
            - name: LANGFLOW_PUBLIC_KEY
              valueFrom:
                secretKeyRef:
                  name: langflow-jwt-keys
                  key: public-key
```


### Configure token expiration [​](https://docs.langflow.org/api-keys-and-authentication#configure-token-expiration)


Access tokens authenticate API requests and typically expire within 15 minutes to 1 hour. Refresh tokens obtain new access tokens without requiring the user to log in again and typically expire within 7 to 30 days. When an access token expires, the client can use the refresh token to get a new one from `/api/v1/refresh`.


```bash
LANGFLOW_ACCESS_TOKEN_EXPIRE_SECONDS=3600    # 1 hour
LANGFLOW_REFRESH_TOKEN_EXPIRE_SECONDS=604800 # 7 days
```


## Start a Langflow server with authentication enabled [​](https://docs.langflow.org/api-keys-and-authentication#start-a-langflow-server-with-authentication-enabled)


This section shows you how to use the [authentication environment variables](https://docs.langflow.org/api-keys-and-authentication#authentication-environment-variables) to deploy a Langflow server with authentication enabled. This involves disabling automatic login, setting superuser credentials, and generating a secret encryption key.


This configuration is recommended for any deployment where Langflow is exposed to a shared or public network, or where multiple users access the same Langflow server.


With authentication enabled, all users must sign in to the visual editor with valid credentials, and API requests require authentication with a Langflow API key. Sign in as a superuser to [create a Langflow API key](https://docs.langflow.org/api-keys-and-authentication#create-a-langflow-api-key) with superuser privileges. User management is through the [Users API](https://docs.langflow.org/api-users), not the visual editor.


### Start the Langflow server [​](https://docs.langflow.org/api-keys-and-authentication#start-the-langflow-server)


1. Create a `.env` file with the following variables: ```text LANGFLOW_AUTO_LOGIN=False LANGFLOW_SUPERUSER= LANGFLOW_SUPERUSER_PASSWORD= LANGFLOW_SECRET_KEY= LANGFLOW_NEW_USER_IS_ACTIVE=False LANGFLOW_ENABLE_SIGNUP=False LANGFLOW_ENABLE_SUPERUSER_CLI=False ``` Your `.env` file can have other environment variables. This example focuses on authentication variables. `LANGFLOW_ENABLE_SIGNUP=False` restricts account creation to superusers. `LANGFLOW_NEW_USER_IS_ACTIVE=False` keeps new accounts inactive until you activate them with the Users API.
2. Set `LANGFLOW_SUPERUSER_PASSWORD` to your desired superuser password. Optionally set `LANGFLOW_SUPERUSER` to override the default `langflow` username. For a one-time test, you can use basic credentials like `administrator` and `password`. Strong, securely-stored credentials are recommended in genuine development and production environments.
3. Recommended: Generate and set a `LANGFLOW_SECRET_KEY` for encrypting sensitive data. If you don't set a secret key, Langflow generates one automatically, but this isn't recommended for production environments. For instructions on generating and setting a secret key, see [`LANGFLOW_SECRET_KEY`](https://docs.langflow.org/api-keys-and-authentication#langflow-secret-key).
4. Save your `.env` file with the populated variables. For example: ```text LANGFLOW_AUTO_LOGIN=False LANGFLOW_SUPERUSER=administrator LANGFLOW_SUPERUSER_PASSWORD=securepassword LANGFLOW_SECRET_KEY=dBuu...2kM2_fb LANGFLOW_NEW_USER_IS_ACTIVE=False LANGFLOW_ENABLE_SIGNUP=False LANGFLOW_ENABLE_SUPERUSER_CLI=False ```
5. Start Langflow with the configuration from your `.env` file: ```text uv run langflow run --env-file .env ``` Starting Langflow with this `.env` file creates or uses the configured superuser. If `LANGFLOW_SUPERUSER_PASSWORD` isn't set, startup fails instead of creating a default password.
6. Verify the server is running. The default location is `http://localhost:7860`.


Next, add users with the Users API so they can collaborate on flows.


### Manage users as an administrator [​](https://docs.langflow.org/api-keys-and-authentication#manage-users-as-an-administrator)


As of Langflow 1.12, Langflow OSS has no **Admin Page** in the visual editor. Superusers add, activate, list, and delete users, set **Superuser**, and set other users' passwords with `PATCH /api/v1/users/{id}`. For more information, see [Users endpoints](https://docs.langflow.org/api-users).


1. To complete your first-time login as a superuser, navigate to `http://localhost:7860/login`. If you aren't using the default location, replace `localhost:7860` with your server's address.
2. Log in with the password you set in `LANGFLOW_SUPERUSER_PASSWORD` and the username from `LANGFLOW_SUPERUSER`. If you did not set `LANGFLOW_SUPERUSER`, the username is `langflow`.
3. [Create a Langflow API key](https://docs.langflow.org/api-keys-and-authentication#create-a-langflow-api-key) while signed in as the superuser. User-management requests require a Langflow API key in the `x-api-key` header.
4. Create a user: - Python - TypeScript - curl ```python import os import requests base = os.environ["LANGFLOW_URL"] headers = { "Content-Type": "application/json", "x-api-key": os.environ["LANGFLOW_API_KEY"], } payload = { "username": "newuser", "password": "securepassword123", } response = requests.post(f"{base}/api/v1/users/", headers=headers, json=payload, timeout=30) response.raise_for_status() print(response.json()) ``` ```ts const url = `${process.env.LANGFLOW_URL}/api/v1/users/`; const response = await fetch(url, { method: "POST", headers: { "Content-Type": "application/json", "x-api-key": process.env.LANGFLOW_API_KEY!, }, body: JSON.stringify({ username: "newuser", password: "securepassword123", }), }); if (!response.ok) { throw new Error(`HTTP ${response.status}`); } console.log(await response.json()); ``` ```bash curl -X POST \ "$LANGFLOW_URL/api/v1/users/" \ -H "Content-Type: application/json" \ -H "x-api-key: $LANGFLOW_API_KEY" \ -d '{ "username": "newuser", "password": "securepassword123" }' ``` The response includes the user's `id`. New accounts are inactive when `LANGFLOW_NEW_USER_IS_ACTIVE=False` (the default, and the value in the `.env` example above).
5. Activate the account so the user can sign in. Replace `USER_ID` with the `id` from the create response: - Python - TypeScript - curl ```python import os import requests base = os.environ["LANGFLOW_URL"] user_id = "USER_ID" headers = { "Content-Type": "application/json", "x-api-key": os.environ["LANGFLOW_API_KEY"], } payload = {"is_active": True} response = requests.patch( f"{base}/api/v1/users/{user_id}", headers=headers, json=payload, timeout=30 ) response.raise_for_status() print(response.json()) ``` ```ts const userId = "USER_ID"; const url = `${process.env.LANGFLOW_URL}/api/v1/users/${userId}`; const response = await fetch(url, { method: "PATCH", headers: { "Content-Type": "application/json", "x-api-key": process.env.LANGFLOW_API_KEY!, }, body: JSON.stringify({ is_active: true }), }); if (!response.ok) { throw new Error(`HTTP ${response.status}`); } console.log(await response.json()); ``` ```bash curl -X PATCH \ "$LANGFLOW_URL/api/v1/users/USER_ID" \ -H "Content-Type: application/json" \ -H "x-api-key: $LANGFLOW_API_KEY" \ -d '{ "is_active": true }' ``` To grant administrative privileges, include `"is_superuser": true` in the same request. To reset another user's password, `PATCH /api/v1/users/{id}` with `"password": "<new password>"`. That path does not require the current password. `PATCH /api/v1/users/{id}/reset-password` is self-service: it must be called as that user and requires `current_password`. See [Update user](https://docs.langflow.org/api-users#update-user). To list, deactivate, or delete a user, see [Users endpoints](https://docs.langflow.org/api-users).
6. Send the username and password to the user. The superuser sets the initial password when creating the account.
7. To test the new user's access, sign out of Langflow, and then sign in at `/login` with the new user's credentials. A non-superuser can use the visual editor and cannot call the Users API to manage other accounts.


## See also [​](https://docs.langflow.org/api-keys-and-authentication#see-also)


- [Langflow environment variables](https://docs.langflow.org/environment-variables)
- [Users endpoints](https://docs.langflow.org/api-users)
- [Langflow Security Policy](https://github.com/langflow-ai/langflow/blob/main/SECURITY.md) — reporting vulnerabilities, security configuration, and [secret key rotation](https://github.com/langflow-ai/langflow/blob/main/SECURITY.md#secret-key-rotation)


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)

- [Langflow API keys](https://docs.langflow.org/api-keys-and-authentication#langflow-api-keys)
  - [Langflow API key permissions](https://docs.langflow.org/api-keys-and-authentication#langflow-api-key-permissions)
  - [Create a Langflow API key](https://docs.langflow.org/api-keys-and-authentication#create-a-langflow-api-key)
  - [Use a Langflow API key](https://docs.langflow.org/api-keys-and-authentication#use-a-langflow-api-key)
  - [Track API key usage](https://docs.langflow.org/api-keys-and-authentication#track-api-key-usage)
  - [Revoke an API key](https://docs.langflow.org/api-keys-and-authentication#revoke-an-api-key)- [Component API keys](https://docs.langflow.org/api-keys-and-authentication#component-api-keys)
- [Authentication environment variables](https://docs.langflow.org/api-keys-and-authentication#authentication-environment-variables)
  - [LANGFLOW_AUTO_LOGIN](https://docs.langflow.org/api-keys-and-authentication#langflow-auto-login)
  - [LANGFLOW_ENABLE_SUPERUSER_CLI](https://docs.langflow.org/api-keys-and-authentication#langflow-enable-superuser-cli)
  - [LANGFLOW_SUPERUSER and LANGFLOW_SUPERUSER_PASSWORD](https://docs.langflow.org/api-keys-and-authentication#langflow-superuser)
  - [LANGFLOW_SECRET_KEY](https://docs.langflow.org/api-keys-and-authentication#langflow-secret-key)
  - [LANGFLOW_NEW_USER_IS_ACTIVE](https://docs.langflow.org/api-keys-and-authentication#langflow-new-user-is-active)
  - [LANGFLOW_ENABLE_SIGNUP](https://docs.langflow.org/api-keys-and-authentication#langflow-enable-signup)
  - [LANGFLOW_API_KEY_SOURCE](https://docs.langflow.org/api-keys-and-authentication#langflow-api-key-source)
  - [LANGFLOW_CORS_*](https://docs.langflow.org/api-keys-and-authentication#cors-configuration-for-authentication)
  - [LANGFLOW_ACCESS_* and LANGFLOW_REFRESH_*](https://docs.langflow.org/api-keys-and-authentication#session-cookie-hardening)
  - [Anonymous public-flow authorization](https://docs.langflow.org/api-keys-and-authentication#anonymous-public-flow-authorization)
  - [LANGFLOW_RATE_LIMIT_*](https://docs.langflow.org/api-keys-and-authentication#login-rate-limiting)
  - [LANGFLOW_SSRF_* and LANGFLOW_CONNECTOR_SSRF_*](https://docs.langflow.org/api-keys-and-authentication#ssrf-protection)
  - [Component hardening for untrusted users](https://docs.langflow.org/api-keys-and-authentication#multi-tenant-component-hardening)
  - [LANGFLOW_WEBHOOK_AUTH_ENABLE](https://docs.langflow.org/api-keys-and-authentication#langflow-webhook-auth-enable)- [Configure JWT token signing](https://docs.langflow.org/api-keys-and-authentication#configure-jwt-token-signing)
  - [HS256 (default)](https://docs.langflow.org/api-keys-and-authentication#hs256-default)
  - [RS256](https://docs.langflow.org/api-keys-and-authentication#rs256)
  - [RS512](https://docs.langflow.org/api-keys-and-authentication#rs512)
  - [Configure Docker and Kubernetes deployments](https://docs.langflow.org/api-keys-and-authentication#configure-docker-and-kubernetes-deployments)
  - [Configure token expiration](https://docs.langflow.org/api-keys-and-authentication#configure-token-expiration)- [Start a Langflow server with authentication enabled](https://docs.langflow.org/api-keys-and-authentication#start-a-langflow-server-with-authentication-enabled)
  - [Start the Langflow server](https://docs.langflow.org/api-keys-and-authentication#start-the-langflow-server)
  - [Manage users as an administrator](https://docs.langflow.org/api-keys-and-authentication#manage-users-as-an-administrator)- [See also](https://docs.langflow.org/api-keys-and-authentication#see-also)[Manage Privacy Choices](https://docs.langflow.org/api-keys-and-authentication#)

---

# URL | Langflow Documentation

`https://docs.langflow.org/url`

Copy page ⌥C Version: 1.12.x On this page

The **URL** component fetches content from one or more URLs, processes the content, and returns it in various formats. It follows links recursively to a given depth, and it supports output in plain text, Markdown, or raw HTML.


## URL parameters [​](https://docs.langflow.org/url#url-parameters)


Some parameters are hidden by default in the visual editor. You can modify all component parameters through the [component inspection panel](https://docs.langflow.org/concepts-components#component-inspection-panel) that appears when you select a component.
## URL parameters​
## URL output​




Some of the available parameters include the following:


| Name | Display Name | Info |
| --- | --- | --- |
| urls | URLs | Input parameter. One or more URLs to crawl recursively. In the visual editor, click **Add URL** to add multiple URLs. |
| max_depth | Depth | Input parameter. Controls link traversal: how many "clicks" away from the initial page the crawler will go. A depth of 1 limits the crawl to the first page at the given URL only. A depth of 2 means the crawler crawls the first page plus each page directly linked from the first page, then stops. This setting exclusively controls link traversal; it doesn't limit the number of URL path segments or the domain. |
| prevent_outside | Prevent Outside | Input parameter. If enabled, only crawls URLs within the same domain as the root URL. This prevents the crawler from accessing sites outside the given URL's domain, even if they are linked from one of the crawled pages. |
| use_async | Use Async | Input parameter. If enabled, uses asynchronous loading which can be significantly faster but might use more system resources. |
| format | Output Format | Input parameter. Sets the desired output format as **Text**, **Markdown**, or **HTML**. The default is **Text**. For more information, see [URL output](https://docs.langflow.org/url#url-output). |
| timeout | Timeout | Input parameter. Timeout for the request in seconds. |
| headers | Headers | Input parameter. The headers to send with the request if needed for authentication or otherwise. |


Additional input parameters are available for error handling and encoding.


## URL output [​](https://docs.langflow.org/url#url-output)


There are two settings that control the output of the **URL** component at different stages:


- **Output Format**: This optional parameter controls the content extracted from the crawled pages:
  - **Text (default)**: The component extracts only the text from the HTML of the crawled pages.
  - **Markdown**: The component converts the HTML content to markdown format using [Markitdown](https://github.com/microsoft/markitdown).
  - **HTML**: The component extracts the entire raw HTML content of the crawled pages.- **Output data type**: In the component's output field (near the output port) you can select the structure of the outgoing data when it is passed to other components:
  - **Extracted Pages**: Outputs a [`Table`](https://docs.langflow.org/data-types#table) that breaks the crawled pages into columns for the entire page content (`text`) and metadata like `url` and `title`.
  - **Raw Content**: Outputs a [`Message`](https://docs.langflow.org/data-types#message) containing the entire text, Markdown, or HTML from the crawled pages, including metadata, in a single block of text.


When used as a standard component in a flow, the **URL** component must be connected to a component that accepts the selected output data type (`Table` or `Message`). You can connect the **URL** component directly to a compatible component, or you can use a [**Type Convert** component](https://docs.langflow.org/type-convert) to convert the output to another type before passing the data to other components if the data types aren't directly compatible.


Processing components like the **Type Convert** component are useful with the **URL** component because it can extract a large amount of data from the crawled pages. For example, if you only want to pass specific fields to other components, you can use a [**Parser** component](https://docs.langflow.org/parser) to extract only that data from the crawled pages before passing the data to other components.


When used in **Tool Mode** with an **Agent** component, the **URL** component can be connected directly to the **Agent** component's **Tools** port without converting the data. The agent decides whether to use the **URL** component based on the user's query, and it can process the `Table` or `Message` output directly.


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)

- [URL parameters](https://docs.langflow.org/url#url-parameters)
- [URL output](https://docs.langflow.org/url#url-output)[Manage Privacy Choices](https://docs.langflow.org/url#)

---

# Chat Input and Output | Langflow Documentation

`https://docs.langflow.org/chat-input-and-output`

Copy page ⌥C Version: 1.12.x On this page


**Chat Input and Output** components are designed to handle conversational interactions in Langflow.


## Chat Input [​](https://docs.langflow.org/chat-input-and-output#chat-input)


The **Chat Input** component accepts text and file input, such as a chat message or a file. This data is passed to other components as [`Message` data](https://docs.langflow.org/data-types) containing the provided input as well as associated chat metadata, such as the sender, session ID, timestamp, and file attachments.


Initial input should *not* be provided as a complete `Message` object because the **Chat Input** component constructs the `Message` object that is then passed to other components in the flow.


### Chat Input parameters [​](https://docs.langflow.org/chat-input-and-output#chat-input-parameters)


Some parameters are hidden by default in the visual editor. You can modify all component parameters through the [component inspection panel](https://docs.langflow.org/concepts-components#component-inspection-panel) that appears when you select a component.


| Name | Display Name | Info |
| --- | --- | --- |
| input_value | Input Text | Input parameter. The message text string to be passed as input. |
| sender | Sender Type | Input parameter. Identifies the sender as either `User` or `Language Model`. |
| sender_name | Sender Name | Input parameter. The name of the sender. If unspecified, defaults to `User` or `Language Model`. |
| session_id | Session ID | Input parameter. The unique identifier for the chat session. If empty, the current session ID parameter is used. |
| files | Files | Input parameter. The files to be sent with the message. |
| background_color | Background Color | Input parameter. The background color of the icon. |
| chat_icon | Icon | Input parameter. The icon of the message. |
| should_store_message | Store Messages | Input parameter. Whether to store the message in chat history. |
| text_color | Text Color | Input parameter. The text color of the name. |


For information about the resulting `Message` object, including input parameters that are directly mapped to `Message` attributes, see [`Message` data](https://docs.langflow.org/data-types#message).


## Chat Output [​](https://docs.langflow.org/chat-input-and-output#chat-output)


The **Chat Output** component ingests `Message`, `JSON`, or `Table` data from other components, transforms it into `Message` data if needed, and then emits the final output as a chat message. For information about these data types, see [Use Langflow data types](https://docs.langflow.org/data-types).


In the **Playground**, chat output is limited to the parts of the `Message` object that are relevant to the chat interface, such as the text response, sender name, and file attachments. To see the metadata associated with a chat message, inspect the message logs in the **Playground**.


When using the Langflow API, the API response includes the **Chat Output** `Message` object along with other response data from the flow run. Langflow API responses can be extremely verbose, so your applications must include code to extract relevant data from the response to return to the user. For an example, see the [Langflow quickstart](https://docs.langflow.org/get-started-quickstart).


### Chat Output parameters [​](https://docs.langflow.org/chat-input-and-output#chat-output-parameters)


Some parameters are hidden by default in the visual editor. You can modify all component parameters through the [component inspection panel](https://docs.langflow.org/concepts-components#component-inspection-panel) that appears when you select a component.


| Name | Display Name | Info |
| --- | --- | --- |
| input_value | Inputs | Input parameter. The message text string to be passed as output. |
| should_store_message | Store Messages | Input parameter. Whether to store the message in chat history. |
| sender | Sender Type | Input parameter. Identifies the sender as either `User` or `Language Model`. |
| sender_name | Sender Name | Input parameter. The name of the sender. If unspecified, defaults to `User` or `Language Model`. |
| session_id | Session ID | Input parameter. The unique identifier for the chat session. If empty, the current session ID parameter is used. |
| data_template | Data Template | Input parameter. The template to convert [`JSON` input](https://docs.langflow.org/data-types#json) to `text`. If empty, it is dynamically set to the `JSON` object's `text` key. |
| background_color | Background Color | Input parameter. The background color of the icon. |
| chat_icon | Icon | Input parameter. The icon of the message. |
| text_color | Text Color | Input parameter. The text color of the name. |
| clean_data | Basic Clean Data | Input parameter. When enabled, [`Table` input](https://docs.langflow.org/data-types#table) is cleaned when converted to text. Cleaning removes empty rows, empty lines in cells, and multiple newlines. |


For information about the resulting `Message` object, including input parameters that are directly mapped to `Message` attributes, see [`Message` data](https://docs.langflow.org/data-types#message).


## Use Chat Input and Output components in a flow [​](https://docs.langflow.org/chat-input-and-output#use-chat-input-and-output-components-in-a-flow)


To use the **Chat Input** and **Chat Output** components in a flow, connect them to components that accept or emit [`Message` data](https://docs.langflow.org/data-types#message).


For example, the following flow connects **Chat Input** and **Chat Output** to a **Language Model** component, creating a simple LLM-based chat flow.


![Chat Input and Output components connected to an OpenAI component](https://docs.langflow.org/assets/images/component-chat-io-ae6252ae1ebc69b9c7ce74f33c251699.png)


### Send chat input with the Langflow API [​](https://docs.langflow.org/chat-input-and-output#send-chat-input-with-the-langflow-api)


You can use the Langflow API to run a flow by sending input to a **Chat Input** component:


```bash
curl --request POST \
  --url "http://$LANGFLOW_SERVER_ADDRESS/api/v1/run/$FLOW_ID" \
  --header "Content-Type: application/json" \
  --header "x-api-key: $LANGFLOW_API_KEY" \
  --data '{
  "input_value": "What's the recommended way to install Docker on Mac M1?",
  "output_type": "chat",
  "input_type": "chat"
}'
```


When triggering flows with the Langflow API, the payload must contain the values for the **Chat Input** component's input parameters, such as `input_value`.


Not all parameters need to be specified in the request. For example, `session_id` uses the flow's default session ID if omitted. If you want to use a custom session ID, include `session_id` in your request:


```bash
curl --request POST \
  --url "http://$LANGFLOW_SERVER_ADDRESS/api/v1/run/$FLOW_ID" \
  --header "Content-Type: application/json" \
  --header "x-api-key: $LANGFLOW_API_KEY" \
  --data '{
  "input_value": "Whats the recommended way to install Docker on Mac M1",
  "session_id": "$USER_ID",
  "output_type": "chat",
  "input_type": "chat"
}'
```


For more information, see [Trigger flows with the Langflow API](https://docs.langflow.org/concepts-publish).
## Chat Input​
## Chat Output​
## Use Chat Input and Output components in a flow​





Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)

- [Chat Input](https://docs.langflow.org/chat-input-and-output#chat-input)
  - [Chat Input parameters](https://docs.langflow.org/chat-input-and-output#chat-input-parameters)- [Chat Output](https://docs.langflow.org/chat-input-and-output#chat-output)
  - [Chat Output parameters](https://docs.langflow.org/chat-input-and-output#chat-output-parameters)- [Use Chat Input and Output components in a flow](https://docs.langflow.org/chat-input-and-output#use-chat-input-and-output-components-in-a-flow)
  - [Send chat input with the Langflow API](https://docs.langflow.org/chat-input-and-output#send-chat-input-with-the-langflow-api)[Manage Privacy Choices](https://docs.langflow.org/chat-input-and-output#)

---

# Calculator | Langflow Documentation

`https://docs.langflow.org/calculator`

Copy page ⌥C Version: 1.12.x On this page

The **Calculator** component performs basic arithmetic operations on mathematical expressions. It supports addition, subtraction, multiplication, division, and exponentiation operations.


For an example of using this component in a flow, see the [**Python Interpreter** component](https://docs.langflow.org/python-interpreter).


## Calculator parameters [​](https://docs.langflow.org/calculator#calculator-parameters)


| Name | Type | Description |
| --- | --- | --- |
| expression | String | Input parameter. The arithmetic expression to evaluate, such as `4*4*(33/22)+12-20`. |
| result | JSON | Output parameter. The calculation result as a [`JSON` object](https://docs.langflow.org/data-types) containing the evaluated expression. |
## Calculator parameters​



Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)

- [Calculator parameters](https://docs.langflow.org/calculator#calculator-parameters)[Manage Privacy Choices](https://docs.langflow.org/calculator#)

---

# Get started with the Langflow API | Langflow Documentation

`https://docs.langflow.org/api-reference-api-examples`

# Get started with the Langflow API

To view and test all available endpoints, you can access the Langflow API's OpenAPI specification at your Langflow deployment's /docs endpoint, such as http://localhost:7860/docs.

Copy page ⌥C Version: 1.12.x On this page
## Form Langflow API requests​
*The Langflow API serves /v1 and /v2 endpoints.*

## Set environment variables​
## Try some Langflow API requests​
*Returns a dictionary of all Langflow components.
Requires a Langflow API key.*

## Available endpoints​
## Next steps​






You can use the Langflow API for programmatic interactions with Langflow, such as the following:


- Create and edit flows, including file management for flows.
- Develop applications that use your flows.
- Develop custom components.
- Build Langflow as a dependency of a larger application, codebase, or service.
- Contribute to the overall Langflow codebase.


To view and test all available endpoints, you can access the Langflow API's OpenAPI specification at your Langflow deployment's `/docs` endpoint, such as `http://localhost:7860/docs`.


## Form Langflow API requests [​](https://docs.langflow.org/api-reference-api-examples#form-langflow-api-requests)


While individual options vary by endpoint, all Langflow API requests share some commonalities, like a URL, method, parameters, and authentication.


As an example of a Langflow API request, the following curl command calls the `/v1/run` endpoint, and it passes a runtime override (`tweaks`) to the flow's **Chat Output** component:


- Python
- JavaScript
- curl


```python
import os

import requests

base = os.environ.get("LANGFLOW_URL") or os.environ.get("LANGFLOW_SERVER_URL", "")
flow_id = os.environ.get("FLOW_ID", "")
api_key = os.environ.get("LANGFLOW_API_KEY", "")

url = f"{base}/api/v1/run/{flow_id}?stream=false"

headers = {
    "Content-Type": "application/json",
    "x-api-key": api_key,
}

payload = {
    "input_value": "hello world!",
    "output_type": "chat",
    "input_type": "chat",
}

response = requests.post(url, headers=headers, json=payload, timeout=60)
response.raise_for_status()
print(response.text)
```


```js
const url = `${process.env.LANGFLOW_SERVER_URL ?? ""}/api/v1/run/${process.env.FLOW_ID ?? ""}?stream=false`;

const options = {
  method: 'POST',
  headers: {
    "Content-Type": `application/json`,
    "x-api-key": `${process.env.LANGFLOW_API_KEY ?? ""}`,
  },
  body: JSON.stringify({
  "input_value": "hello world!",
  "output_type": "chat",
  "input_type": "chat",
  "tweaks": {
    "ChatOutput-6zcZt": {
      "should_store_message": true
    }
  }
}),
};

fetch(url, options)
  .then(async (response) => {
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    const text = await response.text();
    console.log(text);
  })
  .catch((error) => console.error(error));
```


```bash
curl --request POST \
  --url "$LANGFLOW_SERVER_URL/api/v1/run/$FLOW_ID?stream=false" \
  --header "Content-Type: application/json" \
  --header "x-api-key: $LANGFLOW_API_KEY" \
  --data '{
  "input_value": "hello world!",
  "output_type": "chat",
  "input_type": "chat",
  "tweaks": {
    "ChatOutput-6zcZt": {
      "should_store_message": true
    }
  }
}'
```


### Base URL [​](https://docs.langflow.org/api-reference-api-examples#base-url)


By default, local deployments serve the Langflow API at `http://localhost:7860/api`.


Remotely hosted Langflow deployments are available at the domain set by the hosting service, such as `http://IP_OR_DNS/api` or `http://IP_OR_DNS:LANGFLOW_PORT/api`.


You can configure the Langflow port number in the `LANGFLOW_PORT` [environment variable](https://docs.langflow.org/environment-variables).


- `https://UUID.ngrok.app/api`
- `http://IP_OR_DNS/api`
- `http://IP_OR_DNS:LANGFLOW_PORT/api`


### Authentication [​](https://docs.langflow.org/api-reference-api-examples#authentication)


In Langflow versions 1.5 and later, most API endpoints require authentication with a Langflow API key in either an `x-api-key` header or query parameter. For more information, see [API keys and authentication](https://docs.langflow.org/api-keys-and-authentication).


As with any API, follow industry best practices for storing and referencing sensitive credentials. For example, you can [set environment variables](https://docs.langflow.org/api-reference-api-examples#set-environment-variables) for your API keys, and then reference those environment variables in your API requests.


### Methods, paths, and parameters [​](https://docs.langflow.org/api-reference-api-examples#methods-paths-and-parameters)


Langflow API requests use various methods, paths, path parameters, query parameters, and body parameters. The specific requirements and options depend on the endpoint that you want to call.


For example, to create a flow, you pass a JSON-formatted flow definition to `POST /v1/flows`. Then, to run your flow, you call `POST /v1/run/$FLOW_ID` with optional run parameters in the request body.


### API versions [​](https://docs.langflow.org/api-reference-api-examples#api-versions)


The Langflow API serves `/v1` and `/v2` endpoints.


Some endpoints only exist under a single version and some exist under both the `/v1` and `/v2` versions.


If a request fails or has an unexpected result, make sure your endpoint path has the correct version.


## Set environment variables [​](https://docs.langflow.org/api-reference-api-examples#set-environment-variables)


You can store commonly used values in environment variables to facilitate reuse, simplify token rotation, and securely reference sensitive values.


You can use any method you prefer to set environment variables, such as `export`, `.env`, `zshrc`, or `.curlrc`. Then, reference those environment variables in your API requests. For example:


```bash
# Set environment variables (allow callers/wrappers to override defaults)
export LANGFLOW_API_KEY="${LANGFLOW_API_KEY:-sk-local-placeholder}"
export LANGFLOW_SERVER_URL="${LANGFLOW_SERVER_URL:-http://localhost:7860}"
export FLOW_ID="${FLOW_ID:-359cd752-07ea-46f2-9d3b-a4407ef618da}"
export PROJECT_ID="${PROJECT_ID:-1415de42-8f01-4f36-bf34-539f23e47466}"

# Use environment variables in API requests
curl --request POST \
  --url "$LANGFLOW_SERVER_URL/api/v1/run/$FLOW_ID?stream=false" \
  --header "Content-Type: application/json" \
  --header "x-api-key: $LANGFLOW_API_KEY" \
  --data '{
  "input_value": "hello world!",
  "output_type": "chat",
  "input_type": "chat",
  "tweaks": {
    "ChatOutput-6zcZt": {
      "should_store_message": true
    }
  }
}'
```


Commonly used values in Langflow API requests include your [Langflow server URL](https://docs.langflow.org/api-reference-api-examples#base-url), [Langflow API keys](https://docs.langflow.org/api-reference-api-examples#authentication), flow IDs, and [project IDs](https://docs.langflow.org/api-projects#read-projects).


You can retrieve flow IDs from the [**API access** pane](https://docs.langflow.org/concepts-publish#api-access), in a flow's URL, and with [`GET /flows`](https://docs.langflow.org/api-flows#read-flows).


## Try some Langflow API requests [​](https://docs.langflow.org/api-reference-api-examples#try-some-langflow-api-requests)


Once you have your Langflow server URL, try calling these endpoints that return Langflow metadata.


### Health check [​](https://docs.langflow.org/api-reference-api-examples#health-check)


Returns the health status of the Langflow database and chat services:


- Python
- JavaScript
- curl


```python
import os

import requests

url = f"{os.getenv('LANGFLOW_SERVER_URL', '')}/health_check"

headers = {
    "accept": "application/json",
}

response = requests.request("GET", url, headers=headers)
response.raise_for_status()

print(response.text)
```


```js
const url = `${process.env.LANGFLOW_SERVER_URL ?? ""}/health_check`;

const options = {
  method: 'GET',
  headers: {
    "accept": `application/json`,
  },
};

fetch(url, options)
  .then(async (response) => {
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    const text = await response.text();
    console.log(text);
  })
  .catch((error) => console.error(error));
```


```bash
curl -X GET \
  "$LANGFLOW_SERVER_URL/health_check" \
  -H "accept: application/json"
```


Langflow provides an additional `GET /health` endpoint. This endpoint is served by uvicorn before Langflow is fully initialized, so it's not reliable for checking Langflow service health.


### Get version [​](https://docs.langflow.org/api-reference-api-examples#get-version)


Returns the current Langflow API version:


- Python
- JavaScript
- curl


```python
import os

import requests

url = f"{os.getenv('LANGFLOW_SERVER_URL', '')}/api/v1/version"

headers = {
    "accept": "application/json",
}

response = requests.request("GET", url, headers=headers)
response.raise_for_status()

print(response.text)
```


```js
const url = `${process.env.LANGFLOW_SERVER_URL ?? ""}/api/v1/version`;

const options = {
  method: 'GET',
  headers: {
    "accept": `application/json`,
  },
};

fetch(url, options)
  .then(async (response) => {
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    const text = await response.text();
    console.log(text);
  })
  .catch((error) => console.error(error));
```


```bash
curl -X GET \
  "$LANGFLOW_SERVER_URL/api/v1/version" \
  -H "accept: application/json"
```


### Get configuration [​](https://docs.langflow.org/api-reference-api-examples#get-configuration)


Returns configuration details for your Langflow deployment. Requires a [Langflow API key](https://docs.langflow.org/api-keys-and-authentication).


- Python
- JavaScript
- curl


```python
import os

import requests

url = f"{os.getenv('LANGFLOW_SERVER_URL', '')}/api/v1/config"

headers = {
    "accept": "application/json",
    "x-api-key": f"{os.getenv('LANGFLOW_API_KEY', '')}",
}

response = requests.request("GET", url, headers=headers)
response.raise_for_status()

print(response.text)
```


```js
const url = `${process.env.LANGFLOW_SERVER_URL ?? ""}/api/v1/config`;

const options = {
  method: 'GET',
  headers: {
    "accept": `application/json`,
    "x-api-key": `${process.env.LANGFLOW_API_KEY ?? ""}`,
  },
};

fetch(url, options)
  .then(async (response) => {
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    const text = await response.text();
    console.log(text);
  })
  .catch((error) => console.error(error));
```


```bash
curl -X GET \
  "$LANGFLOW_SERVER_URL/api/v1/config" \
  -H "accept: application/json" \
  -H "x-api-key: $LANGFLOW_API_KEY"
```


### Get all components [​](https://docs.langflow.org/api-reference-api-examples#get-all-components)


Returns a dictionary of all Langflow components. Requires a [Langflow API key](https://docs.langflow.org/api-keys-and-authentication).


- Python
- JavaScript
- curl


```python
import os

import requests

url = f"{os.getenv('LANGFLOW_SERVER_URL', '')}/api/v1/all"

headers = {
    "accept": "application/json",
    "x-api-key": f"{os.getenv('LANGFLOW_API_KEY', '')}",
}

response = requests.request("GET", url, headers=headers)
response.raise_for_status()

print(response.text)
```


```js
const url = `${process.env.LANGFLOW_SERVER_URL ?? ""}/api/v1/all`;

const options = {
  method: 'GET',
  headers: {
    "accept": `application/json`,
    "x-api-key": `${process.env.LANGFLOW_API_KEY ?? ""}`,
  },
};

fetch(url, options)
  .then(async (response) => {
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    const text = await response.text();
    console.log(text);
  })
  .catch((error) => console.error(error));
```


```bash
curl -X GET \
  "$LANGFLOW_SERVER_URL/api/v1/all" \
  -H "accept: application/json" \
  -H "x-api-key: $LANGFLOW_API_KEY"
```


## Available endpoints [​](https://docs.langflow.org/api-reference-api-examples#available-endpoints)


Because you can run Langflow as either an IDE (frontend and backend) or a runtime (headless, backend-only), it serves endpoints that support frontend and backend operations. Many endpoints are for orchestration between the frontend and backend, reading and writing to the Langflow database, or enabling frontend functionality, like the **Playground**. Unless you are contributing to the Langflow codebase, you won't directly call most of the Langflow endpoints.


For application development, the most commonly used endpoints are the `/run` and `/webhook` [flow trigger endpoints](https://docs.langflow.org/api-flows-run). For some use cases, you might use some other endpoints, such as the `/files` endpoints to use files in flows.


To help you explore the available endpoints, the following lists are sorted by primary use case, although some endpoints might support multiple use cases.


- Application development
- Codebase development
- Deprecated


The following endpoints are useful for developing applications with Langflow and administering Langflow deployments with one or more users. You will most often use the flow trigger endpoints. Other endpoints are helpful for specific use cases, such as administration and flow management in runtime deployments that don't have a visual editor.


- [Flow trigger endpoints](https://docs.langflow.org/api-flows-run):
  - POST `/v1/run/{flow_id_or_name}`: Run a flow.
  - POST `/v1/run/advanced/{flow_id}`: Advanced run with explicit `inputs`, `outputs`, `tweaks`, and optional `session_id`.
  - POST `/v1/webhook/{flow_id_or_name}`: Trigger a flow via webhook payload.- [OpenAI Responses API](https://docs.langflow.org/api-openai-responses):
  - POST `/v1/responses`: Execute flows using an OpenAI-compatible request format.- Deployment details:
  - GET `/v1/version`: Return Langflow version. See [Get version](https://docs.langflow.org/api-reference-api-examples#get-version).
  - GET `/v1/config`: Return deployment configuration. See [Get configuration](https://docs.langflow.org/api-reference-api-examples#get-configuration).
  - GET `/health_check`: Health check endpoint that validates database and chat service connectivity. Returns 500 status if any service is unavailable.- [Projects endpoints](https://docs.langflow.org/api-projects):
  - POST `/v1/projects/`: Create a project.
  - GET `/v1/projects/`: List projects.
  - GET `/v1/projects/{project_id}`: Read a project (with paginated flows support).
  - PATCH `/v1/projects/{project_id}`: Update project info and membership.
  - DELETE `/v1/projects/{project_id}`: Delete a project.
  - GET `/v1/projects/download/{project_id}`: Export all flows in a project as ZIP.
  - POST `/v1/projects/upload/`: Import a project ZIP (creates project and flows).
  - GET `/v1/starter-projects/`: Return a list of templates.- [Files endpoints](https://docs.langflow.org/api-files):
  - Files (v1)
    - POST `/v1/files/upload/{flow_id}`: Upload a file to a specific flow.
    - GET `/v1/files/download/{flow_id}/{file_name}`: Download a file from a flow.
    - GET `/v1/files/images/{flow_id}/{file_name}`: Stream an image from a flow.
    - GET `/v1/files/profile_pictures/{folder_name}/{file_name}`: Get a profile picture asset.
    - GET `/v1/files/profile_pictures/list`: List available profile picture assets.
    - GET `/v1/files/list/{flow_id}`: List files for a flow.
    - DELETE `/v1/files/delete/{flow_id}/{file_name}`: Delete a file from a flow.  - Files (v2)
    - POST `/v2/files` (alias `/v2/files/`): Upload a file owned by the current user.
    - GET `/v2/files` (alias `/v2/files/`): List files owned by the current user.
    - DELETE `/v2/files/batch/`: Delete multiple files by IDs.
    - POST `/v2/files/batch/`: Download multiple files as a ZIP by IDs.
    - GET `/v2/files/{file_id}`: Download a file by ID (or return raw content internally).
    - PUT `/v2/files/{file_id}`: Edit a file name by ID.
    - DELETE `/v2/files/{file_id}`: Delete a file by ID.
    - DELETE `/v2/files` (alias `/v2/files/`): Delete all files for the current user.- [API keys and authentication](https://docs.langflow.org/api-keys-and-authentication):
  - GET `/v1/api_key/`: List API keys for the current user.
  - POST `/v1/api_key/`: Create a new API key.
  - DELETE `/v1/api_key/{api_key_id}`: Delete an API key.
  - POST `/v1/api_key/store`: Save an encrypted Store API key (cookie set).- [Flow management endpoints](https://docs.langflow.org/api-flows):
  - POST `/v1/flows/`: Create a flow.
  - GET `/v1/flows/`: List flows (supports pagination and filters).
  - GET `/v1/flows/{flow_id}`: Read a flow by ID.
  - GET `/v1/flows/public_flow/{flow_id}`: Read a public flow by ID.
  - PATCH `/v1/flows/{flow_id}`: Update a flow.
  - DELETE `/v1/flows/{flow_id}`: Delete a flow.
  - POST `/v1/flows/batch/`: Create multiple flows.
  - POST `/v1/flows/upload/`: Import flows from a JSON file.
  - DELETE `/v1/flows/`: Delete multiple flows by IDs.
  - POST `/v1/flows/download/`: Export flows to a ZIP file.
  - GET `/v1/flows/basic_examples/`: List basic example flows.- [Users endpoints](https://docs.langflow.org/api-users):
  - POST `/v1/users/`: Add a user (superuser required when auth enabled).
  - GET `/v1/users/whoami`: Return the current authenticated user.
  - GET `/v1/users/`: List all users (superuser required).
  - PATCH `/v1/users/{user_id}`: Update a user (with role checks).
  - PATCH `/v1/users/{user_id}/reset-password`: Reset own password.
  - DELETE `/v1/users/{user_id}`: Delete a user (cannot delete yourself).- [Catalog and model policy](https://docs.langflow.org/api-governance-policy) (superuser required):
  - GET `/v1/policy-bundle`: Read the install-wide catalog and model policy.
  - PUT `/v1/policy-bundle`: Replace the bundle. Requires `expected_revision`.
  - GET `/v1/catalog-policy/components` and `PUT /v1/catalog-policy/components`: Blocked component keys.
  - GET `/v1/model-provider-policy` and `PUT /v1/model-provider-policy`: Approved model providers.- Custom components: You might use these endpoints when developing custom Langflow components for your own use or to share with the Langflow community:
  - GET `/v1/all`: Return all available Langflow component types. See [Get all components](https://docs.langflow.org/api-reference-api-examples#get-all-components).
  - POST `/v1/custom_component`: Build a custom component from code and return its node.
  - POST `/v1/custom_component/update`: Update an existing custom component's build config and outputs.
  - POST `/v1/validate/code`: Validate a Python code snippet for a custom component.
  - POST `/v1/validate/prompt`: Validate a prompt payload.


The following endpoints are most often used when contributing to the Langflow codebase, and you need to understand or call endpoints that support frontend-to-backend orchestration or other internal functionality.


- Base (metadata):
  - GET `/v1/all`: Return all available Langflow component types. See [Get all components](https://docs.langflow.org/api-reference-api-examples#get-all-components).
  - GET `/v1/version`: Return Langflow version. See [Get version](https://docs.langflow.org/api-reference-api-examples#get-version).
  - GET `/v1/config`: Return deployment configuration. See [Get configuration](https://docs.langflow.org/api-reference-api-examples#get-configuration).
  - GET `/v1/starter-projects/`: Return a list of templates.- [Build endpoints](https://docs.langflow.org/api-build) (internal editor support):
  - POST `/v1/build/{flow_id}/flow`: Start a flow build and return a job ID.
  - GET `/v1/build/{job_id}/events`: Stream or fetch build events.
  - POST `/v1/build/{job_id}/cancel`: Cancel a build job.
  - POST `/v1/build_public_tmp/{flow_id}/flow`: Build a public flow without auth.
  - POST `/v1/validate/prompt`: Validate a prompt payload.- [API keys and authentication](https://docs.langflow.org/api-keys-and-authentication):
  - POST `/v1/login`: Login and set tokens as cookies.
  - GET `/v1/auto_login`: Auto-login (if enabled) and set tokens.
  - POST `/v1/refresh`: Refresh tokens using refresh cookie.
  - POST `/v1/logout`: Logout and clear cookies.- [Monitor endpoints](https://docs.langflow.org/api-monitor):
  - GET `/v1/monitor/builds`: Get vertex builds for a flow.
  - DELETE `/v1/monitor/builds`: Delete vertex builds for a flow.
  - GET `/v1/monitor/messages/sessions`: List message session IDs (auth required).
  - GET `/v1/monitor/messages`: List messages with optional filters.
  - DELETE `/v1/monitor/messages`: Delete messages by IDs (auth required).
  - PUT `/v1/monitor/messages/{message_id}`: Update a message.
  - PATCH `/v1/monitor/messages/session/{old_session_id}`: Change a session ID for all messages in that session.
  - DELETE `/v1/monitor/messages/session/{session_id}`: Delete messages by session.
  - GET `/v1/monitor/transactions`: List transactions for a flow (paginated).- Variables:
  - POST `/v1/variables/`: Create a variable, such as an API key, for the user.
  - GET `/v1/variables/`: List variables for the user.
  - PATCH `/v1/variables/{variable_id}`: Update a variable.
  - DELETE `/v1/variables/{variable_id}`: Delete a variable.- [Use voice mode](https://docs.langflow.org/concepts-voice-mode):
  - WS `/v1/voice/ws/flow_tts/{flow_id}`: Speech-to-text session that runs a flow and returns TTS.
  - WS `/v1/voice/ws/flow_tts/{flow_id}/{session_id}`: Same as above with explicit session ID.
  - GET `/v1/voice/elevenlabs/voice_ids`: List available ElevenLabs voice IDs for the user.- MCP servers: The following endpoints are for managing Langflow MCP servers and MCP server connections. They aren't typically called directly; instead, they are used to drive internal functionality in the Langflow frontend and when running flows that call MCP servers. Langflow MCP servers support both streamable HTTP and SSE transport.
  - HEAD `/v1/mcp/streamable`: Health check for streamable HTTP MCP.
  - GET `/v1/mcp/streamable`: Open streamable HTTP connection for MCP server.
  - POST `/v1/mcp/streamable`: Post messages to the MCP server via streamable HTTP.
  - DELETE `/v1/mcp/streamable`: Close streamable HTTP connection.
  - HEAD `/v1/mcp/sse` (LEGACY): Health check for MCP SSE.
  - GET `/v1/mcp/sse` (LEGACY): Open SSE stream for MCP server events.
  - POST `/v1/mcp/` (LEGACY): Post messages to the MCP server.
  - GET `/v1/mcp/project/{project_id}`: List MCP-enabled tools and project auth settings.
  - HEAD `/v1/mcp/project/{project_id}/streamable`: Health check for project streamable HTTP MCP.
  - GET `/v1/mcp/project/{project_id}/streamable`: Open project-scoped streamable HTTP connection.
  - POST `/v1/mcp/project/{project_id}/streamable`: Post messages to project MCP server via streamable HTTP.
  - DELETE `/v1/mcp/project/{project_id}/streamable`: Close project streamable HTTP connection.
  - HEAD `/v1/mcp/project/{project_id}/sse` (LEGACY): Health check for project SSE.
  - GET `/v1/mcp/project/{project_id}/sse` (LEGACY): Open project-scoped MCP SSE.
  - POST `/v1/mcp/project/{project_id}` (LEGACY): Post messages to project MCP server.
  - PATCH `/v1/mcp/project/{project_id}`: Update MCP settings for flows and project auth settings.
  - POST `/v1/mcp/project/{project_id}/install`: Install MCP client config for Cursor/Windsurf/Claude (local only).
  - GET `/v1/mcp/project/{project_id}/installed`: Check which clients have MCP config installed.- Custom components: You might use these endpoints when developing custom Langflow components for your own use or to share with the Langflow community:
  - GET `/v1/all`: Return all available Langflow component types. See [Get all components](https://docs.langflow.org/api-reference-api-examples#get-all-components).
  - POST `/v1/custom_component`: Build a custom component from code and return its node.
  - POST `/v1/custom_component/update`: Update an existing custom component's build config and outputs.
  - POST `/v1/validate/code`: Validate a Python code snippet for a custom component.
  - POST `/v1/validate/prompt`: Validate a prompt payload.


The following endpoints are deprecated:


- POST `/v1/predict/{flow_id}`: Use [`/v1/run/{flow_id}`](https://docs.langflow.org/api-flows-run) instead.
- POST `/v1/process/{flow_id}`: Use [`/v1/run/{flow_id}`](https://docs.langflow.org/api-flows-run) instead.
- GET `/v1/task/{task_id}`: Deprecated functionality.
- POST `/v1/upload/{flow_id}`: Use [`/files`](https://docs.langflow.org/api-files) instead.
- POST `/v1/build/{flow_id}/vertices`: Replaced by [`/monitor/builds`](https://docs.langflow.org/api-monitor).
- POST `/v1/build/{flow_id}/vertices/{vertex_id}`: Replaced by [`/monitor/builds`](https://docs.langflow.org/api-monitor).
- GET `/v1/build/{flow_id}/{vertex_id}/stream`: Replaced by [`/monitor/builds`](https://docs.langflow.org/api-monitor).
- GET `/v1/store/check/`: Return whether the Store feature is enabled.
- GET `/v1/store/check/api_key`: Check if a Store API key exists and is valid.
- POST `/v1/store/components/`: Share a component to the Store.
- PATCH `/v1/store/components/{component_id}`: Update a shared component.
- GET `/v1/store/components/`: List available Store components (filters supported).
- GET `/v1/store/components/{component_id}`: Download a component from the Store.
- GET `/v1/store/tags`: List Store tags.
- GET `/v1/store/users/likes`: List components liked by the current user.
- POST `/v1/store/users/likes/{component_id}`: Like a component.


## Next steps [​](https://docs.langflow.org/api-reference-api-examples#next-steps)


- Use the Langflow API to [run a flow](https://docs.langflow.org/api-flows-run).
- Use the Langflow API to [upload files](https://docs.langflow.org/api-files).
- Use the Langflow API to [get flow logs](https://docs.langflow.org/api-logs).
- Explore all endpoints in the [Langflow API specification](https://docs.langflow.org/api).


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)

- [Form Langflow API requests](https://docs.langflow.org/api-reference-api-examples#form-langflow-api-requests)
  - [Base URL](https://docs.langflow.org/api-reference-api-examples#base-url)
  - [Authentication](https://docs.langflow.org/api-reference-api-examples#authentication)
  - [Methods, paths, and parameters](https://docs.langflow.org/api-reference-api-examples#methods-paths-and-parameters)
  - [API versions](https://docs.langflow.org/api-reference-api-examples#api-versions)- [Set environment variables](https://docs.langflow.org/api-reference-api-examples#set-environment-variables)
- [Try some Langflow API requests](https://docs.langflow.org/api-reference-api-examples#try-some-langflow-api-requests)
  - [Health check](https://docs.langflow.org/api-reference-api-examples#health-check)
  - [Get version](https://docs.langflow.org/api-reference-api-examples#get-version)
  - [Get configuration](https://docs.langflow.org/api-reference-api-examples#get-configuration)
  - [Get all components](https://docs.langflow.org/api-reference-api-examples#get-all-components)- [Available endpoints](https://docs.langflow.org/api-reference-api-examples#available-endpoints)
- [Next steps](https://docs.langflow.org/api-reference-api-examples#next-steps)[Manage Privacy Choices](https://docs.langflow.org/api-reference-api-examples#)

---

# Language Model | Langflow Documentation

`https://docs.langflow.org/components-models`

Copy page ⌥C Version: 1.12.x On this page
## Use language model components in flows​
## Language model parameters​
## Language model output types​
## Additional language models​
## Pair models with vector stores​






Language model components in Langflow generate text using a specified Large Language Model (LLM). These components accept inputs like chat messages, files, and instructions in order to generate a text response.


Langflow includes a **Language Model** core component that has built-in support for many LLMs. Alternatively, you can use any [additional language model](https://docs.langflow.org/components-models#additional-language-models) in place of the **Language Model** core component.


## Use language model components in flows [​](https://docs.langflow.org/components-models#use-language-model-components-in-flows)


Use language model components anywhere you would use an LLM in a flow.


- Chat
- Drivers
- Agents


One of the most common use cases of language model components is to chat with LLMs in your flows.


The following example uses a language model component in a chatbot flow similar to the **Basic Prompting** template.


1. To edit Langflow's global model provider configuration, do the following: After you enable a model in Langflow's global model configuration, you can use that model in any model-driven component in your flows.
  1. To open the **Model Providers** pane, click your profile icon, select **Settings**, and then click **Model Providers**.
  2. In the **Model Providers** pane, select a provider.
  3. In the **API Key** field, add your provider's API key. Some providers require additional configuration fields. For more information, see the model provider's documentation. The key must have permission to call the models you want to use in your flow, and your account must have sufficient credits for the actions you want to perform. You can only add one key for each provider. Make sure the key has access to *all* models that you want to use in Langflow.
  4. Click **Save**.
  5. Enable the specific models that you want to use in Langflow. The available models depend on the provider and your API key's permissions. Models that generate text are listed under **Language Models**. Models that generate embeddings are listed under **Embedding Models**.2. Add the **Language Model** core component to your flow, and then select your model from the **Language Model** field. Optionally, to configure API keys and enable or disable models, click **Manage Model Providers** to open the **Model Providers** pane.
3. In the [component inspection panel](https://docs.langflow.org/concepts-components#component-menus), enable the **System Message** parameter.
4. Add a [**Prompt Template** component](https://docs.langflow.org/components-prompts) to your flow.
5. In the **Template** field, enter some instructions for the LLM, such as `You are an expert in geography who is tutoring high school students`.
6. Connect the **Prompt Template** component's output to the **Language Model** component's **System Message** input.
7. Add [**Chat Input** and **Chat Output** components](https://docs.langflow.org/chat-input-and-output) to your flow. These components are required for direct chat interaction with an LLM.
8. Connect the **Chat Input** component to the **Language Model** component's **Input**, and then connect the **Language Model** component's **Message** output to the **Chat Output** component. ![A basic prompting flow with Language Model, Prompt Template, Chat Input, and Chat Output components](https://docs.langflow.org/assets/images/component-language-model-beccd1ed73b0f526547622f3c592fa45.png)
9. Open the **Playground**, and ask a question to chat with the LLM and test the flow, such as `What is the capital of Utah?`.
10. Optional: Try a different model or provider to see how the response changes. If you enabled multiple models in Langflow's global **Model Providers** pane, select a different model in the **Language Model** field. To open the **Model Providers** pane, click your profile icon, select **Settings**, and then click **Model Providers**. Then, open the **Playground**, ask the same question as you did before, and then compare the content and format of the responses. This helps you understand how different models handle the same request so you can choose the best model for your use case. You can also learn more about different models in each model provider's documentation.


Some components use a language model component to perform LLM-driven actions. Typically, these components prepare data for further processing by downstream components, rather than emitting direct chat output. For an example, see the [**Smart Transform** component](https://docs.langflow.org/smart-transform).


A component must accept a `LanguageModel` input to use a language model component as a driver, and you must set the language model component's output type to `LanguageModel`. For more information, see [Language Model output types](https://docs.langflow.org/components-models#language-model-output-types).


If you don't want to use the **Agent** component's built-in LLM, you can use a language model component to connect your preferred model:


1. Add a language model component to your flow. You can use the **Language Model** core component or browse [**Bundles**](https://docs.langflow.org/components-bundle-components) to find additional language models. Components in bundles may not have `language model` in the name. For example, Azure OpenAI LLMs are provided through the [**Azure OpenAI** component](https://docs.langflow.org/bundles-azure#azure-openai).
2. Select your preferred model from the **Language Model** dropdown. The model must be configured globally in the **Models** pane.
3. Change the language model component's output type from **Model Response** to **Language Model**. The output port changes to a `LanguageModel` port. This is required to connect the language model component to the **Agent** component. For more information, see [Language Model output types](https://docs.langflow.org/components-models#language-model-output-types).
4. Add an **Agent** component to the flow.
5. Connect the language model component's output to the **Agent** component's **Language Model** input. The **Agent** component now inherits the language model settings from the connected language model component instead of using any of the built-in models.


## Language model parameters [​](https://docs.langflow.org/components-models#language-model-parameters)


The following parameters are for the **Language Model** core component. Other language model components can have additional or different parameters.


Some parameters are hidden by default in the visual editor. You can modify all component parameters through the [component inspection panel](https://docs.langflow.org/concepts-components#component-inspection-panel) that appears when you select a component.


| Name | Type | Description |
| --- | --- | --- |
| provider | String | Input parameter. The model provider to use. Options depend on your global **Models** configuration. |
| model_name | String | Input parameter. The name of the model to use. Options depend on the selected provider and your global **Models** configuration. |
| input_value | String | Input parameter. The input text to send to the model. |
| system_message | String | Input parameter. A system message that helps set the behavior of the assistant. |
| stream | Boolean | Input parameter. Whether to stream the response. Default: `false`. |
| temperature | Float | Input parameter. Controls randomness in responses. Range: `[0.0, 1.0]`. Default: `0.1`. |
| model | LanguageModel | Output parameter. Alternative output type to the default `Message` output. Produces an instance of Chat configured with the specified parameters. See [Language Model output types](https://docs.langflow.org/components-models#language-model-output-types). |


## Language model output types [​](https://docs.langflow.org/components-models#language-model-output-types)


Language model components, including the core component and bundled components, can produce two types of output:


- **Model Response**: The default output type emits the model's generated response as [`Message` data](https://docs.langflow.org/data-types#message). Use this output type when you want the typical LLM interaction where the LLM produces a text response based on given input.
- **Language Model**: Change the language model component's output type to [`LanguageModel`](https://docs.langflow.org/data-types#languagemodel) when you need to attach an LLM to another component in your flow, such as an **Agent** or **Smart Transform** component. With this configuration, the language model component supports an action completed by another component, rather than a direct chat interaction. For an example, the **Smart Transform** component uses an LLM to create a function from natural language input.


## Additional language models [​](https://docs.langflow.org/components-models#additional-language-models)


If your provider or model isn't supported by the **Language Model** core component, additional language model components are available in [**Bundles**](https://docs.langflow.org/components-bundle-components).


You can use these components in the same way that you use the core **Language Model** component, as explained in [Use language model components in flows](https://docs.langflow.org/components-models#use-language-model-components-in-flows).


## Pair models with vector stores [​](https://docs.langflow.org/components-models#pair-models-with-vector-stores)


By design, vector data is essential for LLM applications, such as chatbots and agents.


While you can use an LLM alone for generic chat interactions and common tasks, you can take your application to the next level with context sensitivity (such as RAG) and custom datasets (such as internal business data). This often requires integrating vector databases and vector searches that provide the additional context and define meaningful queries.


Langflow includes vector store components that can read and write vector data, including embedding storage, similarity search, Graph RAG traversals, and dedicated search instances like OpenSearch. Because of their interdependent functionality, it is common to use vector store, language model, and embedding model components in the same flow or in a series of dependent flows.


To find available vector store components, browse [**Bundles**](https://docs.langflow.org/components-bundle-components) or **Search** for your preferred vector database provider.


Example: Vector search flow


The following example demonstrates how to use vector store components in flows alongside related components like embedding model and language model components. These steps walk through important configuration details, functionality, and best practices for using these components effectively. This is only one example; it isn't a prescriptive guide to all possible use cases or configurations.


1. Create a flow with the **Vector Store RAG** template. This template has two subflows. The **Load Data** subflow loads embeddings and content into a vector database, and the **Retriever** subflow runs a vector search to retrieve relevant context based on a user's query.
2. Configure the database connection for both [**Astra DB** components](https://docs.langflow.org/bundles-datastax#astra-db), or replace them with another pair of vector store components of your choice. Make sure the components connect to the same vector store, and that the component in the **Retriever** subflow is able to run a similarity search. The parameters you set in each vector store component depend on the component's role in your flow. In this example, the **Load Data** subflow *writes* to the vector store, whereas the **Retriever** subflow *reads* from the vector store. Therefore, search-related parameters are only relevant to the **Vector Search** component in the **Retriever** subflow. For information about specific parameters, see the documentation for your chosen vector store component.
3. To configure the embedding model, do one of the following:
  - **Use an OpenAI model**: In both **OpenAI Embeddings** components, enter your OpenAI API key. You can use the default model or select a different OpenAI embedding model.
  - **Use another provider**: Replace the **OpenAI Embeddings** components with another pair of [embedding model components](https://docs.langflow.org/components-embedding-models) of your choice, and then configure the parameters and credentials accordingly.
  - **Use Astra DB vectorize**: If you are using an Astra DB vector store that has a vectorize integration, you can remove both **OpenAI Embeddings** components. If you do this, the vectorize integration automatically generates embeddings from the **Ingest Data** (in the **Load Data** subflow) and **Search Query** (in the **Retriever** subflow).4. Recommended: In the [**Split Text** component](https://docs.langflow.org/split-text), optimize the chunking settings for your embedding model. For example, if your embedding model has a token limit of 512, then the **Chunk Size** parameter must not exceed that limit. Additionally, because the **Retriever** subflow passes the chat input directly to the vector store component for vector search, make sure that your chat input string doesn't exceed your embedding model's limits. For this example, you can enter a query that is within the limits; however, in a production environment, you might need to implement additional checks or preprocessing steps to ensure compliance. For example, use additional components to prepare the chat input before running the vector search, or enforce chat input limits in your application code.
5. In the **Language Model** component, enter your OpenAI API key, or select a different provider and model to use for the chat portion of the flow.
6. Run the **Load Data** subflow to populate your vector store. In the **Read File** component, select one or more files, and then click **Run component** on the vector store component in the **Load Data** subflow. The **Load Data** subflow loads files from your local machine, chunks them, generates embeddings for the chunks, and then stores the chunks and their embeddings in the vector database. ![Embedding data into a vector store](https://docs.langflow.org/assets/images/vector-store-document-ingestion-6157311fb4d16e7f944d55254f0cc0e2.png) The **Load Data** subflow is separate from the **Retriever** subflow because you probably won't run it every time you use the chat. You can run the **Load Data** subflow as needed to preload or update the data in your vector store. Then, your chat interactions only use the components that are necessary for chat. If your vector store already contains data that you want to use for vector search, then you don't need to run the **Load Data** subflow.
7. Open the **Playground** and start chatting to run the **Retriever** subflow. The **Retriever** subflow generates an embedding from chat input, runs a vector search to retrieve similar content from your vector store, parses the search results into supplemental context for the LLM, and then uses the LLM to generate a natural language response to your query. The LLM uses the vector search results along with its internal training data and tools, such as basic web search and datetime information, to produce the response. ![Retrieval from a vector store](https://docs.langflow.org/assets/images/vector-store-retrieval-af7257d77ff0259ab1a0980641d464ce.png) To avoid passing the entire block of raw search results to the LLM, the **Parser** component extracts `text` strings from the search results `JSON` object, and then passes them to the **Prompt Template** component in `Message` format. From there, the strings and other template content are compiled into natural language instructions for the LLM. You can use other components for this transformation, such as the **JSON Operations** component, depending on how you want to use the search results. To view the raw search results, click **Inspect output** on the vector store component after running the **Retriever** subflow.


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)

- [Use language model components in flows](https://docs.langflow.org/components-models#use-language-model-components-in-flows)
- [Language model parameters](https://docs.langflow.org/components-models#language-model-parameters)
- [Language model output types](https://docs.langflow.org/components-models#language-model-output-types)
- [Additional language models](https://docs.langflow.org/components-models#additional-language-models)
- [Pair models with vector stores](https://docs.langflow.org/components-models#pair-models-with-vector-stores)[Manage Privacy Choices](https://docs.langflow.org/components-models#)

---

# Manage files | Langflow Documentation

`https://docs.langflow.org/concepts-file-management`

# Manage files

Files uploaded to Langflow file management are stored in Langflow's storage backend (local or AWS S3), and they are available to all of your flows.

Copy page ⌥C Version: 1.12.x On this page
## Use the file management UI​
## Upload and manage files with the Langflow API​
## Set the maximum file size​
## Use files in a flow​
## Upload images​
## Work with video files​
*For videos, see the Twelve Labs and YouTube  Bundles.*

## Configure file storage​
*For more information, see the AWS documentation.*

## File storage environment variables​
## See also​










Each Langflow server has a file management system where you can store files that you want to use in your flows.


Files uploaded to Langflow file management are stored in Langflow's [storage backend (local or AWS S3)](https://docs.langflow.org/concepts-file-management#configure-file-storage), and they are available to all of your flows.


Uploading files to Langflow file management keeps your files in a central location, and allows you to reuse files across flows without repeated manual uploads.


## Use the file management UI [​](https://docs.langflow.org/concepts-file-management#use-the-file-management-ui)


You can use the file management UI to upload files from your local machine to your own Langflow server. You can also manage all files that have been uploaded to your Langflow server.


1. Navigate to Langflow file management:
  - **Langflow Desktop**: In Langflow, on the [**Projects** page](https://docs.langflow.org/concepts-flows#projects) page, click **My Files** below the list of projects.
  - **Langflow OSS**: From a browser, navigate to your Langflow server's `/files` endpoint, such as `http://localhost:7860/files`. Modify the base URL as needed for your Langflow server.
  - **Backend-only**: For programmatic file management, use the [Langflow API files endpoints](https://docs.langflow.org/api-files). However, the following steps assume you're using the file management UI.2. On the **My Files** page, click **Upload**.
3. Select one or more files to upload.


After uploading files, you can rename, download, copy, or delete files within the file management UI. To delete a file, hover over a file's icon, select it, and then click **Delete**. You can delete multiple files in a single action. To download a file, hover over a file's icon, select it, and then click **Download**. If you download multiple files in a single action, they are saved together in a zip file.


## Upload and manage files with the Langflow API [​](https://docs.langflow.org/concepts-file-management#upload-and-manage-files-with-the-langflow-api)


With the Langflow API, you can upload and manage files in Langflow file management, and you can send files to flows programmatically at runtime.


For more information and examples, see [Files endpoints](https://docs.langflow.org/api-files) and [Create a chatbot that can ingest files](https://docs.langflow.org/chat-with-files).


## Set the maximum file size [​](https://docs.langflow.org/concepts-file-management#set-the-maximum-file-size)


By default, the maximum file size is 1024 MB. To modify this value, change the `LANGFLOW_MAX_FILE_SIZE_UPLOAD` [environment variable](https://docs.langflow.org/environment-variables).


## Use files in a flow [​](https://docs.langflow.org/concepts-file-management#use-files-in-a-flow)


To use files in your Langflow file management system in a flow, add a component that accepts file input to your flow, such as the **Read File** component.


For example, add a **Read File** component to your flow, click **Select files**, and then select files from the **My Files** list.


This list includes all files in your server's file management system, but you can only select [file types that are supported by the **Read File** component](https://docs.langflow.org/read-file). If you need another file type, you must use a different component that supports that file type, or you need to convert it to a supported type before uploading it.


For more information about the **Read File** component and other data loading components, see the [**Read file** component](https://docs.langflow.org/read-file).


### Load files at runtime [​](https://docs.langflow.org/concepts-file-management#load-files-at-runtime)


You can use preloaded files in your flows, and you can load files at runtime, if your flow accepts file input. To enable file input in your flow, do the following:


1. Add a [**Read File** component](https://docs.langflow.org/read-file) to your flow.
2. Select the **Read File** component, click **Parameters**, and then click **API** on the **Files** (path) field to expose it as a [`tweak`](https://docs.langflow.org/concepts-publish#input-schema).
3. Open **Share** > **API access**. The payload in each code snippet now includes `tweaks` with your **Read File** component's ID and the `path` key: ```json "tweaks": { "File-qYD5w": { "path": [] } } ```
4. When you run this flow programmatically, your script must upload a file to Langflow file management, and then pass the returned `file_path` to the `path` tweak in the `/run` request: ```json "tweaks": { "FILE_COMPONENT_ID": { "path": [ "file_path" ] } } ``` For a complete example see [Create a chatbot that can ingest files](https://docs.langflow.org/chat-with-files) and [Files endpoints](https://docs.langflow.org/api-files). If you want to upload multiple files, you can pass multiple `file_path` values in the `path` array, such as `[ "path1", "path2" ]`.


## Upload images [​](https://docs.langflow.org/concepts-file-management#upload-images)


Langflow supports base64 images in the following formats:


- PNG
- JPG/JPEG
- GIF
- BMP
- WebP


You can upload images to the **Playground** chat interface and as runtime input with the Langflow API.


- In the **Playground**, you can drag-and-drop images into the chat input area, or you can click the **Attach image** icon to select an image to upload.
- When you trigger a flow with the `/api/v1/run/$FLOW_ID` endpoint, you can use the `files` parameter to attach image data as a base64-encoded string: ```bash curl -X POST "http://$LANGFLOW_SERVER_ADDRESS/api/v1/run/$FLOW_ID" \ -H "Content-Type: application/json" \ -H "x-api-key: $LANGFLOW_API_KEY" \ -d '{ "session_id": "custom_session_123", "input_value": "What is in this image?", "input_type": "chat", "output_type": "chat", "files": ["data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA..."] }' ```


For more specialized image processing, browse [**Bundles**] or [create your own components](https://docs.langflow.org/components-custom-components).


## Work with video files [​](https://docs.langflow.org/concepts-file-management#work-with-video-files)


For videos, see the **Twelve Labs** and **YouTube** [**Bundles**](https://docs.langflow.org/components-bundle-components).


## Configure file storage [​](https://docs.langflow.org/concepts-file-management#configure-file-storage)


Langflow supports two storage backends for file management.


- **Local storage**: Langflow's default storage backend. Files are stored locally in your [Langflow configuration directory](https://docs.langflow.org/memory). Set `LANGFLOW_STORAGE_TYPE=local` or leave it unset to use local storage.
- **S3 storage**: Files are stored in an AWS S3 bucket. Langflow uses the [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) library to interact with S3.


To use S3 as your file storage backend, add the following configuration to your `.env` file:


```text
# S3 Storage Configuration
LANGFLOW_STORAGE_TYPE=s3
LANGFLOW_OBJECT_STORAGE_BUCKET_NAME=S3_BUCKET_NAME
LANGFLOW_OBJECT_STORAGE_PREFIX=S3_BUCKET_DIRECTORY

# AWS Credentials (required for S3)
AWS_ACCESS_KEY_ID=S3_ACCESS_KEY
AWS_SECRET_ACCESS_KEY=S3_ACCESS_SECRET_KEY
AWS_DEFAULT_REGION=S3_REGION
```


Replace the following placeholders with the actual values for your S3 instance:


- `S3_BUCKET_NAME`: The name of your S3 bucket.
- `S3_BUCKET_DIRECTORY`: An optional folder path within the bucket where files are stored, such as `s3://S3_BUCKET_NAME/S3_BUCKET_DIRECTORY`.
- `S3_ACCESS_KEY`: Your AWS Access Key ID.
- `S3_ACCESS_SECRET_KEY`: Your AWS Secret Access Key.
- `S3_REGION`: The AWS region where your bucket is located, such as `us-east-2`.


Your AWS credentials must have the necessary permissions to perform the required S3 operations for your use case, such as reading, writing, and deleting files in S3. This example policy allows basic CRUD operations on S3 objects.


```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "LangflowS3StorageAccess",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:GetObject",
                "s3:DeleteObject",
                "s3:ListBucket",
                "s3:PutObjectTagging",
            ],
            "Resource": [
                "arn:aws:s3:::S3_BUCKET_NAME",
                "arn:aws:s3:::S3_BUCKET_NAME/S3_BUCKET_DIRECTORY/*"
            ]
        }
    ]
}
```


Replace the following placeholders with the actual values for your IAM policy and S3 instance:


- `S3_BUCKET_NAME`: The name of your S3 bucket.
- `S3_BUCKET_DIRECTORY`: An optional folder path within the bucket where files are stored, such as `s3://S3_BUCKET_NAME/S3_BUCKET_DIRECTORY`.


For more information, see the [AWS documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html).


**Google Drive** storage is available through the [**Read File**](https://docs.langflow.org/read-file) and [**Write file**](https://docs.langflow.org/write-file) components, but you cannot use environment variables to configure it.


## File storage environment variables [​](https://docs.langflow.org/concepts-file-management#file-storage-environment-variables)


The following environment variables configure file storage backends for Langflow's file management system:


| Variable | Format | Default | Description |
| --- | --- | --- | --- |
| `LANGFLOW_​STORAGE_​TYPE` | String | `local` | Set the file storage backend. Supported values: `local` (files stored in the Langflow configuration directory) or `s3` (files stored in AWS S3). For S3 storage, you must also configure AWS credentials and bucket settings. |
| `LANGFLOW_​OBJECT_​STORAGE_​BUCKET_​NAME` | String | Not set | The name of the S3 bucket to use for file storage. Required when `LANGFLOW_​STORAGE_​TYPE=s3`. |
| `LANGFLOW_​OBJECT_​STORAGE_​PREFIX` | String | Not set | Optional prefix/folder path within the S3 bucket where files will be stored. If not set, files are stored at the bucket root. |
| `LANGFLOW_​OBJECT_​STORAGE_​TAGS` | JSON object | Not set | Optional S3 object tags applied to stored files when `LANGFLOW_​STORAGE_​TYPE=s3`. Ignored for local storage. Provided as a JSON map of string keys to string values, such as `{"env": "prod", "owner": "data-team"}`. |


## See also [​](https://docs.langflow.org/concepts-file-management#see-also)


- [Components reference](https://docs.langflow.org/concepts-components)


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)

- [Use the file management UI](https://docs.langflow.org/concepts-file-management#use-the-file-management-ui)
- [Upload and manage files with the Langflow API](https://docs.langflow.org/concepts-file-management#upload-and-manage-files-with-the-langflow-api)
- [Set the maximum file size](https://docs.langflow.org/concepts-file-management#set-the-maximum-file-size)
- [Use files in a flow](https://docs.langflow.org/concepts-file-management#use-files-in-a-flow)
  - [Load files at runtime](https://docs.langflow.org/concepts-file-management#load-files-at-runtime)- [Upload images](https://docs.langflow.org/concepts-file-management#upload-images)
- [Work with video files](https://docs.langflow.org/concepts-file-management#work-with-video-files)
- [Configure file storage](https://docs.langflow.org/concepts-file-management#configure-file-storage)
- [File storage environment variables](https://docs.langflow.org/concepts-file-management#file-storage-environment-variables)
- [See also](https://docs.langflow.org/concepts-file-management#see-also)[Manage Privacy Choices](https://docs.langflow.org/concepts-file-management#)

---

# Type Convert | Langflow Documentation

`https://docs.langflow.org/type-convert`

Copy page ⌥C Version: 1.12.x On this page

The **Type Convert** component converts data from one type to another. It supports `JSON`, `Table`, and `Message` data types.


- Data
- DataFrame
- Message


A `JSON` object is a structured object that contains a primary `text` key and other key-value pairs:


```json
"data": {
  "text": "User Profile",
  "name": "Charlie Lastname",
  "age": 28,
  "email": "charlie.lastname@example.com"
},
```


The larger context associated with a component's `data` dictionary also identifies which key is the primary `text_key`, and it can provide an optional default value if the primary key isn't specified. For example:


```json
{
  "text_key": "text",
  "data": {
    "text": "User Profile",
    "name": "Charlie Lastname",
    "age": 28,
    "email": "charlie.lastname@example.com"
  },
  "default_value": ""
}
```


A `Table` is an array that represents a tabular data structure with rows and columns.


It consists of a list (array) of dictionary objects, where each dictionary represents a row. Each key in the dictionaries corresponds to a column name. For example, the following `Table` contains two rows with columns for `name`, `age`, and `email`:


```json
[
  {
    "name": "Charlie Lastname",
    "age": 28,
    "email": "charlie.lastname@example.com"
  },
  {
    "name": "Bobby Othername",
    "age": 25,
    "email": "bobby.othername@example.com"
  }
]
```


A `Message` is primarily for passing a `text` string, such as `"Name: Charlie Lastname, Age: 28, Email: charlie.lastname@example.com"`. However, the entire `Message` object can include metadata about the message, particularly when used as chat input or output.


For more information, see [Langflow data types](https://docs.langflow.org/data-types).


## Use the Type Convert component in a flow [​](https://docs.langflow.org/type-convert#use-the-type-convert-component-in-a-flow)


The **Type Convert** component is typically used to transform data into a format required by a downstream component. For example, if a component outputs a `Message`, but the following component requires `JSON`, then you can use the **Type Convert** component to reformat the `Message` as `JSON` before passing it to the downstream component.


The following example uses the **Type Convert** component to convert the `Table` output from a **Web Search** component into `Message` data that is passed as text input for an LLM:


1. Create a flow based on the **Basic prompting** template.
2. Add a **Web Search** component to the flow, and then enter a search query, such as `environmental news`.
3. In the **Prompt Template** component, replace the contents of the **Template** field with the following text: ```text Answer the user's question using the {context} ``` The curly braces define a [prompt variable](https://docs.langflow.org/components-prompts#define-variables-in-prompts) that becomes an input field on the **Prompt Template** component. In this example, you will use the **context** field to pass the search results into the template, as explained in the next steps.
4. Add a **Type Convert** component to the flow, and then set the **Output Type** to **Message**. Because the **Web Search** component's `Table` output is incompatible with the **context** variable's `Message` input, you must use the **Type Convert** component to change the `Table` to a `Message` in order to pass the search results to the **Prompt Template** component.
*For more information, see Langflow data types.*

## Use the Type Convert component in a flow​
## Type Convert parameters​


5. Connect the additional components to the rest of the flow: ![Convert web search output to text input](https://docs.langflow.org/assets/images/component-type-convert-and-web-search-39a09775930134090eb60ff7f536b70e.png)
  - Connect the **Web Search** component's output to the **Type Convert** component's input.
  - Connect the **Type Convert** component's output to the **Prompt Template** component's **context** input.6. In the **Language Model** component, add your OpenAI API key. If you want to use a different provider or model, edit the **Model Provider**, **Model Name**, and **API Key** fields accordingly.
7. Click **Playground**, and then ask something relevant to your search query, such as `latest news` or `what's the latest research on the environment?`.


## Type Convert parameters [​](https://docs.langflow.org/type-convert#type-convert-parameters)


| Name | Display Name | Info |
| --- | --- | --- |
| input_data | Input Data | Input parameter. The data to convert. Accepts `JSON`, `Table`, or `Message` input. |
| output_type | Output Type | Input parameter. The desired output type, as one of **Data**, **DataFrame** or **Message**. |
| output | Output | Output parameter. The converted data in the specified format. The output port changes depending on the selected **Output Type**. |


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)

- [Use the Type Convert component in a flow](https://docs.langflow.org/type-convert#use-the-type-convert-component-in-a-flow)
- [Type Convert parameters](https://docs.langflow.org/type-convert#type-convert-parameters)[Manage Privacy Choices](https://docs.langflow.org/type-convert#)

---

# Langflow data types | Langflow Documentation

`https://docs.langflow.org/data-types`

# Langflow data types

In the workspace, hover over a port to see connection details for that port. Click a port to Search for compatible components.

Copy page ⌥C Version: 1.12.x On this page
## JSON​
*The schema is defined in data.py.*

## Table​
*Use the Table type to work with data containing multiple rows or records.*

*The schema is defined in dataframe.py.*

## Embeddings​
## LanguageModel​
## Memory​
*For more information, see the Message History component.*

## Message​
*Message data is structured as a JSON object.
For example:*

## Tool​
*Tool ports  connect tools to an Agent component.*

## Unknown or multiple types​
## View data types in flows​
## See also​











Langflow components are designed to accept and produce specific types of inputs and outputs. Input and output data types define the structure and flow of information between components. Understanding these structures helps you build applications that provide valid input and correctly anticipate the output format.


[Component ports](https://docs.langflow.org/concepts-components#component-ports) represent the data types that each component can send and receive. Some data types are self-evident from the fields they are attached to; for example, a **System Message** field accepts [message data](https://docs.langflow.org/data-types#message). [Port colors](https://docs.langflow.org/concepts-components#port-colors) also indicate the port's data type. For example **JSON** ports, represented by , either accept or emit [structured data objects](https://docs.langflow.org/data-types#json).


When building flows, connect output ports to input ports of the same type (color) to transfer that type of data between two components.


## JSON [​](https://docs.langflow.org/data-types#json)


**JSON** ports accept or produce the `JSON` type, which is a structured data object, like a JSON payload that you might send to an API. This data type is used to pass key-value pairs between components, such as user profiles, settings, or other structured information.


`JSON` objects include a primary text field, indicated by a `text_key`, and additional metadata.


### Schema and attributes [​](https://docs.langflow.org/data-types#schema-and-attributes)


The schema is defined in [`data.py`](https://github.com/langflow-ai/langflow/blob/main/src/lfx/src/lfx/schema/data.py).


The following attributes are available:


- `data`: A `JSON` object stores key-value pairs within the `.data` attribute. This is the `JSON` object's core dictionary. Each key is a field name, and the values can be any supported data type.
- `text_key`: The key in `data` that is considered the primary text value.
- `default_value`: Fallback if `text_key` is missing. The default `text_key` is `"text"`.


```python
data_obj = JSON(
    text_key="text",
    data={
        "text": "Hello world",
        "name": "Charlie",
        "age": 28
    },
    default_value=""
)
```


`JSON` objects can be serialized to JSON, created from JSON, or created from other dictionary data. However, the resulting `JSON` object is a structured object with validation and methods, not a plain dictionary. For example, when serialized into JSON, the previous Python example becomes the following JSON object:


```json
{
  "text_key": "text",
  "data": {
    "text": "Hello world",
    "name": "Charlie",
    "age": 28
  },
  "default_value": ""
}
```


## Table [​](https://docs.langflow.org/data-types#table)


**Table** ports accept or produce [pandas DataFrames](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html), which are similar to tabular CSV data.


Use the `Table` type to work with data containing multiple rows or records.


### Schema and attributes [​](https://docs.langflow.org/data-types#schema-and-attributes-1)


The schema is defined in [`dataframe.py`](https://github.com/langflow-ai/langflow/blob/main/src/lfx/src/lfx/schema/dataframe.py).


The following attributes are available:


- **Full pandas compatibility**: All pandas DataFrame methods and functionality are supported
- **Langflow integration**: Accepts lists of [`JSON` objects](https://docs.langflow.org/data-types#json), dictionaries, or existing DataFrames.
- **Convenience methods**:
  - `to_data_list()`
  - `add_row()`
  - `add_rows()`
  - `to_lc_documents()`
  - `to_data()`
  - `to_message()`- **Text key support**: Maintains `text_key` and `default_value` attributes for [`JSON` object](https://docs.langflow.org/data-types#json) compatibility.


### Table structure [​](https://docs.langflow.org/data-types#table-structure)


A Table has a tabular data structure with rows and columns. Keys are columns, and each object in the array is a row.


```json
[
  {
    "name": "Charlie Lastname",
    "age": 28,
    "email": "charlie.lastname@example.com"
  },
  {
    "name": "Alexandra Example",
    "age": 34,
    "email": "alexandra@example.com"
  }
]
```


When represented as tabular data, the preceding Table object is structured as follows:


```text
| name | age | email |
|------|-----|-------|
| Charlie Lastname | 28 | charlie.lastname@example.com |
| Alexandra Example | 34 | alexandra@example.com |
```


## Embeddings [​](https://docs.langflow.org/data-types#embeddings)


**Embeddings** ports emit or ingest vector embeddings to support functions like similarity search.


The `Embeddings` data type is used specifically by components that either produce or consume vector embeddings, such as the [embedding model components](https://docs.langflow.org/components-embedding-models) and vector store components.


For example, embedding model components output `Embeddings` data that you can connect to an **Embedding** input port on a vector store component.


For information about the underlying Python classes that produce `Embeddings`, see the [LangChain Embedding models documentation](https://docs.langchain.com/oss/python/integrations/text_embedding).


## LanguageModel [​](https://docs.langflow.org/data-types#languagemodel)


The `LanguageModel` type is a specific data type that can be produced by language model components and accepted by components that use an LLM.


When you change a language model component's output type from **Model Response** to **Language Model**, the component's output port changes from a **Message** port to a **Language Model** port . Then, you connect the outgoing **Language Model** port to a **Language Model** input port on a compatible component, such as a **Smart Transform** component.


For more information about using these components in flows and toggling `LanguageModel` output, see [Language model components](https://docs.langflow.org/components-models#language-model-output-types).


## Memory [​](https://docs.langflow.org/data-types#memory)


**Memory** ports are used to integrate a **Message History** component with external chat memory storage.


For more information, see the [**Message History** component](https://docs.langflow.org/message-history).


## Message [​](https://docs.langflow.org/data-types#message)


**Message** ports accept or produce `Message` data, which extends the [`JSON` type](https://docs.langflow.org/data-types#json) with additional fields and methods for text input typically used in chat flows.


This data type is used by many components.


### Schema, structure, and attributes [​](https://docs.langflow.org/data-types#schema-structure-and-attributes)


The `Message` schema is defined in [`message.py`](https://github.com/langflow-ai/langflow/blob/main/src/lfx/src/lfx/schema/message.py). Some `Message` attributes have their own schema definitions, such as [`content_block.py`](https://github.com/langflow-ai/langflow/blob/main/src/backend/base/langflow/schema/content_block.py).


`Message` data is structured as a JSON object. For example:


```json
{
  "text": "Name: Charlie Lastname, Age: 28, Email: charlie.lastname@example.com",
  "sender": "User",
  "sender_name": "Charlie Lastname",
  "session_id": "some-session-id",
  "timestamp": "2024-06-01T12:00:00Z",
  "files": [],
  "content_blocks": [],
  "category": "message"
}
```


The attributes included in a specific `Message` object depend on the context, including the component type, flow activity, and whether the message is a query or response. Some common attributes include the following:


- `text`: The main message content.
- `sender`: Identifies the originator of a chat message as either `User` or `Language Model`.
- `sender_name`: The display name for the sender. Defaults to `User` or `Language Model`.
- `session_id`: The chat [session identifier](https://docs.langflow.org/session-id).
- `flow_id`: The ID of the flow that the message is associated with. `flow_id` and `session_id` are the same if the flow doesn't use custom session IDs.
- `timestamp`: The UTC timestamp that the message was sent.
- `files`: A list of file paths or images included with the message
- `content_blocks`: Container for rich content input, such as text, media, or code. Also contains error message information if the LLM can't process the input.
- `category`: `"message"`, `"error"`, `"warning"`, or `"info"`.


Not all attributes are required, and some components accept message-compatible input, such as raw text input. The strictness depends on the component.


### Message data in Input and Output components [​](https://docs.langflow.org/data-types#message-data-in-input-and-output-components)


In flows with [**Chat Input and Output** components](https://docs.langflow.org/chat-input-and-output), `Message` data provides a consistent structure for chat interactions, and it is ideal for chatbots, conversational analysis, and other use cases based on a dialogue with an LLM or agent. In these flows, the **Playground** chat interface prints only the `Message` attributes that are relevant to the conversation, such as `text`, `files`, and error messages from `content_blocks`. To see all `Message` attributes, inspect the message logs in the **Playground**.


In flows with **Text Input and Output** components (now legacy), `Message` data is used to pass simple text strings without the chat-related metadata. These components handle `Message` data as independent text strings, not as part of an ongoing conversation. For this reason, a flow with only **Text Input and Output** components isn't compatible with the **Playground**. Replace them with the [**Chat Input and Output** components](https://docs.langflow.org/chat-input-and-output).


When using the Langflow API, the response includes the `Message` object along with other response data from the flow run. Langflow API responses can be extremely verbose, so your applications must include code to extract relevant data from the response to return to the user. For an example, see the [Langflow quickstart](https://docs.langflow.org/get-started-quickstart).


Additionally, input sent to the input port of input/output components does *not* need to be a complete `Message` object because the component constructs the `Message` object that is then passed to other components in the flow or returned as flow output. In fact, some components shouldn't receive a complete `Message` object because some attributes, like `timestamp` should be added by the component for accuracy.


## Tool [​](https://docs.langflow.org/data-types#tool)


**Tool** ports connect tools to an **Agent** component.


Tools can be other components where you enabled **Tool Mode**, they can be the dedicated **MCP Tools** component, or they can be other components that only support **Tool Mode**. Multiple tools can be connected to the same **Agent** component at the same port.


Functionally, `Tool` data is a LangChain `StructuredTool` object that can be used in agent flows.


For more information, see [Configure tools for agents](https://docs.langflow.org/agents-tools) and [Use Langflow as an MCP client](https://docs.langflow.org/mcp-client).


## Unknown or multiple types [​](https://docs.langflow.org/data-types#unknown-or-multiple-types)


If a port can accept or produce multiple data types, it is represented by the gray port icon .


Hover over the port to see the accepted or produced data types.


## View data types in flows [​](https://docs.langflow.org/data-types#view-data-types-in-flows)


In Langflow, you can use **Inspect output** to view the output of individual components. This can help you learn about the different data type and debug problems with invalid or malformed inputs and output.


The following example shows how to inspect the output of a [**Type Convert** component](https://docs.langflow.org/type-convert), which can convert data from one type to another:


1. Create a flow, and then connect a **Chat Input** component to a **Type Convert** component.
2. In the **Chat Input** component, enter some text for the type converter to process.
3. On the **Type Convert** component, click **Run component**, and then click **Inspect output**. The default output is `Message` data, which is the same as the input coming from the **Chat Input** component. To see the `Message` data converted to `JSON` or `Table`, change the **Output Type** on the **Type Convert** component, and then rerun the component. - Message - JSON - Table ```text Input text ``` ```json { "timestamp": "2025-07-15 20:56:20 UTC", "sender": "User", "sender_name": "User", "session_id": "a0c7e888-4fd6-4242-b8c8-e761ad690aeb", "text": "", "files": [], "error": false, "edit": false, "properties": { "text_color": "", "background_color": "", "edited": false, "source": { "id": null, "display_name": null, "source": null }, "icon": "", "allow_markdown": false, "positive_feedback": null, "state": "complete", "targets": [] }, "category": "message", "content_blocks": [], "id": "9da72da2-efbb-4ccd-90ad-b32429b0418e", "flow_id": "a0c7e888-4fd6-4242-b8c8-e761ad690aeb", "duration": null } ``` ```text | Field | Value | |-------|-------| | timestamp | 2025-07-15 20:56:11 UTC | | sender | User | | sender_name | User | | session_id | a0c7e888-4fd6-4242-b8c8-e761ad690aeb | | text | (empty) | | files | [] | | error | False | | edit | False | | properties | text_color: '', background_color: '', edited: False, source: {id: None, display_name: None, source: None}, icon: '', allow_markdown: False, positive_feedback: None, state: 'complete', targets: [] | | category | message | | content_blocks | [] | | id | 341686eb-7a39-4b80-a90a-d8bf267815ef | | flow_id | a0c7e888-4fd6-4242-b8c8-e761ad690aeb | | duration | (empty) | ```


## See also [​](https://docs.langflow.org/data-types#see-also)


- [Custom components](https://docs.langflow.org/components-custom-components)
- [Pydantic Models](https://docs.pydantic.dev/latest/api/base_model/)
- [pandas.DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)

- [JSON](https://docs.langflow.org/data-types#json)
  - [Schema and attributes](https://docs.langflow.org/data-types#schema-and-attributes)- [Table](https://docs.langflow.org/data-types#table)
  - [Schema and attributes](https://docs.langflow.org/data-types#schema-and-attributes-1)
  - [Table structure](https://docs.langflow.org/data-types#table-structure)- [Embeddings](https://docs.langflow.org/data-types#embeddings)
- [LanguageModel](https://docs.langflow.org/data-types#languagemodel)
- [Memory](https://docs.langflow.org/data-types#memory)
- [Message](https://docs.langflow.org/data-types#message)
  - [Schema, structure, and attributes](https://docs.langflow.org/data-types#schema-structure-and-attributes)
  - [Message data in Input and Output components](https://docs.langflow.org/data-types#message-data-in-input-and-output-components)- [Tool](https://docs.langflow.org/data-types#tool)
- [Unknown or multiple types](https://docs.langflow.org/data-types#unknown-or-multiple-types)
- [View data types in flows](https://docs.langflow.org/data-types#view-data-types-in-flows)
- [See also](https://docs.langflow.org/data-types#see-also)[Manage Privacy Choices](https://docs.langflow.org/data-types#)

---

# Prompt Template | Langflow Documentation

`https://docs.langflow.org/components-prompts`

Copy page ⌥C Version: 1.12.x On this page

Use the **Prompt Template** core component to create a *prompt* that supplies instructions and context to an LLM or agent, separate from other input like chat messages and file uploads.
## Prompt Template parameters​
## Define variables in prompts​
## See also​





Prompts are structured input that use natural language, fixed values, and dynamic variables to provide baseline context for the LLM. For example:


- Define a consistent structure for user queries, making it easier for the LLM to understand and respond appropriately.
- Define a specific output format for the LLM, such as JSON or structured text.
- Define a role for the LLM, such as `You are a helpful assistant` or `You are an expert in microbiology`.
- Allow the LLM to reference chat memory.


The **Prompt Template** component can also output variable instructions to other components later in the flow.


## Prompt Template parameters [​](https://docs.langflow.org/components-prompts#prompt-template-parameters)


Name

Display Name

Description

template

Template

Input parameter. Create a prompt template with dynamic variables in curly braces, such as `{VARIABLE_​NAME}`.

If your template includes literal text and variables, you can use double curly braces to escape literal curly braces in the template and prevent interpretation of that text as a variable. For example: `This is a template with {{literal text in curly braces}} and a {variable}`.


If your template contains many literal curly braces, such as JSON structures, consider using Mustache templating instead. For more information, see [Use Mustache templating in prompt templates](https://docs.langflow.org/components-prompts#use-mustache-templating-in-prompt-templates).

use_double_brackets

Use Double Brackets

When enabled, use Mustache syntax `{{variable}}` instead of f-string syntax `{variable}`. For more information, see [Use Mustache templating in prompt templates](https://docs.langflow.org/components-prompts#use-mustache-templating-in-prompt-templates).


## Define variables in prompts [​](https://docs.langflow.org/components-prompts#define-variables-in-prompts)


Variables in a **Prompt Template** component dynamically add fields to the **Prompt Template** component so that your flow can receive definitions for those values from other components, Langflow global variables, or fixed input.


For example, with the [**Message History** component](https://docs.langflow.org/message-history), you can use a `{memory}` variable to pass chat history to the prompt. However, the **Agent** component includes built-in chat memory that is enabled by default. For more information, see [Memory management options](https://docs.langflow.org/memory).


The following steps demonstrate how to add variables to a **Prompt Template** component:


1. Create a flow based on the **Basic prompting** template. This template already has a **Prompt Template** component, but the template only contains natural language instructions: `Answer the user as if you were a GenAI expert, enthusiastic about helping them get started building something fresh.` This prompt defines a role for the LLM's chat interactions, but it doesn't include variables that help you create prompts that adapt dynamically to changing contexts, such as different users and environments.
2. Click the **Prompt Template** component, and then add some variables to the **Template** field. Variables are declared by wrapping the variable name in curly braces, like `{variable_name}`. For example, the following template creates `context` and `user_question` variables: ```text Given the context: {context} Answer the question: {user_question} ``` If your template includes literal text and variables, you can use double curly braces to escape literal curly braces in the template and prevent interpretation of that text as a variable. For example: `This is a template with {{literal text in curly braces}} and a {variable}`. If your template contains many literal curly braces, such as JSON structures, consider using Mustache templating instead. For more information, see [Use Mustache templating in prompt templates](https://docs.langflow.org/components-prompts#use-mustache-templating-in-prompt-templates).
3. Click **Check & Save** to save the template. After adding the variables to the template, new fields are added to the **Prompt Template** component for each variable.
4. Provide input for the variable fields:
  - Connect the fields to other components to pass the output from those components to the variables.
  - Use Langflow global variables.
  - Enter fixed values directly into the fields.


You can add as many variables as you like in your template. For example, you could add variables for `{references}` and `{instructions}`, and then feed that information in from other components, such as **Text Input**, **URL**, or **Read File** components.


### Use Mustache templating in prompt templates [​](https://docs.langflow.org/components-prompts#use-mustache-templating-in-prompt-templates)


F-string escaping can become confusing when you mix escaped braces with variables in the same template. For example:


```text
Generate a response in this JSON format:
{{"name": "{name}", "age": {age}, "city": "{city}"}}

The user's name is {name}, age is {age}, and they live in {city}.
```


The characters `{{` and `}}` are escaped literal braces for the JSON structure, but `{name}` is a variable. This can make prompts error-prone and difficult to parse. Use [Mustache](https://mustache.github.io) in your prompt templates to make the differences clearer.


To enable Mustache templating, do the following:


1. In the **Prompt Template** component, enable **Use Double Brackets**.
2. In your prompt template, change the variables from `{variable}` to `{{variable}}`. Mustache uses `{` `}` for literal braces and `{{variable}}` for variables. ```text Generate a response in this JSON format: {"name": "{{name}}", "age": {{age}}, "city": "{{city}}"} The user's name is {{name}}, age is {{age}}, and they live in {{city}}. ```
3. Click **Check & Save**. The component lints the template code and returns **Prompt is ready** if there are no errors. Your prompt is now ready to use in a flow.


Langflow supports variable replacement with double brackets, but does not support the full Mustache engine. The prompt component validation rejects syntax for other Mustache features such as loops and conditionals.


## See also [​](https://docs.langflow.org/components-prompts#see-also)


- [**LangChain Prompt Hub** component](https://docs.langflow.org/bundles-langchain#prompt-hub)
- [Processing components](https://docs.langflow.org/concepts-components)


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)

- [Prompt Template parameters](https://docs.langflow.org/components-prompts#prompt-template-parameters)
- [Define variables in prompts](https://docs.langflow.org/components-prompts#define-variables-in-prompts)
  - [Use Mustache templating in prompt templates](https://docs.langflow.org/components-prompts#use-mustache-templating-in-prompt-templates)- [See also](https://docs.langflow.org/components-prompts#see-also)[Manage Privacy Choices](https://docs.langflow.org/components-prompts#)

---

# Create a vector RAG chatbot | Langflow Documentation

`https://docs.langflow.org/chat-with-rag`

# Create a vector RAG chatbot

In Langflow, click New Flow, and then select the Vector Store RAG template.

Copy page ⌥C Version: 1.12.x On this page
## Prerequisites​
## Create a vector RAG flow​
## Load data and generate embeddings​
## Chat with your flow from a JavaScript application​
## Next steps​






This tutorial demonstrates how you can use Langflow to create a chatbot application that uses Retrieval Augmented Generation (RAG) to embed your data as vectors in a vector database, and then chat with the data.


## Prerequisites [​](https://docs.langflow.org/chat-with-rag#prerequisites)


- [Install and start Langflow](https://docs.langflow.org/get-started-installation)
- Create a [Langflow API key](https://docs.langflow.org/api-keys-and-authentication)
- Create an [OpenAI API key](https://platform.openai.com/api-keys)
- Install the [Langflow JavaScript client](https://docs.langflow.org/typescript-client)
- Be familiar with vector search concepts and applications, such as vector databases and RAG


## Create a vector RAG flow [​](https://docs.langflow.org/chat-with-rag#create-a-vector-rag-flow)


1. In Langflow, click **New Flow**, and then select the **Vector Store RAG** template.
2. Add your **OpenAI** API key to both **OpenAI Embeddings** components.
3. Optional: Replace both **Astra DB** vector store components with a **Chroma DB** or another vector store component of your choice. This tutorial uses Chroma DB. The **Load Data Flow** should have **Read File**, **Split Text**, **Embedding Model**, vector store (such as **Chroma DB**), and **Chat Output** components: ![File loader chat flow](https://docs.langflow.org/assets/images/tutorial-chatbot-embed-files-6157311fb4d16e7f944d55254f0cc0e2.png) The **Retriever Flow** should have **Chat Input**, **Embedding Model**, vector store, **Parser**, **Prompt**, **Language Model**, and **Chat Output** components: ![Chat with RAG flow](https://docs.langflow.org/assets/images/tutorial-chatbot-chat-flow-af7257d77ff0259ab1a0980641d464ce.png) The flows are ready to use. Continue the tutorial to learn how to use the loading flow to load data into your vector store, and then call the chat flow in a chatbot application.


## Load data and generate embeddings [​](https://docs.langflow.org/chat-with-rag#load-data-and-generate-embeddings)


To load data and generate embeddings, you can use the visual editor or the `/v2/files` endpoint.


The visual editor option is simpler, but it is only recommended for scenarios where the user who created the flow is the same user who loads data into the database.


In situations where many users load data or you need to load data programmatically, use the Langflow API option.


- Visual editor
- Langflow API


1. In your RAG chatbot flow, click the **Read File** component, and then click **File**.
2. Select the local file you want to upload, and then click **Open**. The file is loaded to your Langflow server.
3. To load the data into your vector database, click the vector store component, and then click **Run component** to run the selected component and all prior dependent components.


To load data programmatically, use the `/v2/files/` and `/v1/run/$FLOW_ID` endpoints. The first endpoint loads a file to your Langflow server, and then returns an uploaded file path. The second endpoint runs the **Load Data Flow**, referencing the uploaded file path, to chunk, embed, and load the data into the vector store.


The following script demonstrates this process.


```js
// Node 18+ example using global fetch, FormData, and Blob
import fs from 'fs/promises';

// 1. Prepare the form data with the file to upload
const fileBuffer = await fs.readFile('FILE_NAME');
const data = new FormData();
data.append('file', new Blob([fileBuffer]), 'FILE_NAME');
const headers = { 'x-api-key': 'LANGFLOW_API_KEY' };

// 2. Upload the file to Langflow
const uploadRes = await fetch('LANGFLOW_SERVER_ADDRESS/api/v2/files/', {
  method: 'POST',
  headers,
  body: data
});
const uploadData = await uploadRes.json();
const uploadedPath = uploadData.path;

// 3. Call the Langflow run endpoint with the uploaded file path
const payload = {
  input_value: "Analyze this file",
  output_type: "chat",
  input_type: "text",
  tweaks: {
    'FILE_COMPONENT_NAME': {
      path: uploadedPath
    }
  }
};
const runRes = await fetch('LANGFLOW_SERVER_ADDRESS/api/v1/run/FLOW_ID', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json', 'x-api-key': 'LANGFLOW_API_KEY' },
  body: JSON.stringify(payload)
});
const langflowData = await runRes.json();
// Output only the message
console.log(langflowData.outputs?.[0]?.outputs?.[0]?.results?.message?.data?.text);
```


When the flow runs, the flow ingests the selected file, chunks the data, loads the data into the vector store database, and then generates embeddings for the chunks, which are also stored in the vector store.


Your database now contains data with vector embeddings that an LLM can use as context to respond to queries, as demonstrated in the next section of the tutorial.


## Chat with your flow from a JavaScript application [​](https://docs.langflow.org/chat-with-rag#chat-with-your-flow-from-a-javascript-application)


To chat with the data in your vector database, create a chatbot application that runs the **Retriever Flow** programmatically.


This tutorial uses JavaScript for demonstration purposes.


1. To construct the chatbot, gather the following information:
  - `LANGFLOW_SERVER_ADDRESS`: Your Langflow server's domain. The default value is `127.0.0.1:7860`. You can get this value from the code snippets on your flow's [**API access** pane](https://docs.langflow.org/concepts-publish#api-access).
  - `FLOW_ID`: Your flow's UUID or custom endpoint name. You can get this value from the code snippets on your flow's [**API access** pane](https://docs.langflow.org/concepts-publish#api-access).
  - `LANGFLOW_API_KEY`: A valid [Langflow API key](https://docs.langflow.org/api-keys-and-authentication).2. Copy the following script into a JavaScript file, and then replace the placeholders with the information you gathered in the previous step: ```js const readline = require('readline'); const { LangflowClient } = require('@datastax/langflow-client'); # pragma: allowlist nextline secret const API_KEY = 'LANGFLOW_API_KEY'; const SERVER = 'LANGFLOW_SERVER_ADDRESS'; const FLOW_ID = 'FLOW_ID'; const rl = readline.createInterface({ input: process.stdin, output: process.stdout }); // Initialize the Langflow client const client = new LangflowClient({ baseUrl: SERVER, apiKey: API_KEY }); async function sendMessage(message) { try { const response = await client.flow(FLOW_ID).run(message, { session_id: 'user_1' }); // Use the convenience method to get the chat output text return response.chatOutputText() || 'No response'; } catch (error) { return `Error: ${error.message}`; } } function chat() { console.log('🤖 Langflow RAG Chatbot (type "quit" to exit)\n'); const ask = () => { rl.question('👤 You: ', async (input) => { if (['quit', 'exit', 'bye'].includes(input.trim().toLowerCase())) { console.log('👋 Goodbye!'); rl.close(); return; } const response = await sendMessage(input.trim()); console.log(`🤖 Assistant: ${response}\n`); ask(); }); }; ask(); } chat(); ``` The script creates a Node application that chats with the content in your vector database, using the `chat` input and output types to communicate with your flow. Chat maintains ongoing conversation context across multiple messages. If you used `text` type inputs and outputs, each request is a standalone text string.
3. Save and run the script to send the requests and test the flow.


## Next steps [​](https://docs.langflow.org/chat-with-rag#next-steps)


For more information on building or extending this tutorial, see the following:


- [Model Context Protocol (MCP) servers](https://docs.langflow.org/mcp-server)
- [Langflow deployment overview](https://docs.langflow.org/deployment-overview)


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)

- [Prerequisites](https://docs.langflow.org/chat-with-rag#prerequisites)
- [Create a vector RAG flow](https://docs.langflow.org/chat-with-rag#create-a-vector-rag-flow)
- [Load data and generate embeddings](https://docs.langflow.org/chat-with-rag#load-data-and-generate-embeddings)
- [Chat with your flow from a JavaScript application](https://docs.langflow.org/chat-with-rag#chat-with-your-flow-from-a-javascript-application)
- [Next steps](https://docs.langflow.org/chat-with-rag#next-steps)[Manage Privacy Choices](https://docs.langflow.org/chat-with-rag#)

---

# Structured Output | Langflow Documentation

`https://docs.langflow.org/structured-output`

Copy page ⌥C Version: 1.12.x On this page

The **Structured Output** component uses an LLM to transform any input into structured data (`JSON` or `Table`) using natural language formatting instructions and an output schema definition. For example, you can extract specific details from documents, like email messages or scientific papers.


## Use the Structured Output component in a flow [​](https://docs.langflow.org/structured-output#use-the-structured-output-component-in-a-flow)


To use the **Structured Output** component in a flow, do the following:


1. Provide an **Input Message**, which is the source material from which you want to extract structured data. This can come from practically any component, but it is typically a **Chat Input**, **Read File**, or other component that provides some unstructured or semi-structured input.
## Use the Structured Output component in a flow​
## Structured Output parameters​


2. Define **Format Instructions** and an **Output Schema** to specify the data to extract from the source material and how to structure it in the final `JSON` or `Table` output. The instructions are a prompt that tell the LLM what data to extract, how to format it, how to handle exceptions, and any other instructions relevant to preparing the structured data. The schema is a table that defines the fields (keys) and data types to organize the data extracted by the LLM into a structured `JSON` or `Table` object. For more information, see [Output Schema options](https://docs.langflow.org/structured-output#output-schema-options)
3. Attach a [language model component](https://docs.langflow.org/components-models) that is set to emit [`LanguageModel`](https://docs.langflow.org/data-types#languagemodel) output. The LLM uses the **Input Message** and **Format Instructions** from the **Structured Output** component to extract specific pieces of data from the input text. The output schema is applied to the model's response to produce the final `JSON` or `Table` structured object.
4. Optional: Typically, the structured output is passed to downstream components that use the extracted data for other processes, such as the **Parser** or **Data Operations** components.


![A basic flow with Structured Output, Language Model, Type Convert, and Chat Input and Output components.](https://docs.langflow.org/assets/images/component-structured-output-23458b0d29eed6d092b557c7aaf6ab2c.png)


## Structured Output parameters [​](https://docs.langflow.org/structured-output#structured-output-parameters)


Some parameters are hidden by default in the visual editor. You can modify all component parameters through the [component inspection panel](https://docs.langflow.org/concepts-components#component-inspection-panel) that appears when you select a component.


| Name | Type | Description |
| --- | --- | --- |
| Language Model (`llm`) | `LanguageModel` | Input parameter. The [`LanguageModel`](https://docs.langflow.org/data-types#languagemodel) output from a **Language Model** component that defines the LLM to use to analyze, extract, and prepare the structured output. |
| Input Message (`input_​value`) | String | Input parameter. The input message containing source material for extraction. |
| Format Instructions (`system_​prompt`) | String | Input parameter. The instructions to the language model for extracting and formatting the output. |
| Schema Name (`schema_​name`) | String | Input parameter. An optional title for the **Output Schema**. |
| Output Schema (`output_​schema`) | Table | Input parameter. A table describing the schema of the desired structured output, ultimately determining the content of the `JSON` or `Table` output. See [Output Schema options](https://docs.langflow.org/structured-output#output-schema-options). |
| Structured Output (`structured_​output`) | `JSON` or `Table` | Output parameter. The final structured output produced by the component. Near the component's output port, you can select the output data type as either **Structured Output Data** or **Structured Output DataFrame**. The specific content and structure of the output depends on the input parameters. |


#### Output Schema options [​](https://docs.langflow.org/structured-output#output-schema-options)


After the LLM extracts the relevant data from the **Input Message** and **Format Instructions**, the data is organized according to the **Output Schema**.


The schema is a table that defines the fields (keys) and data types for the final `JSON` or `Table` output from the **Structured Output** component.


The default schema is a single `field` string.


To add a key to the schema, click **Add a new row**, and then edit each column to define the schema:


- **Name**: The name of the output field. Typically a specific key for which you want to extract a value. You can reference these keys as variables in downstream components, such as a **Parser** component's template. For example, the schema key `NET_INCOME` could be referenced by the variable `{NET_INCOME}`.
- **Description**: An optional metadata description of the field's contents and purpose.
- **Type**: The data type of the value stored in the field. Supported types are `str` (default), `int`, `float`, `bool`, and `dict`.
- **As List**: Enable this setting if you want the field to contain a list of values rather than a single value.


For simple schemas, you might only extract a few `string` or `int` fields. For more complex schemas with lists and dictionaries, it might help to refer to the `JSON` and `Table` structures and attributes, as described in [Langflow data types](https://docs.langflow.org/data-types). You can also emit a rough `JSON` or `Table`, and then use downstream components for further refinement, such as a **Data Operations** component.


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)

- [Use the Structured Output component in a flow](https://docs.langflow.org/structured-output#use-the-structured-output-component-in-a-flow)
- [Structured Output parameters](https://docs.langflow.org/structured-output#structured-output-parameters)[Manage Privacy Choices](https://docs.langflow.org/structured-output#)

---

# API Request | Langflow Documentation

`https://docs.langflow.org/api-request`

Copy page ⌥C Version: 1.12.x On this page

The **API Request** component constructs and sends HTTP requests using URLs or curl commands:


- **URL mode**: Enter one or more comma-separated URLs, and then select the method for the request to each URL.
- **curl mode**: Enter the curl command to execute.
*Returns a JSON object containing the response.*

*For provider-specific API components, see  Bundles.*

## API Request parameters​



You can enable additional request options and fields in the component's parameters.


Returns a [`JSON` object](https://docs.langflow.org/data-types#json) containing the response.


For provider-specific API components, see [**Bundles**](https://docs.langflow.org/components-bundle-components).


## API Request parameters [​](https://docs.langflow.org/api-request#api-request-parameters)


Some parameters are hidden by default in the visual editor. You can modify all component parameters through the [component inspection panel](https://docs.langflow.org/concepts-components#component-inspection-panel) that appears when you select a component.


| Name | Display Name | Info |
| --- | --- | --- |
| mode | Mode | Input parameter. Set the mode to either **URL** or **curl**. |
| urls | URL | Input parameter. Enter one or more comma-separated URLs for the request. |
| curl | curl | Input parameter. **curl mode** only. Enter a complete curl command. Other component parameters are populated from the command arguments. |
| method | Method | Input parameter. The HTTP method to use. |
| query_params | Query Parameters | Input parameter. The query parameters to append to the URL. |
| body | Body | Input parameter. The body to send with POST, PATCH, and PUT requests as a dictionary. |
| headers | Headers | Input parameter. The headers to send with the request as a dictionary. |
| timeout | Timeout | Input parameter. The timeout to use for the request. |
| follow_redirects | Follow Redirects | Input parameter. Whether to follow HTTP redirects. Starting in Langflow version 1.7, the **Follow Redirects** parameter is disabled (`false`) by default to prevent SSRF bypass attacks where a public URL redirects to internal resources. Only enable redirects if you trust the target server. For more information, see [SSRF protection environment variables](https://docs.langflow.org/api-keys-and-authentication#ssrf-protection). |
| save_to_file | Save to File | Input parameter. Whether to save the API response to a temporary file. Default: Disabled (`false`) |
| include_httpx_metadata | Include HTTPx Metadata | Input parameter. Whether to include properties such as `headers`, `status_​code`, `response_​headers`, and `redirection_​history` in the output. Default: Disabled (`false`) |


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)

- [API Request parameters](https://docs.langflow.org/api-request#api-request-parameters)[Manage Privacy Choices](https://docs.langflow.org/api-request#)

---

# LFX and Langflow version compatibility | Langflow Documentation

`https://docs.langflow.org/lfx-compatibility`

# LFX and Langflow version compatibility
## Compatibility contract​
*LFX X.Y.N is guaranteed compatible with any flow exported from Langflow X.Y.M.*

## Compatibility matrix​
## Check and upgrade flows with lfx upgrade​
## Inline compatibility checking with --upgrade-flow​
## Pin versions​
## Migrating from LFX 0.5.x to 1.10.0​
## Engine-only LFX and lfx[bundles]​








Langflow and LFX are versioned together on the same major.minor line, so you can always tell which LFX release runs which flows.

Copy page ⌥C Version: 1.12.x On this page

Langflow and LFX are versioned together on the same `major.minor` line, so you can always tell which LFX release runs which flows.


## Compatibility contract [​](https://docs.langflow.org/lfx-compatibility#compatibility-contract)


**LFX `X.Y.N` is guaranteed compatible with any flow exported from Langflow `X.Y.M`.**


The major and minor numbers must match. The patches `.N` for LFX and `.M` for Langflow are released independently. An LFX patch fix does not require a Langflow patch release, and vice versa.


When LFX and a flow share the same `major` version but differ on `minor`, such as a flow exported from Langflow 1.9.x run with LFX 1.10.x, individual components may have been updated since the flow was saved. Use `lfx upgrade` to check compatibility and apply safe automatic fixes before running or serving such a flow. For more information, see [Check and upgrade flows with lfx upgrade](https://docs.langflow.org/lfx-compatibility#check-and-upgrade-flows-with-lfx-upgrade).


## Compatibility matrix [​](https://docs.langflow.org/lfx-compatibility#compatibility-matrix)


| Langflow version | Compatible LFX version | Notes |
| --- | --- | --- |
| 1.10.x | 1.10.x | Fully compatible. Same `major.minor` line. |
| 1.11.x | 1.11.x | Fully compatible. Same `major.minor` line. |
| 1.9.x or earlier | 1.10.x | Use `lfx upgrade --upgrade-flow=safe` to apply safe component schema upgrades before running. |
| Any 1.x.x | 0.5.x | LFX 0.5.x was a standalone release before version alignment. It is no longer compatible with Langflow 1.10+ flows. |


## Check and upgrade flows with `lfx upgrade` [​](https://docs.langflow.org/lfx-compatibility#check-and-upgrade-flows-with-lfx-upgrade)


The `lfx upgrade` command inspects a flow against the built-in component registry and reports any components that have become incompatible or that have safe automatic upgrades available.


`lfx upgrade` compares each component in the flow against a bundled index at `_assets/component_index.json` that ships with the LFX release.


Run it with no flags to get a read-only compatibility report. The command reads your flow JSON, walks through every component node, and prints one line per node with its status. It does not modify the file.


```bash
lfx upgrade my-flow.json
```


Example output:


```text
  [SAFE] Agent (AgentComponent) - id: abc123
  [OK] Chat Output (ChatOutput) - id: def456
```


| CLI output | What it means | Example |
| --- | --- | --- |
| `[OK]` | Component matches the current registry. | No action needed. |
| `[SAFE]` | Component code changed, but ports and fields your flow uses still line up. `lfx upgrade --write` can apply this update automatically. | An output that previously emitted only `Message` now also supports `Data`. |
| `[BREAKING]` | A port or field your flow relies on was removed. | An input that accepted `Message` and `Data` now accepts only `Message` and your flow uses a `Data` component. |
| `[BLOCKED]` | The component type no longer exists in this LFX build. | A bundle-only component is not installed in your environment. |


To apply fixes or enforce stricter checks, run:


```bash
# Apply all safe upgrades and overwrite the file
lfx upgrade my-flow.json --write

# Fail if any safe upgrades are still pending (use after a dry run before running `--write`)
lfx upgrade my-flow.json --strict
```


## Inline compatibility checking with `--upgrade-flow` [​](https://docs.langflow.org/lfx-compatibility#inline-compatibility-checking-with---upgrade-flow)


Both `lfx run` and `lfx serve` accept an `--upgrade-flow` option so you can apply compatibility checks at execution without a separate `lfx upgrade` step.


```bash
# Check only — fail if any component is blocked
lfx run my-flow.json --upgrade-flow=check "Hello world"

# Apply safe upgrades in memory, then run
lfx run my-flow.json --upgrade-flow=safe "Hello world"

# Same options for serve
lfx serve my-flow.json --upgrade-flow=safe
```


| Mode | Behavior |
| --- | --- |
| `check` | Reports compatibility issues and exits non-zero if any component is blocked. No changes are written to disk. |
| `safe` | Applies all safe upgrades in memory, then runs or serves the flow. Blocked components still cause a non-zero exit. |


## Pin versions [​](https://docs.langflow.org/lfx-compatibility#pin-versions)


Pin `lfx~=1.10.0` in `requirements.txt` to track all patch releases for a given Langflow minor without crossing into the next minor automatically.


```text
# requirements.txt — allows 1.10.1, 1.10.2, … but not 1.11.0
lfx~=1.10.0
```


## Migrating from LFX 0.5.x to 1.10.0 [​](https://docs.langflow.org/lfx-compatibility#migrating-from-lfx-05x-to-1100)


LFX was realigned from its standalone `0.5.x` line onto Langflow's `major.minor` line, so the version number jumps from `0.5.0` to `1.10.0` in one release. This is a version-numbering change, not 95 minor releases of new features.


This jump can affect existing dependency pins in unexpected ways:


| Pin style | Effect |
| --- | --- |
| `lfx==0.5.x` or `lfx<1.0` | Does not upgrade. The deployment stays on 0.5.x. |
| `lfx>=0.5,<1` | Does not upgrade. The upper bound excludes 1.10.0. |
| `lfx>=0.5` (no upper bound) | Upgrades automatically to 1.10.0 on the next install. |


Going forward, pin with `lfx~=1.10.0` so you receive compatible patches without silently crossing minor lines.


## Engine-only LFX and `lfx[bundles]` [​](https://docs.langflow.org/lfx-compatibility#engine-only-lfx-and-lfxbundles)


`pip install lfx` installs the engine only — no component bundles. For headless or serverless deployments that execute flows using provider components without the full Langflow server, install `lfx-bundles` alongside the engine:


```bash
uv pip install "lfx[bundles]"
```


This is equivalent to installing `lfx` plus `lfx-bundles[all]`, including the PyTorch-based providers **CUGA** and **Code Agents**. It does **not** install standalone packages such as `lfx-openai` or `lfx-exa`. `uv pip install langflow` installs the curated standalone `lfx-*` packages without `lfx-bundles`. Use `uv pip install "langflow[bundles]"` to add the `lfx-bundles[all-no-torch]` profile plus the opt-in standalone packages while keeping the full Langflow application torch-free. For the providers omitted from the default install, see [Additional bundles](https://docs.langflow.org/extensions-bundle-list#additional-bundles). For a slimmer image, install only the provider packages a deployment actually executes, for example `uv pip install lfx lfx-openai "lfx-bundles[qdrant]"`. There is intentionally no `lfx[all]` extra. Install `lfx-bundles` explicitly, or install only the provider extras you need to avoid the full torch-inclusive `[all]` set. Some components require a [torch opt-in install](https://docs.langflow.org/components-bundle-components#torch-opt-in).


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)

- [Compatibility contract](https://docs.langflow.org/lfx-compatibility#compatibility-contract)
- [Compatibility matrix](https://docs.langflow.org/lfx-compatibility#compatibility-matrix)
- [Check and upgrade flows with `lfx upgrade`](https://docs.langflow.org/lfx-compatibility#check-and-upgrade-flows-with-lfx-upgrade)
- [Inline compatibility checking with `--upgrade-flow`](https://docs.langflow.org/lfx-compatibility#inline-compatibility-checking-with---upgrade-flow)
- [Pin versions](https://docs.langflow.org/lfx-compatibility#pin-versions)
- [Migrating from LFX 0.5.x to 1.10.0](https://docs.langflow.org/lfx-compatibility#migrating-from-lfx-05x-to-1100)
- [Engine-only LFX and `lfx[bundles]`](https://docs.langflow.org/lfx-compatibility#engine-only-lfx-and-lfxbundles)[Manage Privacy Choices](https://docs.langflow.org/lfx-compatibility#)

---

# Deploy Langflow with Nginx and SSL | Langflow Documentation

`https://docs.langflow.org/deployment-nginx-ssl`

# Deploy Langflow with Nginx and SSL

Replace DANA@EXAMPLE.COM with the email address that you want to associate with the SSH key.

Copy page ⌥C Version: 1.12.x On this page
## Prerequisites​
## Connect to your server with SSH​
## Install Langflow on your server​
## Install Nginx​
## Install Certbot and obtain SSL certificates​
## See also​







Deploy Langflow on a Linux-based server using Nginx as a reverse proxy, Let's Encrypt for SSL certificates, and Certbot for automated certificate management.


This setup encrypts all communications between users and your Langflow server. SSL certificates ensure that sensitive data is protected from eavesdropping and tampering, and the automatic certificate management through Certbot eliminates the complexity of manual SSL configuration.


## Prerequisites [​](https://docs.langflow.org/deployment-nginx-ssl#prerequisites)


- An Ubuntu or Debian-based Linux server with a dual-core CPU and at least 2 GB of RAM This example uses [Digital Ocean cloud](https://www.digitalocean.com) for hosting. Your deployment may vary.
- A domain name with external DNS management access
- A DNS record configured to point your domain to your server's external IP address For example, if your server's IP is `203.0.113.1`, configure your DNS like this: ```bash Type: A Name: langflow.example.com Value: 203.0.113.1 ```


## Connect to your server with SSH [​](https://docs.langflow.org/deployment-nginx-ssl#connect-to-your-server-with-ssh)


1. Create an SSH key to connect to your server remotely. For example: ```bash ssh-keygen -t ed25519 -C "DANA@EXAMPLE.COM" ``` Replace `DANA@EXAMPLE.COM` with the email address that you want to associate with the SSH key.
2. In your terminal, follow the instructions to create your SSH key pair. This creates both a private and public key. To copy the public key from your terminal, enter the following command: ```bash cat ~/Downloads/host-lf.pub | pbcopy ```
3. In your server, add the SSH key you copied in the previous step. For example, if you are using a Digital Ocean cloud server, add this SSH key when the server is created, or with the [Digital Ocean control panel](https://docs.digitalocean.com/products/droplets/how-to/add-ssh-keys/).
4. To connect to your server with SSH, enter the following command. ```bash ssh -i PATH_TO_PRIVATE_KEY/PRIVATE_KEY_NAME root@SERVER_IP_ADDRESS ``` Replace the following:
  - `PATH_TO_PRIVATE_KEY/PRIVATE_KEY_NAME`: The path to your private SSH key file that matches the public key you added to your server
  - `SERVER_IP_ADDRESS`: Your server's IP address5. When prompted for a key fingerprint, type `yes`. The terminal output indicates if the connection succeeds or fails. The following response was returned after connecting to a Digital Ocean cloud server. ```bash System information as of Wed Oct 8 21:40:43 UTC 2025 System load: 0.02 Processes: 103 Usage of /: 4.1% of 47.35GB Users logged in: 1 Memory usage: 10% IPv4 address for eth0: 165.227.176.236 Swap usage: 0% IPv4 address for eth0: 10.17.0.5 ```


## Install Langflow on your server [​](https://docs.langflow.org/deployment-nginx-ssl#install-langflow-on-your-server)


To install Langflow on your server, do the following:


1. Update system packages. ```bash sudo apt update && sudo apt upgrade -y ```
2. Install Python and pip. ```bash sudo apt install python3 python3-pip python3-venv -y ```
3. Install uv to manage Python packages. Langflow recommends uv for faster installation. ```bash pip install uv ```
4. Create a virtual environment for Langflow. ```bash uv venv langflow-venv source langflow-venv/bin/activate ```
5. Install Langflow using uv. ```bash uv pip install langflow ```
6. Optionally, start Langflow. ```bash uv run langflow run --host 127.0.0.1 --port 7860 & ``` Test access at your `http://YOUR_PUBLIC_IP:7860`. Since Langflow is running on `localhost`, you should not be successful. In next steps, you will install Nginx as a reverse proxy to handle external access, and Certbot to configure SSL for secure HTTPS access.


## Install Nginx [​](https://docs.langflow.org/deployment-nginx-ssl#install-nginx)


Nginx is a reverse proxy that receives external requests and forwards them to your Langflow server. In addition to SSL termination, Nginx includes features for load balancing and security. For more information, see the [Nginx documentation](https://nginx.org/en/docs/).


1. Install Nginx on your server. ```bash sudo apt install nginx -y ```
2. Start and enable Nginx on your server. ```bash sudo systemctl start nginx sudo systemctl enable nginx ```
3. Create an Nginx configuration file. Replace **DOMAIN_NAME** with your actual domain name, such as `langflow.example.com`. ```bash sudo nano /etc/nginx/sites-available/DOMAIN_NAME ```
4. Paste the following content to the configuration file you created at `/etc/nginx/sites-available/DOMAIN_NAME`. Replace **DOMAIN_NAME** with your actual domain name, such as `langflow.example.com`. ```nginx server { listen 80; server_name DOMAIN_NAME; # Increase client body size for file uploads client_max_body_size 100M; location / { proxy_pass http://127.0.0.1:7860/; proxy_set_header Host $host; proxy_set_header X-Real-IP $remote_addr; proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for; proxy_set_header X-Forwarded-Proto $scheme; # WebSocket support for Langflow proxy_http_version 1.1; proxy_set_header Upgrade $http_upgrade; proxy_set_header Connection "upgrade"; # Timeout settings for long-running flows proxy_connect_timeout 60s; proxy_send_timeout 60s; proxy_read_timeout 300s; # Buffer settings proxy_buffering off; proxy_request_buffering off; } } ``` This configuration listens on port 80 for standard HTTP. When you install Certbot in a later step, it will modify this configuration to add port 443 for HTTPS.
5. To enable your site configuration, create a symlink between the `/sites-available` and `/sites-enabled` directories. `/sites-available` stores all site configurations, and `/sites-enabled` stores only active configurations which Nginx reads from. Creating this symlink switches this configuration ON. ```bash sudo ln -s /etc/nginx/sites-available/DOMAIN_NAME /etc/nginx/sites-enabled/DOMAIN_NAME ```
6. Check the Nginx configuration file's syntax. ```bash sudo nginx -t ```
7. Restart Nginx. ```bash sudo systemctl restart nginx ```


## Install Certbot and obtain SSL certificates [​](https://docs.langflow.org/deployment-nginx-ssl#install-certbot-and-obtain-ssl-certificates)


While Nginx handles SSL termination in encrypting and decrypting traffic, Certbot automatically obtains SSL certificates from Let's Encrypt and configures Nginx to use them.


The Certbot client is [recommended by Let's Encrypt](https://letsencrypt.org/getting-started/#selecting-and-operating-an-acme-client-yourself) for automated certificate management. For more information, see the [Certbot documentation](https://certbot.eff.org/).


Install the Certbot client on your server to manage certificates, and install the [`python3-certbot-nginx` plugin](https://packages.ubuntu.com/source/jammy/python-certbot-nginx) to allow Certbot to modify your server's Nginx configuration.


1. Install Certbot and the `python3-certbot-nginx` plugin. ```bash sudo apt install certbot python3-certbot-nginx -y ```
2. Obtain the SSL certificate for `DOMAIN_NAME` from Let's Encrypt. ```bash sudo certbot --nginx -d DOMAIN_NAME ``` This result indicates that Certbot succeeded. ```bash Successfully received certificate. Certificate is saved at: /etc/letsencrypt/live/DOMAIN_NAME/fullchain.pem Key is saved at: /etc/letsencrypt/live/DOMAIN_NAME/privkey.pem ``` When using `--nginx`, Certbot automatically injects the paths into your Nginx configuration as `ssl_certificate` and `ssl_certificate_key`.
3. Start Langflow from the virtual environment. a. Activate the virtual environment. ```bash source langflow-venv/bin/activate ``` b. Start Langflow in the background. ```bash uv run langflow run --host 127.0.0.1 --port 7860 & ```
4. To test the deployment, navigate to `https://DOMAIN_NAME` in your browser.
5. Verify the SSL certificate is working. Ensure the URL is `https://`, not `http://`. Your browser's address bar should display a **Lock** icon. Click **Lock** to view your SSL certificate details.


## See also [​](https://docs.langflow.org/deployment-nginx-ssl#see-also)


- [Deploy Langflow on a remote server with Caddy](https://docs.langflow.org/deployment-caddyfile)
- [Deploy Langflow on Docker](https://docs.langflow.org/deployment-docker)


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)

- [Prerequisites](https://docs.langflow.org/deployment-nginx-ssl#prerequisites)
- [Connect to your server with SSH](https://docs.langflow.org/deployment-nginx-ssl#connect-to-your-server-with-ssh)
- [Install Langflow on your server](https://docs.langflow.org/deployment-nginx-ssl#install-langflow-on-your-server)
- [Install Nginx](https://docs.langflow.org/deployment-nginx-ssl#install-nginx)
- [Install Certbot and obtain SSL certificates](https://docs.langflow.org/deployment-nginx-ssl#install-certbot-and-obtain-ssl-certificates)
- [See also](https://docs.langflow.org/deployment-nginx-ssl#see-also)[Manage Privacy Choices](https://docs.langflow.org/deployment-nginx-ssl#)

---

# Deploy a public Langflow server | Langflow Documentation

`https://docs.langflow.org/deployment-public-server`

# Deploy a public Langflow server
## Prerequisites​
## Expose your Langflow server with ngrok​
## Use a public Langflow server​




By default, your Langflow server at http://localhost:7860 isn't exposed to the public internet. However, you can forward Langflow server traffic with a forwarding platform like ngrok or zrok to make your server public.

Copy page ⌥C Version: 1.12.x On this page

By default, your Langflow server at `http://localhost:7860` isn't exposed to the public internet. However, you can forward Langflow server traffic with a forwarding platform like [ngrok](https://ngrok.com/docs/getting-started/) or [zrok](https://docs.zrok.io/docs/getting-started) to make your server public.


When your Langflow server is public, you can do things like [deploy your Langflow MCP server externally](https://docs.langflow.org/deployment-public-server#deploy-your-mcp-server-externally), [serve API requests](https://docs.langflow.org/deployment-public-server#serve-api-requests), and [share a flow's **Playground** publicly](https://docs.langflow.org/deployment-public-server#share-a-flows-playground).


## Prerequisites [​](https://docs.langflow.org/deployment-public-server#prerequisites)


On the machine where you plan to host your Langflow installation, [install Langflow](https://docs.langflow.org/get-started-installation) and a reverse proxy or forwarding service.


This guide uses ngrok, but you can use any similar reverse proxy or forwarding platform.


If you want to follow along with this guide, [install ngrok](https://ngrok.com/docs/getting-started/#1-install-ngrok) and [create an ngrok authtoken](https://dashboard.ngrok.com/get-started/your-authtoken).


## Expose your Langflow server with ngrok [​](https://docs.langflow.org/deployment-public-server#expose-your-langflow-server-with-ngrok)


1. Start Langflow: ```bash uv run langflow run ```
2. In another terminal window, use your ngrok authtoken to authenticate your local ngrok server: ```bash ngrok config add-authtoken NGROK_AUTHTOKEN ```
3. Use ngrok to expose your Langflow server to the public internet: ```bash ngrok http http://localhost:7860 ``` This example assumes that you use the default Langflow listening address at `http://localhost:7860`. If you have a different listening address, you must modify this command accordingly. The ngrok session starts in your terminal and deploys an ephemeral domain with no authentication. To add authentication or deploy a static domain, see the [ngrok documentation](https://ngrok.com/docs/). The `Forwarding` line prints the forwarding address for your Langflow server: ```text Forwarding https://94b1-76-64-171-14.ngrok-free.app -> http://localhost:7860 ``` The forwarding address acts as a reverse proxy for your Langflow server, and ngrok forwards your local traffic to this domain.
4. To verify that your Langflow server is publicly available, navigate to the forwarding address URL, such as `https://94b1-76-64-171-14.ngrok-free.app`.


## Use a public Langflow server [​](https://docs.langflow.org/deployment-public-server#use-a-public-langflow-server)


When your Langflow server is public, you can do things like [deploy your Langflow MCP server externally](https://docs.langflow.org/deployment-public-server#deploy-your-mcp-server-externally), [serve API requests](https://docs.langflow.org/deployment-public-server#serve-api-requests), and [share a flow's **Playground** publicly](https://docs.langflow.org/deployment-public-server#share-a-flows-playground).


### Deploy your MCP server externally [​](https://docs.langflow.org/deployment-public-server#deploy-your-mcp-server-externally)


After you deploy a public Langflow server, you can also access your Langflow projects' MCP servers publicly.


To do this, use your server's forwarding address when you [connect a client to a Langflow MCP server](https://docs.langflow.org/mcp-server#connect-clients-to-use-the-servers-actions).


### Serve API requests [​](https://docs.langflow.org/deployment-public-server#serve-api-requests)


To send requests to a public Langflow server's [Langflow API](https://docs.langflow.org/api-reference-api-examples) endpoints, use the server's domain as the [base URL](https://docs.langflow.org/api-reference-api-examples#base-url) for your API requests. For example:


```bash
curl -X POST \
  "PUBLIC_SERVER_DOMAIN/api/v1/webhook/FLOW_ID" \
  -H "Content-Type: application/json" \
  -H "x-api-key: LANGFLOW_API_KEY" \
  -d '{"data": "example-data"}'
```


You also use your public domain when making Langflow API calls in scripts, including the code snippets that are automatically generated by Langflow. For example, the following code snippet calls an ngrok domain to trigger the specified flow (`d764c4b8...`):


```python
import requests

url = "https://3f7c-73-64-93-151.ngrok-free.app/api/v1/run/d764c4b8-5cec-4c0f-9de0-4b419b11901a"  # The complete API endpoint URL for this flow

# Request payload configuration
payload = {
    "output_type": "chat",
    "input_type": "chat",
    "input_value": "Hello"
}

# Request headers
headers = {
    "Content-Type": "application/json",
    "x-api-key": "LANGFLOW_API_KEY"
}

try:
    # Send API request
    response = requests.request("POST", url, json=payload, headers=headers)
    response.raise_for_status()  # Raise exception for bad status codes

    # Print response
    print(response.text)

except requests.exceptions.RequestException as e:
    print(f"Error making API request: {e}")
except ValueError as e:
    print(f"Error parsing response: {e}")
```


For a demo of the Langflow API in a script, see the [Quickstart](https://docs.langflow.org/get-started-quickstart).


### Share a flow's Playground [​](https://docs.langflow.org/deployment-public-server#share-a-flows-playground)


After you deploy a public Langflow server, you can use the **Shareable Playground** option to make a flow's **Playground** available at a public URL. If a user accesses this URL, they can interact with the flow's chat input and output and view the results without installing Langflow or generating a Langflow API key.


For more information, see [Share a flow's Playground](https://docs.langflow.org/concepts-playground#share-a-flows-playground).


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)

- [Prerequisites](https://docs.langflow.org/deployment-public-server#prerequisites)
- [Expose your Langflow server with ngrok](https://docs.langflow.org/deployment-public-server#expose-your-langflow-server-with-ngrok)
- [Use a public Langflow server](https://docs.langflow.org/deployment-public-server#use-a-public-langflow-server)
  - [Deploy your MCP server externally](https://docs.langflow.org/deployment-public-server#deploy-your-mcp-server-externally)
  - [Serve API requests](https://docs.langflow.org/deployment-public-server#serve-api-requests)
  - [Share a flow's Playground](https://docs.langflow.org/deployment-public-server#share-a-flows-playground)[Manage Privacy Choices](https://docs.langflow.org/deployment-public-server#)

---

# Deploy Langflow on a remote server | Langflow Documentation

`https://docs.langflow.org/deployment-caddyfile`

# Deploy Langflow on a remote server
## Prerequisites​
## Connect to your remote server with SSH​
## Deploy Langflow on your server​
## See also​





Learn how to deploy Langflow on your own remote server with secure web access. This guide walks you through setting up Langflow on a remote server using Docker and configuring secure web access with Caddy.

Copy page ⌥C Version: 1.12.x On this page

Learn how to deploy Langflow on your own remote server with secure web access. This guide walks you through setting up Langflow on a remote server using [Docker](https://docs.docker.com/) and configuring secure web access with [Caddy](https://caddyserver.com/docs/).


## Prerequisites [​](https://docs.langflow.org/deployment-caddyfile#prerequisites)


- A server with a dual-core CPU and at least 2 GB of RAM. This example uses [Hetzner cloud](https://www.hetzner.com/) for hosting. Your deployment may vary.


## Connect to your remote server with SSH [​](https://docs.langflow.org/deployment-caddyfile#connect-to-your-remote-server-with-ssh)


1. Create an SSH key to connect to your server remotely. For example: ```bash ssh-keygen -t ed25519 -C "DANA@EXAMPLE.COM" ``` Replace `DANA@EXAMPLE.COM` with the email address that you want to associate with the SSH key.
2. In your terminal, follow the instructions to create your SSH key pair. This creates both a private and public key. To copy the public key from your terminal, enter the following command: ```bash cat ~/Downloads/host-lf.pub | pbcopy ```
3. In your remote server, add the SSH key you copied in the previous step. For example, if you are using a Hetzner cloud server, click **Server**, and then select **SSH keys** to add an SSH key.
4. To connect to your server with SSH, enter the following command. ```bash ssh -i PATH_TO_PRIVATE_KEY/PRIVATE_KEY_NAME root@SERVER_IP_ADDRESS ``` Replace the following:
  - `PATH_TO_PRIVATE_KEY/PRIVATE_KEY_NAME`: The path to your private SSH key file that matches the public key you added to your server
  - `SERVER_IP_ADDRESS`: Your server's IP address5. When prompted for a key fingerprint, type `yes`.


The terminal output indicates if the connection succeeds or fails. The following response was returned after connecting to a Hetzner cloud server:


```text
System information as of Mon May 19 04:34:44 PM UTC 2025

System load:  0.0               Processes:             129
Usage of /:   1.5% of 74.79GB   Users logged in:       0
Memory usage: 5%                IPv4 address for eth0: 5.161.250.132
Swap usage:   0%                IPv6 address for eth0: 2a01:4ff:f0:4de7::1
```


## Deploy Langflow on your server [​](https://docs.langflow.org/deployment-caddyfile#deploy-langflow-on-your-server)


Now that your local machine is connected to your remote server with SSH, you can install Docker, create a `docker-compose.yml` file, and serve it publicly with a reverse proxy, such as Caddy.


1. Install Docker on your server. Since this example server is an Ubuntu server, it can install snap packages. If you aren't using Ubuntu or you prefer a different installation method, see the [official Docker installation guide](https://docs.docker.com/get-started/get-docker/) for instructions for your operating system. ```bash snap install docker ```
2. Create a file called `docker-compose.yml`, and then open it in a text editor: ```bash touch docker-compose.yml && nano docker-compose.yml ```
3. Add the following values to `docker-compose.yml`, and then save the file. The following example defines the Langflow service from the `langflow:latest` image and a Caddy service to expose Langflow through a reverse proxy. ```yaml version: "3.8" services: langflow: image: langflowai/langflow:latest ports: - "7860:7860" environment: - LANGFLOW_HOST=0.0.0.0 - LANGFLOW_PORT=7860 caddy: image: caddy:latest ports: - "80:80" - "443:443" volumes: - ./Caddyfile:/etc/caddy/Caddyfile - caddy_data:/data - caddy_config:/config depends_on: - langflow volumes: caddy_data: caddy_config: ```
4. Create a file called `Caddyfile`: ```bash touch Caddyfile && nano Caddyfile ```
5. Add the following values to `Caddyfile`, and then save the file. This Caddyfile configures Caddy to listen on port 80, and forward all incoming requests to port 80 to the Langflow service at port 7860. ```text :80 { reverse_proxy langflow:7860 } ```
6. To deploy your server, run `docker-compose up`. When the `Welcome to Langflow` message appears, Langflow is running and accessible internally at `http://0.0.0.0:7860` inside the Docker network.
7. To access your Langflow server over the public internet, navigate to your server's public IP address, such as `http://5.161.250.132`. This address uses HTTP because HTTPS isn't enabled yet.
8. Recommended: Enable HTTPS:
  1. Modify your domain's A record to point to your server's IP address. For example: ```text Type: A Name: langflow Value: 5.161.250.132 # Set to your server's IP address ```
  2. Stop your server.
  3. Modify your Caddyfile to include port `443` so Caddy can forward both HTTP (port 80) and HTTPS (port 443) requests to the Langflow service: ```text :80, :443 { reverse_proxy langflow:7860 } ```
  4. Start your server. When users visit your domain, Caddy recognizes the incoming traffic and automatically routes it to your server with a secure, encrypted connection.9. To exit your SSH session, type `exit`.


## See also [​](https://docs.langflow.org/deployment-caddyfile#see-also)


To package your local flows into a custom Docker image, see [Containerize a Langflow application](https://docs.langflow.org/develop-application).


For a step-by-step guide to deploying Langflow, including deployments to [fly.io](https://fly.io/) and [Flightcontrol.dev](https://www.flightcontrol.dev/), see [How to Host Langflow Anywhere](https://www.youtube.com/watch?v=q4qt5hSnte4).


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)

- [Prerequisites](https://docs.langflow.org/deployment-caddyfile#prerequisites)
- [Connect to your remote server with SSH](https://docs.langflow.org/deployment-caddyfile#connect-to-your-remote-server-with-ssh)
- [Deploy Langflow on your server](https://docs.langflow.org/deployment-caddyfile#deploy-langflow-on-your-server)
- [See also](https://docs.langflow.org/deployment-caddyfile#see-also)[Manage Privacy Choices](https://docs.langflow.org/deployment-caddyfile#)

---

# Deploy Langflow on Google Cloud Platform | Langflow Documentation

`https://docs.langflow.org/deployment-gcp`

# Deploy Langflow on Google Cloud Platform

This guide demonstrates how to deploy Langflow on Google Cloud Platform with a Cloud Shell script that walks through the process of setting up a Debian-based VM with the Langflow package, Nginx, and the necessary configurations to run the Langflow development environment in GCP.

Copy page ⌥C Version: 1.12.x

This guide demonstrates how to deploy Langflow on [Google Cloud Platform](https://console.cloud.google.com/) with a Cloud Shell script that walks through the process of setting up a Debian-based VM with the Langflow package, Nginx, and the necessary configurations to run the Langflow development environment in GCP.


To use this script, you need a Google Cloud project with the necessary permissions to create resources.


1. Follow this link to launch the Cloud Shell with the GCP deployment script from the Langflow repository: [![Deploy to Google Cloud](https://gstatic.com/cloudssh/images/open-btn.svg)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/langflow-ai/langflow&working_dir=scripts/gcp&shellonly=true&tutorial=walkthroughtutorial.md)
2. Click **Trust repo**. Some `gcloud` commands may not run in an ephemeral Cloud Shell environment.
3. Click **Start**, and then follow the tutorial to deploy Langflow.


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)[Manage Privacy Choices](https://docs.langflow.org/deployment-gcp#)

---

# Best practices for Langflow on Kubernetes | Langflow Documentation

`https://docs.langflow.org/deployment-prod-best-practices`

# Best practices for Langflow on Kubernetes

IDE (development): Deploy both the Langflow visual editor (frontend) and API (backend). Typically, this is used for development environments where developers use the visual editor to create and manage flows before packaging and serving them through a production runtime deployment.

Copy page ⌥C Version: 1.12.x On this page
## Resources and scaling​
## Failure points​
## Monitoring​
## Security​
## Production preflight checks​
*To enable preflight checks, set the following in your .env file:*

## See also​







This guide provides best practices for deploying Langflow in production environments on Kubernetes.


## Resources and scaling [​](https://docs.langflow.org/deployment-prod-best-practices#resources-and-scaling)


Langflow's minimum resource requirements vary by deployment type:


- **IDE (development)**: Deploy both the Langflow visual editor (frontend) and API (backend). Typically, this is used for development environments where developers use the visual editor to create and manage flows before packaging and serving them through a production runtime deployment. The frontend service requires a minimum of 512Mi RAM and 0.3 CPU per instance with 1 replica. The backend service requires a minimum of 1Gi RAM and 0.5 CPU per instance with 1 replica.
- **Runtime (production)**: Deploy the Langflow runtime for production flows, which is headless (backend only) service focused on serving the Langflow API. This is used for production environments where flows are executed programmatically without the need for the visual editor. Minimum requirements include 2Gi RAM and 1000m (1 CPU) per instance with 3 replicas.


For more information about Langflow deployment types, see [Langflow architecture on Kubernetes](https://docs.langflow.org/deployment-architecture).


### Estimate, test, and adjust [​](https://docs.langflow.org/deployment-prod-best-practices#estimate-test-and-adjust)


Start with the minimum recommended resources and replicas, then monitor and scale as needed based on your deployment's requirements and performance testing. Consider the following factors in your resource estimation and performance testing:


- Flow complexity.
- Volume of concurrent users and requests. For IDE (development) deployments, consider that frontend activity also pings the backend service, so you typically need to scale both the frontend and backend together.
- Request payload content and size, particularly for file uploads in production deployments.
- Storage requirements for cache, file management, and the Langflow database. An [external PostgreSQL database](https://docs.langflow.org/deployment-prod-best-practices#use-an-external-postgresql-database) is recommended for production deployments.
- Infrastructure options that might require more resources, such as multi-core CPUs.


### Use an external PostgreSQL database [​](https://docs.langflow.org/deployment-prod-best-practices#use-an-external-postgresql-database)


An external PostgreSQL database is recommended for production deployments to improve scalability and reliability as compared to the default SQLite database.


Your resource allocation and replication strategy must be able to support the PostgreSQL service and storage. For example, for a runtime (production) deployment, you might allocate 4Gi RAM, 2 CPU, and multiple replicas for high availability. Tune PostgreSQL parameters, such as `work_mem` and `shared_buffers`, as needed based on resource requirements and usage metrics.


Recommended configurations include:


- Persistent storage to prevent data loss on container shutdown
- High Availability (HA) or Active-Active for automatic failover, scaling, and load balancing
- Shared databases for multi-instance deployments
- Shared storage, such as NFS or cloud storage, for multi-instance deployments to access large files stored on disk, such as in `/opt/langflow/data/`.


For more information, see [Configure an external PostgreSQL database](https://docs.langflow.org/configuration-custom-database) and [Langflow database guide for enterprise DBAs](https://docs.langflow.org/enterprise-database-guide).


### Use HPA for dynamic scaling [​](https://docs.langflow.org/deployment-prod-best-practices#use-hpa-for-dynamic-scaling)


Load balancing and dynamic scaling are recommended for runtime (production) deployments.


For example, consider using Horizontal Pod Autoscaler (HPA) in Kubernetes to dynamically scale based on CPU or memory usage. The following example shows a Langflow HPA configuration with CPU-based scaling:


```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: langflow-runtime-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: langflow-runtime
  minReplicas: 1
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 80
```


## Failure points [​](https://docs.langflow.org/deployment-prod-best-practices#failure-points)


Langflow's reliability in production depends on mitigating key failure points, particularly around the database, file system, and instance availability:


- **Database failures**: See [Langflow database guide for enterprise DBAs](https://docs.langflow.org/enterprise-database-guide).
- **File system failures**: Concurrency issues in file caching, such as `/app/data/.cache`, can cause IO errors in multi-instance setups. To avoid this, use a shared, POSIX-compliant file system or cloud storage. Use persistent volumes instead of ramdisk solutions that result in data loss on container shutdown.
- **Instance failures**: Deploy multiple replicas to avoid service disruptions when a single instance fails. Use health checks to detect and replace failed pods.
- **Network and dependency failures**: External APIs or services used in flows may fail, causing flow errors. Implement retry logic and error handling in flows or application code. Monitor network latency and dependency health.


## Monitoring [​](https://docs.langflow.org/deployment-prod-best-practices#monitoring)


Effective monitoring ensures Langflow operates reliably and performs well under varying loads:


- **Database monitoring**: See [Langflow database guide for enterprise DBAs](https://docs.langflow.org/enterprise-database-guide).
- **Application logs**: Collect and analyze logs for errors, warnings, and flow execution issues. Centralize logs using tools like ELK Stack or Fluentd. You can also inspect [Langflow logs](https://docs.langflow.org/logging).
- **Resource usage**: Track CPU, memory, and disk usage of Langflow instances. Use Prometheus and Grafana for real-time metrics collection and monitoring in Kubernetes. To expose your Langflow server's Prometheus metrics, set `LANGFLOW_PROMETHEUS_ENABLED=True` (the default is `false`). The default port for the Prometheus metrics is 9090. To change the port, set `LANGFLOW_PROMETHEUS_PORT`.
- **API performance**: Monitor response times, error rates, and request throughput. Set alerts for high latency or error spikes.
- **Observability tools**: Integrate with [LangWatch](https://docs.langflow.org/integrations-langwatch) or [Opik](https://docs.langflow.org/integrations-opik) for detailed flow tracing and metrics. Use these tools to debug flow performance and optimize execution.


## Security [​](https://docs.langflow.org/deployment-prod-best-practices#security)


Running Langflow in production requires robust security measures to protect the application, data, and users. Follow industry best practices and use secure Langflow configurations, such as the following:


- **Container security**: Apply security best practices for containerized applications. For example, set `readOnlyRootFilesystem: true` in runtime (production) containers to prevent unauthorized modifications. Restrict access to files and codebases containing sensitive data and configuration files that shouldn't be exposed to unauthorized users.
- **Secrets management**: Store sensitive data like API keys and PostgreSQL credentials in Kubernetes secrets or external secrets managers like HashiCorp Vault.
- **Authentication, authorization, and access control**: Start your Langflow server with authentication enabled, as explained in [API keys and authentication](https://docs.langflow.org/api-keys-and-authentication). Restrict network and resource access with firewalls, network policies, network security groups, or VPCs. For example, restrict PostgreSQL database access to Langflow instances.
- **Encryption and privacy**: Follow industry best practices and legal requirements for data privacy and encryption of data in transit and at rest, including GDPR requirements, HTTPS, TLS, and SSL. For example, configure PostgreSQL with valid SSL certificates and append `?sslmode=require` or `?sslmode=verify-full` to the connection string to enable SSL for database connections.
- **Security posture maintenance**: Conduct regular security audits, keep current with software updates, and monitor for suspicious activity using intrusion detection systems.


## Production preflight checks [​](https://docs.langflow.org/deployment-prod-best-practices#production-preflight)


To verify production infrastructure before any workers start, set the `LANGFLOW_DEPLOYMENT_PROFILE` environment variable to `prod`.


By default, `LANGFLOW_DEPLOYMENT_PROFILE` is set to `dev` and skips these checks. When set to `prod`, Langflow runs every check once and prints the full result. A `fail` aborts boot with a non-zero exit, so a misconfigured server never starts up. A `warn` does not abort and allows startup.


Preflight checks run for any Langflow process started with the `prod` profile enabled, not only Kubernetes.


To enable preflight checks, set the following in your `.env` file:


```text
LANGFLOW_DEPLOYMENT_PROFILE=prod
```


Alternatively, pass the CLI option, which overrides the environment variable:


```bash
uv run langflow run --deployment-profile prod
```


### Required checks [​](https://docs.langflow.org/deployment-prod-best-practices#required-checks)


These checks abort boot when they fail:


| Check | What must be true |
| --- | --- |
| Database | `LANGFLOW_​DATABASE_​URL` is a reachable **PostgreSQL** database. SQLite fails this check. |
| File storage | `LANGFLOW_​STORAGE_​TYPE` is an external object store such as `s3`, not local disk. |
| Encryption secret | `LANGFLOW_​SECRET_​KEY` is set in the environment to a usable Fernet key. An auto-generated key or a node-local `config_​dir/secret_​key` file is not enough. See [`LANGFLOW_​SECRET_​KEY`](https://docs.langflow.org/api-keys-and-authentication#langflow-secret-key). |
| pgVector | `PGVECTOR_​CONNECTION_​STRING` is set, the database is reachable, and the Postgres `vector` extension is installed (`CREATE EXTENSION vector;`). Production Langflow requires pgVector even if you are not creating knowledge bases yet. |


### Degraded checks [​](https://docs.langflow.org/deployment-prod-best-practices#degraded-checks)


These checks report reduced capability. Telemetry and MCP only `warn`. Cache and the shared job queue abort boot if you selected an external backend that is unreachable.


| Check | `ok` | `warn` | `fail` (aborts) |
| --- | --- | --- | --- |
| Cache | `LANGFLOW_​CACHE_​TYPE=redis` and Redis is reachable | In-memory default (`async` or `memory`). Caches are not shared across replicas. | Redis selected but unreachable. Unset `LANGFLOW_​CACHE_​TYPE` to boot with the in-memory fallback. |
| Shared queue | `LANGFLOW_​JOB_​QUEUE_​TYPE=redis` and Redis is reachable | In-process default (`asyncio`). Jobs stay on a single pod. | Redis selected but unreachable. Unset `LANGFLOW_​JOB_​QUEUE_​TYPE` to boot with the in-process fallback. |
| Telemetry | Product telemetry is enabled | `LANGFLOW_​DO_​NOT_​TRACK` is set | Never fails |
| MCP serving posture | MCP is disabled, or the serving knobs below match the multi-tenant values | One or more knobs are still at a single-tenant default | Never fails |


If this plane does not serve MCP, set `LANGFLOW_MCP_SERVER_ENABLED=false`. Otherwise, production preflight expects these values when MCP is enabled:


| Variable | Expected in `prod` | Default |
| --- | --- | --- |
| `LANGFLOW_​SKIP_​MCP_​AUTO_​INIT` | `true` | `false` |
| `LANGFLOW_​ADD_​PROJECTS_​TO_​MCP_​SERVERS` | `false` | `true` |
| `LANGFLOW_​MCP_​COMPOSER_​ENABLED` | `false` | `true` |
| `LANGFLOW_​MCP_​SERVERS_​LOCKED` | `true` | `false` |
| `LANGFLOW_​MCP_​SSE_​ENABLED` | `false` | `true` |
| `LANGFLOW_​MCP_​SERVER_​INTERPRETER_​HARDENING` | `true` | `false` |
| `LANGFLOW_​MCP_​SERVER_​DOCKER_​HARDENING` | `true` | `false` |
| `LANGFLOW_​SSRF_​PROTECTION_​ENABLED` | `true` | `true` |
| `LANGFLOW_​CONNECTOR_​SSRF_​VALIDATION_​ENABLED` | `true` | `true` |
| `LANGFLOW_​CONNECTOR_​SSRF_​ALLOW_​LOOPBACK` | `false` | `true` |
| `LANGFLOW_​DISABLE_​TRACK_​APIKEY_​USAGE` | `true` | `false` |
| `LANGFLOW_​MCP_​SERVER_​ALLOWED_​PACKAGES` | Set to an allowlist (empty string blocks all package runners) | Unset |
| `LANGFLOW_​MCP_​SERVER_​ENV_​ALLOWLIST` | Set to an allowlist (empty string blocks all tenant-supplied environment variables) | Unset |


### Local Chroma in `prod` [​](https://docs.langflow.org/deployment-prod-best-practices#local-chroma-in-prod)


The `prod` profile blocks new knowledge bases and memory bases that use local Chroma. For local storage, use a shared pgVector, OpenSearch, or Chroma Cloud store, or run Langflow with `LANGFLOW_DEPLOYMENT_PROFILE=dev`


## See also [​](https://docs.langflow.org/deployment-prod-best-practices#see-also)


- [Deploy the Langflow production environment on Kubernetes](https://docs.langflow.org/deployment-kubernetes-prod)
- [Langflow Helm Charts repository](https://github.com/langflow-ai/langflow-helm-charts)
- [Langflow environment variables](https://docs.langflow.org/environment-variables)


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)

- [Resources and scaling](https://docs.langflow.org/deployment-prod-best-practices#resources-and-scaling)
  - [Estimate, test, and adjust](https://docs.langflow.org/deployment-prod-best-practices#estimate-test-and-adjust)
  - [Use an external PostgreSQL database](https://docs.langflow.org/deployment-prod-best-practices#use-an-external-postgresql-database)
  - [Use HPA for dynamic scaling](https://docs.langflow.org/deployment-prod-best-practices#use-hpa-for-dynamic-scaling)- [Failure points](https://docs.langflow.org/deployment-prod-best-practices#failure-points)
- [Monitoring](https://docs.langflow.org/deployment-prod-best-practices#monitoring)
- [Security](https://docs.langflow.org/deployment-prod-best-practices#security)
- [Production preflight checks](https://docs.langflow.org/deployment-prod-best-practices#production-preflight)
  - [Required checks](https://docs.langflow.org/deployment-prod-best-practices#required-checks)
  - [Degraded checks](https://docs.langflow.org/deployment-prod-best-practices#degraded-checks)
  - [Local Chroma in `prod`](https://docs.langflow.org/deployment-prod-best-practices#local-chroma-in-prod)- [See also](https://docs.langflow.org/deployment-prod-best-practices#see-also)[Manage Privacy Choices](https://docs.langflow.org/deployment-prod-best-practices#)

---

# Deploy Langflow on Hugging Face Spaces | Langflow Documentation

`https://docs.langflow.org/deployment-hugging-face-spaces`

# Deploy Langflow on Hugging Face Spaces

This guide explains how to deploy Langflow on Hugging Face Spaces.

Copy page ⌥C Version: 1.12.x

This guide explains how to deploy Langflow on [Hugging Face Spaces](https://huggingface.co/spaces/).


1. Go to the [Langflow Space](https://huggingface.co/spaces/Langflow/Langflow?duplicate=true).
2. Click **Duplicate Space**.
3. Configure the duplicated Space: ![Hugging Face deployment dialog](https://docs.langflow.org/assets/images/hugging-face-deployment-fa1554738ef6c3249ba3fec70b2134cb.png)
  1. Enter a name for your Space.
  2. Select either public or private visibility.
  3. Click **Duplicate Space**.


When setup is complete, you're redirected to your new Space automatically, and your Langflow instance is ready to use.


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)[Manage Privacy Choices](https://docs.langflow.org/deployment-hugging-face-spaces#)

---

# Langflow CLI | Langflow Documentation

`https://docs.langflow.org/configuration-cli`

Copy page ⌥C Version: 1.12.x On this page
## How to use the CLI​
## Precedence​
## Langflow CLI options​
*The following examples compare Boolean option forms for REMOVE_API_KEYS.*

## CLI commands​





The Langflow command line interface is the main interface for managing and running the Langflow server.


The Langflow CLI is automatically installed when you [install the Langflow package](https://docs.langflow.org/get-started-installation). It isn't available for Langflow Desktop.


## How to use the CLI [​](https://docs.langflow.org/configuration-cli#how-to-use-the-cli)


The Langflow CLI can be invoked in several ways, depending on your installation method and environment.


The recommended approach is to run the CLI with `uv run` from within a virtual environment where Langflow is installed.


For example, to start Langflow on the default port, run the following command:


```bash
uv run langflow run
```


If Langflow is installed globally or added to your PATH, you can execute the CLI directly with `langflow`.


```bash
langflow run
```


## Precedence [​](https://docs.langflow.org/configuration-cli#precedence)


Langflow CLI options override the values of [environment variables](https://docs.langflow.org/environment-variables) set in your terminal or primary `.env` file.


For example, if you have `LANGFLOW_PORT=7860` defined as an environment variable, and you run the CLI with `--port 7880`, then Langflow sets the port to `7880` because the CLI option overrides the environment variable.


This also applies to Boolean environment variables. For example, if you set `LANGFLOW_REMOVE_API_KEYS=True` in your `.env` file, you can change it to `False` at runtime by running the CLI with `--no-remove-api-keys`.


## Langflow CLI options [​](https://docs.langflow.org/configuration-cli#langflow-cli-options)


All Langflow CLI commands support options that modify the command's behavior or set environment variables.


To set values for options, you can use either of the following syntax styles:


- `--option value`
- `--option=value`


Values with spaces must be surrounded by quotation marks:


- `--option 'Value with Spaces'`
- `--option="Value with Spaces"`


### Boolean options [​](https://docs.langflow.org/configuration-cli#boolean-options)


Boolean options enable and disable settings. They have a true (enabled) and false (disabled) form:


- Enabled (true): `--option`
- Disabled (false): `--no-option`


The following examples compare Boolean option forms for `REMOVE_API_KEYS`.


- True
- False


`--remove-api-keys` is equivalent to setting `LANGFLOW_REMOVE_API_KEYS=True` in `.env`:


```bash
uv run langflow run --remove-api-keys
```


`--no-remove-api-keys` is equivalent to `LANGFLOW_REMOVE_API_KEYS=False` in `.env`:


```bash
uv run langflow run --no-remove-api-keys
```


In the following command references, default values for Booleans include both the CLI flag and the equivalent Boolean evaluation, such as "`--option` (true)" and "`--no-option` (false)".


### Universal options [​](https://docs.langflow.org/configuration-cli#universal-options)


The following options are available for all Langflow CLI commands:


- `--version`, `-v`: Show the version and exit.
- `--install-completion`: Install auto-completion for the current shell.
- `--show-completion`: Show the location of the auto-completion config file, if installed.
- `--help`: Print information about command usage, options, and arguments.


## CLI commands [​](https://docs.langflow.org/configuration-cli#cli-commands)


The following sections describe the available CLI commands and any additional options (beyond the [universal options](https://docs.langflow.org/configuration-cli#universal-options)) available for each command.


### langflow [​](https://docs.langflow.org/configuration-cli#langflow)


Running the CLI without any arguments prints a list of available options and commands.


- uv (recommended)
- Direct


```bash
uv run langflow
```


```bash
langflow
```


### langflow api-key [​](https://docs.langflow.org/configuration-cli#langflow-api-key)


Creates a Langflow API key.


You must be a superuser to create API keys with the CLI. For more information, see [Langflow API keys](https://docs.langflow.org/api-keys-and-authentication#langflow-api-keys).


- uv (recommended)
- Direct


```bash
uv run langflow api-key
```


```bash
langflow api-key
```


#### Options [​](https://docs.langflow.org/configuration-cli#options)


| Option | Default | Type | Description |
| --- | --- | --- | --- |
| `--log-level` | `error` | String | The logging level. One of `debug`, `info`, `warning`, `error`, or `critical`. |


### langflow copy-db [​](https://docs.langflow.org/configuration-cli#langflow-copy-db)


Copies the Langflow database files from the cache directory to the current Langflow installation directory, which is the directory containing `__main__.py`. You can find the copy target directory by running `which langflow`.


The following files are copied if they exist in the cache directory:


- `langflow.db`: The main Langflow database, stored in the user cache directory
- `langflow-pre.db`: The pre-release database, if it exists


- uv (recommended)
- Direct


```bash
uv run langflow copy-db
```


```bash
langflow copy-db
```


### langflow migration [​](https://docs.langflow.org/configuration-cli#langflow-migration)


Manages Langflow database schema changes using [Alembic](https://alembic.sqlalchemy.org/en/latest/), a database migration tool for SQLAlchemy.


The `migration` command has two modes:


- **Test mode (default)**: Checks if migrations can be applied safely without actually running the migrations. Use this mode to previews the changes that would be made to the database schema before proceeding with the migrations.
- **Fix mode**: Applies the migrations to update the database schema.


- uv (recommended)
- Global


1. Run test mode:


```bash
uv run langflow migration
```


1. Preview the changes returned by the test to determine if it's safe to proceed with the migration.
2. Run fix mode to apply the changes:


```bash
uv run langflow migration --fix
```


1. Run test mode:


```bash
langflow migration
```


1. Preview the changes returned by the test to determine if it's safe to proceed with the migration.
2. Run fix mode to apply the changes:


```bash
langflow migration --fix
```


### langflow observability doctor [​](https://docs.langflow.org/configuration-cli#langflow-observability-doctor)


Sends a probe span, metric, and log to the configured OTLP endpoint and reports what the backend accepted.


This command is also available as `lfx observability doctor`. It requires the `OTEL_EXPORTER_OTLP_ENDPOINT` environment variable to be set.


- uv (recommended)
- Direct


```bash
uv run langflow observability doctor
```


```bash
langflow observability doctor
```


#### Options [​](https://docs.langflow.org/configuration-cli#options-1)


| Option | Default | Type | Description |
| --- | --- | --- | --- |
| `--timeout` | `OTEL_​EXPORTER_​OTLP_​TIMEOUT` or the OpenTelemetry SDK default | Float | Per-export timeout in seconds. Must be greater than 0. |


The doctor also prints whether log message bodies (`LANGFLOW_OTEL_LOG_BODIES`) and database spans (`LANGFLOW_OTEL_DB_SPANS`) are enabled. In your backend, search for items named `lfx.observability.doctor`.


For more information, see [OpenTelemetry](https://docs.langflow.org/observability-opentelemetry#verify-your-configuration).


### langflow run [​](https://docs.langflow.org/configuration-cli#langflow-run)


Starts the Langflow server.


- uv (recommended)
- Direct


```bash
uv run langflow run [OPTIONS]
```


```bash
langflow run [OPTIONS]
```


#### Options [​](https://docs.langflow.org/configuration-cli#options-2)


This command supports some common and non-sensitive configuration options for your Langflow server. Other options must be set in the `.env` or your terminal. For more information Langflow configuration options, see [Langflow environment variables](https://docs.langflow.org/environment-variables).


| Option | Default | Type | Description |
| --- | --- | --- | --- |
| `--auto-saving` | `--auto-saving` (true) | Boolean | Whether to enable flow auto-saving in the visual editor. Use `--no-auto-saving` to disable flow auto-saving. |
| `--auto-saving-interval` | `1000` | Integer | The interval for flow auto-saving in milliseconds. |
| `--backend-only` | `--no-backend-only` (false) | Boolean | Whether to run Langflow's backend service only (no frontend). Omit or use `--no-backend-only` to start both the frontend and backend. See [Start Langflow in headless mode](https://docs.langflow.org/configuration-cli#start-langflow-in-headless-mode). |
| `--cache` | `async` | String | The type of [cache storage](https://docs.langflow.org/memory) to use. One of `async`, `redis`, `memory`, or `disk`. |
| `--components-path` | Not set | String | The path to the directory containing your custom components. |
| `--dev` | `--no-dev` (false) | Boolean | Whether to run in development mode (may contain bugs). |
| `--deployment-profile` | `dev` | String | Deployment profile: `dev` or `prod`. `prod` runs [production preflight](https://docs.langflow.org/deployment-prod-best-practices#production-preflight) before the server starts and aborts boot if a required service is missing. |
| `--env-file` | Not set | String | The path to the `.env` file containing Langflow environment variables. See [Start Langflow with a specific .env file](https://docs.langflow.org/configuration-cli#start-langflow-with-a-specific-env-file). |
| `--frontend-path` | Not set | String | The path to the frontend directory containing build files. This is only used when [contributing to the Langflow codebase](https://docs.langflow.org/contributing-how-to-contribute) or developing a custom Langflow image that includes customized frontend code. |
| `--health-check-max-retries` | `5` | Integer | The maximum number of retries for your Langflow server's health check. |
| `--host` | `localhost` | String | The host on which the Langflow server will run. |
| `--log-file` | `logs/langflow.log` | String | The path to the log file for Langflow. |
| `--log-level` | `critical` | String | The logging level as one of `debug`, `info`, `warning`, `error`, or `critical`. |
| `--log-rotation` | Not set | String | The log rotation interval, either a time duration or file size. |
| `--max-file-size-upload` | `1024` | Integer | The maximum size in megabytes for file uploads. |
| `--open-browser` | `--no-open-browser` (false) | Boolean | Whether to open the system web browser on startup. Use `--open-browser` to open the system's default web browser when Langflow starts. |
| `--port` | `7860` | Integer | The port on which the Langflow server will run. The server automatically selects a free port if the specified port is in use. |
| `--remove-api-keys` | `--no-remove-api-keys` (false) | Boolean | Whether to remove API keys and tokens from flows saved in the Langflow database. |
| `--ssl-cert-file-path` | Not set | String | The path to the SSL certificate file on the local system for SSL-encrypted connections. |
| `--ssl-key-file-path` | Not set | String | The path to the SSL key file on the local system for SSL-encrypted connections. |
| `--worker-timeout` | `300` | Integer | The Langflow server worker timeout in seconds. |
| `--workers` | `1` | Integer | The number of Langflow server worker processes. |


#### Start Langflow with a specific .env file [​](https://docs.langflow.org/configuration-cli#start-langflow-with-a-specific-env-file)


The `--env-file` option starts Langflow using the configuration defined in the given `.env` file. Additional options appended to this command override the values in the `.env` file if there are duplicates.


If `--env-file` is omitted or doesn't include all required variables, Langflow uses the default values for those variables.


- uv (recommended)
- Direct


```bash
uv run langflow run --env-file PATH/TO/LANGFLOW/.env
```


```bash
langflow run --env-file PATH/TO/LANGFLOW/.env
```


#### Start Langflow in headless mode [​](https://docs.langflow.org/configuration-cli#start-langflow-in-headless-mode)


The `--backend-only` option starts Langflow's backend service only. This headless mode has no frontend (visual editor), and you can only access the server programmatically with the Langflow API and CLI.


- uv (recommended)
- Direct


```bash
uv run langflow run --backend-only
```


```bash
langflow run --backend-only
```


### langflow superuser [​](https://docs.langflow.org/configuration-cli#langflow-superuser)


Creates a superuser account with the given username and password.


- uv (recommended)
- Direct


```bash
uv run langflow superuser --username [NAME] --password [PASSWORD] [OPTIONS]
```


```bash
langflow superuser --username [NAME] --password [PASSWORD] [OPTIONS]
```


#### Options [​](https://docs.langflow.org/configuration-cli#options-3)


| Option | Default | Type | Description |
| --- | --- | --- | --- |
| `--log-level` | `error` | String | The logging level. One of `debug`, `info`, `warning`, `error`, or `critical`. |


For this command, `--username` and `--password` aren't optional, and they have no default value. The command fails if you don't provide these arguments. For more information, see [`LANGFLOW_SUPERUSER` and `LANGFLOW_SUPERUSER_PASSWORD`](https://docs.langflow.org/api-keys-and-authentication#langflow-superuser).


#### Disable CLI superuser creation [​](https://docs.langflow.org/configuration-cli#disable-cli-superuser-creation)


The `langflow superuser` command is controlled by the [`LANGFLOW_ENABLE_SUPERUSER_CLI`](https://docs.langflow.org/api-keys-and-authentication#langflow-enable-superuser-cli) environment variable:


- **`LANGFLOW_ENABLE_SUPERUSER_CLI=True` (default)**: The `langflow superuser` command is available, and superuser creation is unrestricted.
- **`LANGFLOW_ENABLE_SUPERUSER_CLI=False` (recommended)**: Disables the `langflow superuser` command. For security reasons, this is recommended to prevent unauthorized superuser creation, especially in production environments.


To disable the `langflow superuser` command, you must set `LANGFLOW_ENABLE_SUPERUSER_CLI=False` in your Langflow `.env` file, and then [start Langflow with your `.env` file](https://docs.langflow.org/configuration-cli#start-langflow-with-a-specific-env-file).


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)

- [How to use the CLI](https://docs.langflow.org/configuration-cli#how-to-use-the-cli)
- [Precedence](https://docs.langflow.org/configuration-cli#precedence)
- [Langflow CLI options](https://docs.langflow.org/configuration-cli#langflow-cli-options)
  - [Boolean options](https://docs.langflow.org/configuration-cli#boolean-options)
  - [Universal options](https://docs.langflow.org/configuration-cli#universal-options)- [CLI commands](https://docs.langflow.org/configuration-cli#cli-commands)
  - [langflow](https://docs.langflow.org/configuration-cli#langflow)
  - [langflow api-key](https://docs.langflow.org/configuration-cli#langflow-api-key)
  - [langflow copy-db](https://docs.langflow.org/configuration-cli#langflow-copy-db)
  - [langflow migration](https://docs.langflow.org/configuration-cli#langflow-migration)
  - [langflow observability doctor](https://docs.langflow.org/configuration-cli#langflow-observability-doctor)
  - [langflow run](https://docs.langflow.org/configuration-cli#langflow-run)
  - [langflow superuser](https://docs.langflow.org/configuration-cli#langflow-superuser)[Manage Privacy Choices](https://docs.langflow.org/configuration-cli#)

---

# Contribute templates | Langflow Documentation

`https://docs.langflow.org/contributing-templates`

# Contribute templates

For template formatting examples, see /starter_projects in the Langflow repository.

Copy page ⌥C Version: 1.12.x On this page
## Create a PR to submit your template​
## Required items for template submission​



Follow these best practices when submitting a template to Langflow.


For template formatting examples, see [`/starter_projects`](https://github.com/langflow-ai/langflow/tree/main/src/backend/base/langflow/initial_setup/starter_projects) in the Langflow repository.


## Create a PR to submit your template [​](https://docs.langflow.org/contributing-templates#create-a-pr-to-submit-your-template)


Follow these steps to submit your template:


1. Fork the [Langflow repository](https://github.com/langflow-ai/langflow) on GitHub.
2. On your fork, add your `template.json` file to `/starter_projects`.
3. Include the [required items for template submission](https://docs.langflow.org/contributing-templates#required-items-for-template-submission).
4. Create a Pull Request (PR) from your fork to the main Langflow repository.
5. Include a screenshot of your template in the PR.


The Langflow team will review your PR, offer feedback, and, if approved, merge the template.


## Required items for template submission [​](https://docs.langflow.org/contributing-templates#required-items-for-template-submission)


Include the following items and follow these guidelines when submitting your template.


### Name [​](https://docs.langflow.org/contributing-templates#name)


The template name must be concise and contain no more than three words. Capitalize only the first letter of each word. For example: **Blog Writer** or **Travel Planning Agent**.


### Description [​](https://docs.langflow.org/contributing-templates#description)


A brief, informative description that is shown in the visual editor to help users understand the template's purpose and use cases. For example:


```json
   "description": "Auto-generate a customized blog post from instructions and referenced articles.",
```


### Icons [​](https://docs.langflow.org/contributing-templates#icons)


Use icons from the [Lucide](https://lucide.dev/icons/) icon library.


### Flow [​](https://docs.langflow.org/contributing-templates#flow)


Use only **Core components** and **Bundles**. Don't use custom components that aren't part of the Langflow codebase.


Include brief README, quickstart, or other essential details in a **Note**. Notes accept Markdown syntax. For example:


```text
# Financial Assistant Agents

The Financial Assistant Agent retrieves web content and writes reports about finance.

## Prerequisites

* [OpenAI API key](https://platform.openai.com/api-keys)
* [Tavily AI Search key](https://docs.tavily.com/welcome)
* [Sambanova API key](https://sambanova.ai/)

## Quickstart

1. In both **Agent** components, add your OpenAI API key.
2. In the **Model Provider** field, select **Sambanova**, and select a model.
3. In the **Sambanova** component, add your **Sambanova API key**.
4. In the **Tavily Search** component, add your **Tavily API key**.
5. Click the **Playground** and ask `Why did Nvidia stock drop in January?`
```


### Format [​](https://docs.langflow.org/contributing-templates#format)


Submit the template in JSON format.


### Tags [​](https://docs.langflow.org/contributing-templates#tags)


Assign the template to one of the following categories:


- Assistants
- Classification
- Coding
- Content Generation
- Q&A
- Prompting
- RAG
- Agents


For more information, see the Langflow repository's [template categories](https://github.com/langflow-ai/langflow/blob/main/src/frontend/src/modals/templatesModal/index.tsx#L27-L57).


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)

- [Create a PR to submit your template](https://docs.langflow.org/contributing-templates#create-a-pr-to-submit-your-template)
- [Required items for template submission](https://docs.langflow.org/contributing-templates#required-items-for-template-submission)
  - [Name](https://docs.langflow.org/contributing-templates#name)
  - [Description](https://docs.langflow.org/contributing-templates#description)
  - [Icons](https://docs.langflow.org/contributing-templates#icons)
  - [Flow](https://docs.langflow.org/contributing-templates#flow)
  - [Format](https://docs.langflow.org/contributing-templates#format)
  - [Tags](https://docs.langflow.org/contributing-templates#tags)[Manage Privacy Choices](https://docs.langflow.org/contributing-templates#)

---

# Import and export flows | Langflow Documentation

`https://docs.langflow.org/concepts-flows-import`

# Import and export flows

Export from projects: On the Projects page, find the flow you want to export, click More, and then select Export. To export all flows in a project, click Options on the Projects list, and then select Download.

Copy page ⌥C Version: 1.12.x On this page
## Export a flow​
## Import a flow​
## Langflow JSON file contents​
*Additional information about the flow is stored in the root data object:*

## See also​





You can export flows to transfer them between Langflow instances, share them with others, or create backups.


## Export a flow [​](https://docs.langflow.org/concepts-flows-import#export-a-flow)


There are three ways to export flows:


- **Export from projects**: On the [**Projects** page](https://docs.langflow.org/concepts-flows#projects), find the flow you want to export, click **More**, and then select **Export**. To export all flows in a project, click **Options** on the **Projects** list, and then select **Download**.
- **Export by sharing**: When editing a flow, click **Share**, and then click **Export**.
- **Export with the Langflow API**: To export one flow, use the [`/flows/download`](https://docs.langflow.org/api-flows#export-flows) endpoint. To export all flows in a project, use the [`/projects/download`](https://docs.langflow.org/api-projects#export-a-project) endpoint.


Exported flows are downloaded to your local machine as JSON files named `FLOW_NAME.json`. If you export an entire project, the JSON files are packaged in a zip archive. For more information, see [Langflow JSON file contents](https://docs.langflow.org/concepts-flows-import#langflow-json-file-contents).


### Save with my API keys [​](https://docs.langflow.org/concepts-flows-import#save-with-my-api-keys)


When exporting from the **Projects** page or **Share** menu, you can select **Save with my API keys** to export the flow *and* any defined API key variables. Non-API key variables are included in the export regardless of the **Save with my API keys** setting.


When you or another user import the flow to another Langflow instance, that instance must have Langflow global variables with the same names and valid values in order to run the flow successfully. If any variables are missing or invalid, those variables must be created or edited after importing the flow.


## Import a flow [​](https://docs.langflow.org/concepts-flows-import#import-a-flow)


You can import Langflow JSON files from your local machine in the following ways:


- **Import to projects**: On the **Projects** page, click **Upload a flow**, and then select the Langflow JSON file to import.
- **Import anywhere**: Drag and drop Langflow JSON files from your file explorer into your Langflow window to import a flow from any Langflow page.
- **Import with the Langflow API**: To import one Langflow JSON file, use the [`/flows/upload/`](https://docs.langflow.org/api-flows#import-flows) endpoint. To import a zip archive of Langflow JSON files, use the [`/projects/upload`](https://docs.langflow.org/api-projects#import-a-project) endpoint.


### Run an imported flow [​](https://docs.langflow.org/concepts-flows-import#run-an-imported-flow)


Once imported, your flow is ready to use. If the flow contains any global variables, make sure your Langflow instance has global variables with the same names and valid values. For more information, see [Save with my API keys](https://docs.langflow.org/concepts-flows-import#save-with-my-api-keys).


## Langflow JSON file contents [​](https://docs.langflow.org/concepts-flows-import#langflow-json-file-contents)


An exported flow is downloaded to your local machine as a JSON file named `FLOW_NAME.json`.


Langflow JSON files contain the following:


- [Nodes](https://docs.langflow.org/concepts-flows-import#nodes) and [edges](https://docs.langflow.org/concepts-flows-import#edges) that describe components and connections in the flow.
- [Additional metadata](https://docs.langflow.org/concepts-flows-import#additional-metadata-and-project-information) that describes the flow and the project it belongs to.


For example Langflow JSON files, you can examine any of the [https://github.com/langflow-ai/langflow/tree/main/src/backend/base/langflow/initial_setup/starter_projects[templates](https://github.com/langflow-ai/langflow/tree/main/src/backend/base/langflow/initial_setup/starter_projects%5Btemplates) in the Langflow repository], or you can create a flow from a template in Langflow, export it, and then open the exported JSON file in a text editor.


### Nodes [​](https://docs.langflow.org/concepts-flows-import#nodes)


Nodes represent the components that make up the flow. For example, this object represents a **Chat Input** component:


```json
{
  "data": {
    "description": "Get chat inputs from the Playground.",
    "display_name": "Chat Input",
    "id": "ChatInput-jFwUm",
    "node": {
      "base_classes": ["Message"],
      "description": "Get chat inputs from the Playground.",
      "display_name": "Chat Input",
      "icon": "MessagesSquare",
      "template": {
        "input_value": {
          "display_name": "Text",
          "info": "Message to be passed as input.",
          "value": "Hello"
        },
        "sender": {
          "value": "User",
          "options": ["Machine", "User"]
        },
        "sender_name": {
          "value": "User"
        },
        "should_store_message": {
          "value": true
        }
      }
    },
    "type": "ChatInput"
  },
  "position": {
    "x": 689.5720422421635,
    "y": 765.155834131403
  }
}
```


Each node has a unique identifier in the format of `NODE_NAME-UUID`, such as `ChatInput-jFwUm`.


Entrypoint nodes, such as the `ChatInput` node, are the first node executed when running a flow.


### Edges [​](https://docs.langflow.org/concepts-flows-import#edges)


Edges represent the connections between nodes.


The following example represents the edge (or connection) between the `ChatInput` node and the `OpenAIModel` node:


```json
{
  "className": "",
  "data": {
    "sourceHandle": {
      "dataType": "ChatInput",
      "id": "ChatInput-jFwUm",
      "name": "message",
      "output_types": ["Message"]
    },
    "targetHandle": {
      "fieldName": "input_value",
      "id": "OpenAIModel-OcXkl",
      "inputTypes": ["Message"],
      "type": "str"
    }
  },
  "id": "reactflow__edge-ChatInput-jFwUm{œdataTypeœ:œChatInputœ,œidœ:œChatInput-jFwUmœ,œnameœ:œmessageœ,œoutput_typesœ:[œMessageœ]}-OpenAIModel-OcXkl{œfieldNameœ:œinput_valueœ,œidœ:œOpenAIModel-OcXklœ,œinputTypesœ:[œMessageœ],œtypeœ:œstrœ}",
  "source": "ChatInput-jFwUm",
  "sourceHandle": "{œdataTypeœ: œChatInputœ, œidœ: œChatInput-jFwUmœ, œnameœ: œmessageœ, œoutput_typesœ: [œMessageœ]}",
  "target": "OpenAIModel-OcXkl",
  "targetHandle": "{œfieldNameœ: œinput_valueœ, œidœ: œOpenAIModel-OcXklœ, œinputTypesœ: [œMessageœ], œtypeœ: œstrœ}"
}
```


This edge shows that the `ChatInput` component outputs a `Message` type to the `target` node, which is the `OpenAIModel` node. The `OpenAIModel` component accepts the `Message` type at the `input_value` field.


### Additional metadata and project information [​](https://docs.langflow.org/concepts-flows-import#additional-metadata-and-project-information)


Additional information about the flow is stored in the root `data` object:


- Metadata and project information including the name, description, and `last_tested_version` of the flow. For example: ```json { "name": "Basic Prompting", "description": "Perform basic prompting with an OpenAI model.", "tags": ["chatbots"], "id": "1511c230-d446-43a7-bfc3-539e69ce05b8", "last_tested_version": "1.0.19.post2", "gradient": "2", "icon": "Braces" } ```
- Visual information about the flow defining the position of the viewport when you open the flow in the workspace: ```json "viewport": { "x": -37.61270157375441, "y": -155.91266341888854, "zoom": 0.7575251406952855 } ```
- **Notes** are comments that help explain the flow's purpose, configuration details, and any other information relevant to users who might be editing the flow. They can contain text, links, code snippets, and other information. They are encoded in Markdown format and stored as `node` objects. ```json { "id": "undefined-kVLkG", "node": { "description": "## 📖 README\nPerform basic prompting with an OpenAI model.\n\n#### Quick Start\n- Add your **OpenAI API key** to the **OpenAI Model**\n- Open the **Playground** to chat with your bot.\n..." } } ```


## See also [​](https://docs.langflow.org/concepts-flows-import#see-also)


- [Build flows](https://docs.langflow.org/concepts-flows)
- [Share and embed flows](https://docs.langflow.org/concepts-publish)


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)

- [Export a flow](https://docs.langflow.org/concepts-flows-import#export-a-flow)
  - [Save with my API keys](https://docs.langflow.org/concepts-flows-import#save-with-my-api-keys)- [Import a flow](https://docs.langflow.org/concepts-flows-import#import-a-flow)
  - [Run an imported flow](https://docs.langflow.org/concepts-flows-import#run-an-imported-flow)- [Langflow JSON file contents](https://docs.langflow.org/concepts-flows-import#langflow-json-file-contents)
  - [Nodes](https://docs.langflow.org/concepts-flows-import#nodes)
  - [Edges](https://docs.langflow.org/concepts-flows-import#edges)
  - [Additional metadata and project information](https://docs.langflow.org/concepts-flows-import#additional-metadata-and-project-information)- [See also](https://docs.langflow.org/concepts-flows-import#see-also)[Manage Privacy Choices](https://docs.langflow.org/concepts-flows-import#)

---

# Environment variables | Langflow Documentation

`https://docs.langflow.org/environment-variables`

Copy page ⌥C Version: 1.12.x On this page

In general, environment variables, like `LANGFLOW_PORT` or `LANGFLOW_LOG_LEVEL`, configure how Langflow runs. These are broad settings that apply to your entire Langflow deployment.


In contrast, global variables are user-defined values stored in Langflow's database for use in flows, such as `OPENAI_API_KEY`. Langflow can also source global variables from environment variables. For more information, see [Langflow global variables](https://docs.langflow.org/configuration-global-variables).


## Configure environment variables for Langflow OSS [​](https://docs.langflow.org/environment-variables#configure-environment-variables-for-langflow-oss)


Langflow recognizes [supported environment variables](https://docs.langflow.org/environment-variables#supported-variables) from the following sources:


- Environment variables set in your terminal.
- Environment variables imported from a `.env` file when starting Langflow.
- Environment variables set with the [Langflow CLI](https://docs.langflow.org/configuration-cli), including the `--env-file` option and direct options, such as `--port`.
## Configure environment variables for Langflow OSS​
*Langflow recognizes supported environment variables from the following sources:*

## Set environment variables for Langflow Desktop​
## Supported environment variables​





You can choose to use one or more of these sources.


### Precedence [​](https://docs.langflow.org/environment-variables#precedence)


If the same environment variable is set in multiple places, the following hierarchy applies:


1. Langflow CLI options override all other sources.
2. The `.env` file overrides system environment variables.
3. System environment variables are used only if not set elsewhere. When running a Langflow Docker image, the `-e` flag can be used to set additional system environment variables.


For example:


- If you set `LANGFLOW_PORT=8080` in your system environment and `LANGFLOW_PORT=7860` in `.env`, Langflow uses `7860` from `.env`.
- If you use the Langflow CLI to run `langflow run --env-file .env --port 9000`, and you set `LANGFLOW_PORT=7860` in `.env`, then Langflow uses `9000` from the CLI option.


### Set environment variables in your terminal [​](https://docs.langflow.org/environment-variables#configure-variables-terminal)


Run the following commands to set environment variables for your current terminal session:


- Linux or macOS
- Windows
- Docker


```bash
export VARIABLE_NAME='VALUE'
```


```text
set VARIABLE_NAME='VALUE'
```


```bash
docker run -it --rm \
    -p 7860:7860 \
    -e VARIABLE_NAME='VALUE' \
    langflowai/langflow:latest
```


When you start Langflow, it looks for environment variables that you've set in your terminal. If it detects a supported environment variable, then it automatically adopts the specified value, subject to [precedence rules](https://docs.langflow.org/environment-variables#precedence).


### Import environment variables from a .env file [​](https://docs.langflow.org/environment-variables#configure-variables-env-file)


1. If Langflow is running, quit Langflow.
2. Create a `.env` file, and then open it in your preferred editor.
3. Define [Langflow environment variables](https://docs.langflow.org/environment-variables#supported-variables) in the `.env` file.
4. Save and close `.env`.
5. Start Langflow with your `.env` file: - Local - Docker ```bash uv run langflow run --env-file .env ``` ```bash docker run -it --rm \ -p 7860:7860 \ --env-file .env \ langflowai/langflow:latest ``` If your `.env` file isn't in the same directory, provide the path to your `.env` file.


On startup, Langflow imports the environment variables from your `.env` file, as well as any others that you set in your terminal, and then adopts their specified values.


### Configure environment variables for development [​](https://docs.langflow.org/environment-variables#configure-environment-variables-for-development)


The following examples show how to configure Langflow using environment variables in different development scenarios.


- .env file
- Systemd service
- VSCode tasks.json


The `.env` file is a text file that contains key-value pairs of environment variables.


Create or edit a `.env` file in the root directory of your application or Langflow environment, and then add your configuration variables to the file:


A systemd service configuration file configures Linux system services.


To add environment variables, create or edit a service configuration file and add an `override.conf` file. This file allows you to override the default environment variables for the service.


For more information on systemd, see the [Red Hat documentation](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/using_systemd_unit_files_to_customize_and_optimize_your_system/assembly_working-with-systemd-unit-files_working-with-systemd).


The `tasks.json` file located in `.vscode/tasks.json` is a configuration file for development environments using Visual Studio Code.


Create or edit the `.vscode/tasks.json` file in your project root.


To run Langflow using the above VSCode `tasks.json` file, in the VSCode command palette, select **Tasks: Run Task** > **langflow backend**.


## Set environment variables for Langflow Desktop [​](https://docs.langflow.org/environment-variables#set-environment-variables-for-langflow-desktop)


Environment variables set in your terminal aren't automatically available to GUI-based applications like Langflow Desktop when you launch them from the Windows or macOS GUI.


To modify environment variables for Langflow Desktop, set environment variables in a Desktop `.env` file, and then restart the app.


- macOS
- Windows .env file
- Windows user environment variables


To modify the macOS `.env` file, do the following:


1. Create or edit `~/.langflow/data/.env`.
2. Add your Langflow environment variables, for example: ```text LANGFLOW_LOG_LEVEL=info LANGFLOW_DOCLING=true ```
3. Save the file.
4. Restart Langflow Desktop.


To modify the Windows `.env` file, do the following:


1. Create or edit `%APPDATA%\com.LangflowDesktop\data\.env`.
2. Add your Langflow environment variables, for example: ```text LANGFLOW_LOG_LEVEL=info LANGFLOW_DOCLING=true ```
3. Save the file.
4. Restart Langflow Desktop.


Windows supports two sources for Langflow Desktop environment variables: a Langflow application `.env` file, and Windows user environment variables.


The `.env` file at `%APPDATA%\com.LangflowDesktop\data\.env` is the recommended approach, but Windows user variables are useful for single-sourcing API keys between Langflow and other Windows applications. If the same variable is defined in both the Langflow application `.env` file and as a Windows user environment variable, the `.env` file takes precedence.


To modify the Windows user environment variables, do the following:


1. Press Win + R, enter `sysdm.cpl`, and then press Enter.
2. Click the **Advanced** tab, and then click **Environment Variables**.
3. In **User variables**, click **New**.
4. Enter the variable name, such as `OPENAI_API_KEY`, and its value.
5. Click **OK**, and then **restart Langflow Desktop**.


## Supported environment variables [​](https://docs.langflow.org/environment-variables#supported-variables)


The following sections provide information about specific Langflow environment variables.


### Authentication and security [​](https://docs.langflow.org/environment-variables#authentication-and-security)


See [API keys and authentication](https://docs.langflow.org/api-keys-and-authentication).


### Global variables [​](https://docs.langflow.org/environment-variables#global-variables)


For information about the relationship between Langflow global variables and environment variables, as well as environment variables that control handling of global variables, see [Global variables](https://docs.langflow.org/configuration-global-variables).


### Logs [​](https://docs.langflow.org/environment-variables#logging)


See [Configure log options](https://docs.langflow.org/logging#log-storage).


### MCP servers [​](https://docs.langflow.org/environment-variables#mcp)


See [Use Langflow as an MCP server](https://docs.langflow.org/mcp-server).


### A2A agents [​](https://docs.langflow.org/environment-variables#a2a)


See [A2A environment variables](https://docs.langflow.org/a2a-server#a2a-environment-variables).


### Multi-worker deployments [​](https://docs.langflow.org/environment-variables#multi-worker-deployments)


For multi-worker tuning—including the Redis job queue and Gunicorn worker settings—see [Deploy Langflow with multiple workers](https://docs.langflow.org/deployment-multi-worker).


### Monitoring and metrics [​](https://docs.langflow.org/environment-variables#monitoring-and-metrics)


For OpenTelemetry traces, metrics, and logs that describe Langflow service health, including `LANGFLOW_OTEL_*` and `OTEL_EXPORTER_OTLP_*`, see [OpenTelemetry](https://docs.langflow.org/observability-opentelemetry).


For prompt-level LLM tracing, see [Langfuse](https://docs.langflow.org/integrations-langfuse) and the other monitoring integrations. For Prometheus on Kubernetes, see [Best practices for Langflow on Kubernetes](https://docs.langflow.org/deployment-prod-best-practices).


### Server [​](https://docs.langflow.org/environment-variables#server)


The following environment variables set base Langflow server configuration, such as where the server is hosted, required files for SSL encryption, and the deployment type (frontend and backend, backend-only, development mode).


| Variable | Format | Default | Description |
| --- | --- | --- | --- |
| `LANGFLOW_​HOST` | String | `localhost` | The host on which the Langflow server will run. |
| `LANGFLOW_​PORT` | Integer | `7860` | The port on which the Langflow server runs. The server automatically selects a free port if the specified port is in use. |
| `LANGFLOW_​BACKEND_​ONLY` | Boolean | `False` | Run only the Langflow backend service (no frontend). |
| `LANGFLOW_​DEV` | Boolean | `False` | Whether to run Langflow in development mode (may contain bugs). |
| `LANGFLOW_​DEPLOYMENT_​PROFILE` | String | `dev` | Deployment profile. `dev` skips production checks. `prod` runs [production preflight](https://docs.langflow.org/deployment-prod-best-practices#production-preflight) before the server starts and aborts boot if a required service is missing. |
| `LANGFLOW_​OPEN_​BROWSER` | Boolean | `False` | Open the system web browser on startup. |
| `LANGFLOW_​HEALTH_​CHECK_​MAX_​RETRIES` | Integer | `5` | Set the maximum number of retries for Langflow's server status health checks. |
| `LANGFLOW_​WORKERS` | Integer | `1` | Number of worker processes. See [Deploy Langflow with multiple workers](https://docs.langflow.org/deployment-multi-worker#recommended-gunicorn-settings). |
| `LANGFLOW_​WORKER_​TIMEOUT` | Integer | `300` | Worker timeout in seconds. See [Deploy Langflow with multiple workers](https://docs.langflow.org/deployment-multi-worker#recommended-gunicorn-settings). |
| `LANGFLOW_​GUNICORN_​PRELOAD` | Boolean | `False` | Enables Gunicorn `preload_​app`. Non-Windows only. See [Deploy Langflow with multiple workers](https://docs.langflow.org/deployment-multi-worker#recommended-gunicorn-settings). |
| `LANGFLOW_​JOB_​QUEUE_​TYPE` | String | `asyncio` | Job queue backend. Use `redis` for multi-worker deployments. See [Deploy Langflow with multiple workers](https://docs.langflow.org/deployment-multi-worker#configuration-reference). |
| `LANGFLOW_​DANGEROUSLY_​ALLOW_​MULTI_​WORKER_​WITHOUT_​SHARED_​QUEUE` | Boolean | `False` | Allow startup with `LANGFLOW_​WORKERS` greater than 1 while `LANGFLOW_​JOB_​QUEUE_​TYPE` is `asyncio`. **Unsupported with the Langflow UI and with MCP over SSE.** See [Run multiple workers without Redis](https://docs.langflow.org/deployment-multi-worker#run-multiple-workers-without-redis). |
| `LANGFLOW_​SSL_​CERT_​FILE` | String | Not set | Path to the SSL certificate file for enabling HTTPS on the Langflow web server. This is separate from [database SSL connections](https://docs.langflow.org/configuration-custom-database#connect-langflow-to-a-local-postgresql-database). |
| `LANGFLOW_​SSL_​KEY_​FILE` | String | Not set | Path to the SSL key file for enabling HTTPS on the Langflow web server. This is separate from [database SSL connections](https://docs.langflow.org/configuration-custom-database#connect-langflow-to-a-local-postgresql-database). |
| `LANGFLOW_​DEACTIVATE_​TRACING` | Boolean | `False` | Deactivate tracing functionality. |
| `LANGFLOW_​CELERY_​ENABLED` | Boolean | `False` | Enable Celery for distributed task processing. |
| `LANGFLOW_​ALEMBIC_​LOG_​TO_​STDOUT` | Boolean | `False` | Whether to log Alembic database migration output to stdout instead of a log file. If `true`, Alembic logs to `stdout` and the default log file is ignored. |


### Storage [​](https://docs.langflow.org/environment-variables#storage)


For file storage environment variables, see [File storage environment variables](https://docs.langflow.org/concepts-file-management#file-storage-environment-variables).


For database environment variables, including PostgreSQL configuration, see [Memory management options](https://docs.langflow.org/memory#configure-external-memory).


### Telemetry [​](https://docs.langflow.org/environment-variables#telemetry)


Anonymous product usage telemetry is separate from OpenTelemetry export.


See [Telemetry](https://docs.langflow.org/contributing-telemetry) to opt out with `DO_NOT_TRACK`.


### OpenTelemetry [​](https://docs.langflow.org/environment-variables#opentelemetry)


Langflow can export service-health traces, metrics, and logs over OTLP to **your** backend. This is not LLM tracing and is not the anonymous product telemetry above.


Set `OTEL_EXPORTER_OTLP_ENDPOINT` to enable export. If it is unset, Langflow installs no providers.


| Variable | Format | Default | Description |
| --- | --- | --- | --- |
| `OTEL_​EXPORTER_​OTLP_​ENDPOINT` | String | Not set | OTLP collector or APM endpoint. Required to enable export. |
| `LANGFLOW_​OTEL_​DB_​SPANS` | Boolean | `True` | Whether to export SQLAlchemy database spans. Set to `false` to send flow and request spans only. |
| `LANGFLOW_​OTEL_​LOG_​LEVEL` | String | `INFO` | Minimum severity exported over OTLP. `DEBUG` exports more records (flow inputs and outputs are logged at `DEBUG`) but withholds their bodies unless `LANGFLOW_​OTEL_​LOG_​BODIES=all` is also set. |
| `LANGFLOW_​OTEL_​LOG_​BODIES` | String | `allowlist` | Set to `all` to export log message bodies, including completions and chat history. |


Standard OpenTelemetry SDK variables such as `OTEL_SERVICE_NAME` and `OTEL_EXPORTER_OTLP_HEADERS` also apply. To verify the pipeline, run [`langflow observability doctor`](https://docs.langflow.org/configuration-cli#langflow-observability-doctor).


For the full list, what Langflow does and does not export, and vendor setup, see [OpenTelemetry](https://docs.langflow.org/observability-opentelemetry).


### Python Interpreter sandbox [​](https://docs.langflow.org/environment-variables#langflow-sandbox)


These variables control the optional QEMU microVM backend for the [**Python Interpreter** component](https://docs.langflow.org/python-interpreter#sandbox). They are not included in a default `uv pip install langflow` installation. Install `langflow[sandbox]` first.


| Variable | Format | Default | Description |
| --- | --- | --- | --- |
| `LANGFLOW_​SANDBOX_​BACKEND` | String | `none` | Execution backend for the code-execution components (Python Interpreter and the legacy Python REPL tool). Set to `exec-sandbox` to run user code in a dedicated QEMU microVM per execution instead of in-process. Requires `uv pip install 'langflow[sandbox]'`, Python 3.12 or later, and QEMU 8+ with hardware virtualization (KVM on Linux, HVF on macOS). When configured but unavailable — including hosts without a hardware hypervisor — execution fails with an error instead of falling back to in-process execution. |
| `LANGFLOW_​SANDBOX_​TIMEOUT_​SECONDS` | Integer | `30` | Wall-clock limit for one sandboxed execution (1-300 seconds). Only used when `LANGFLOW_​SANDBOX_​BACKEND` is not `none`. |
| `LANGFLOW_​SANDBOX_​MEMORY_​MB` | Integer | `192` | Guest VM memory for sandboxed executions, in MB (minimum 128). Only used when `LANGFLOW_​SANDBOX_​BACKEND` is not `none`. |
| `LANGFLOW_​SANDBOX_​ALLOW_​NETWORK` | Boolean | `False` | Whether sandboxed code may access the network. The default runs the microVM fully offline. When enabled without `LANGFLOW_​SANDBOX_​ALLOWED_​DOMAINS`, only exec-sandbox's package-registry defaults (PyPI) are reachable. Only used when `LANGFLOW_​SANDBOX_​BACKEND` is not `none`. |
| `LANGFLOW_​SANDBOX_​ALLOWED_​DOMAINS` | String | Not set | Comma-separated list of domains sandboxed code may reach when network access is enabled. Treat like an SSRF allow-list: prefer narrow, fully-qualified domains. Only used when `LANGFLOW_​SANDBOX_​BACKEND` is not `none`. |
| `LANGFLOW_​SANDBOX_​ALLOW_​SOFTWARE_​EMULATION` | Boolean | `False` | Permit the sandbox to run without a hardware hypervisor, letting QEMU fall back to TCG software emulation. Upstream documents TCG as not security-supported, so enable only for trusted/development workloads. Only used when `LANGFLOW_​SANDBOX_​BACKEND` is not `none`. |


### Visual editor and Playground behavior [​](https://docs.langflow.org/environment-variables#visual-editor-and-playground-behavior)


| Variable | Format | Default | Description |
| --- | --- | --- | --- |
| `LANGFLOW_​AUTO_​SAVING` | Boolean | `True` | Whether to automatically save the current flow draft. Auto-save only updates the live draft, and doesn't create [saved flow versions](https://docs.langflow.org/concepts-flows#save-and-restore-flow-versions). |
| `LANGFLOW_​AUTO_​SAVING_​INTERVAL` | Integer | `1000` | Set the auto-save interval in milliseconds if `LANGFLOW_​AUTO_​SAVING=True`. |
| `LANGFLOW_​BUNDLE_​URLS` | List[String] | `[]` | A list of URLs from which to load custom bundles. Supports GitHub URLs. If `LANGFLOW_​AUTO_​LOGIN=True`, flows from these bundles are loaded into the database. |
| `LANGFLOW_​COMPONENTS_​PATH` | String | Not set | Path to a directory containing custom components. Typically used if you have local custom components or you are building a Docker image with custom components. |
| `LANGFLOW_​COMPONENTS_​INDEX_​PATH` | String | Not set | File path or URL (`http://` or `https://`) to a prebuilt component index JSON file used to populate built-in components in the visual editor. When not set, Langflow uses the included index. Useful for supplying a curated component index, for example in airgapped deployments. For more information, see [Block custom components](https://docs.langflow.org/deployment-block-custom-components). |
| `LANGFLOW_​AGENTIC_​EXPERIENCE` | Boolean | `True` | Whether [Langflow Assistant](https://docs.langflow.org/langflow-assistant) is available. Set to `false` to turn it off for a deployment, for example if you don't want model-generated component code running on your server. The Assistant's endpoints then return `404` and its `run_​assistant` MCP tool is unavailable, but the rest of the MCP toolkit at `/api/v1/agentic/mcp` is unaffected. To block code execution itself, including hand-written custom components, use `LANGFLOW_​ALLOW_​CUSTOM_​COMPONENTS`. |
| `LANGFLOW_​ASSISTANT_​MAX_​MESSAGE_​LENGTH` | Integer | `2000` | Maximum length, in characters, of a single message sent to [Langflow Assistant](https://docs.langflow.org/langflow-assistant). The limit is enforced by the Assistant API and mirrored to the visual editor, which blocks sending a longer message instead of truncating it. Raise it for users who paste long specifications into the Assistant; longer messages cost more per turn. |
| `LANGFLOW_​ASSISTANT_​HISTORY_​TURNS` | Integer | `6` | How many prior conversation turns [Langflow Assistant](https://docs.langflow.org/langflow-assistant) injects into its prompt. The block is re-sent on every agent iteration, so this is a direct per-request token-cost lever: raise it for longer memory and accept the cost, or set `0` to inject no history. Values that aren't a number fall back to the default. |
| `LANGFLOW_​ASSISTANT_​VERIFY_​FLOWS` | Boolean | `True` | Whether [Langflow Assistant](https://docs.langflow.org/langflow-assistant) runs a flow it just built before presenting it, repairing fixable failures and adding a caveat to the reply when it can't. Set to `false` to deliver flows unverified, which is faster and cheaper but removes the guarantee that a delivered flow ran at least once. |
| `LANGFLOW_​ALLOW_​CUSTOM_​COMPONENTS` | Boolean | `True` | If `false`, disables custom components, in-editor editing of component code, and registered built-in code-execution components at runtime. This feature is in beta. For more information, see [Block custom components](https://docs.langflow.org/deployment-block-custom-components) and [Component hardening for untrusted users](https://docs.langflow.org/api-keys-and-authentication#multi-tenant-component-hardening). |
| `LANGFLOW_​ALLOW_​PUBLIC_​CUSTOM_​COMPONENTS` | Boolean | `False` | Whether flows shared through the **Shareable Playground** can run custom component code. By default, an unauthenticated public flow build runs only the server's own copy of each component, and a flow containing a custom component is refused with `This flow cannot be executed.` Set to `true` to build public flows from the database as their owner. This requires `LANGFLOW_​ALLOW_​CUSTOM_​COMPONENTS=true`, and it lets every node in a public flow run the code stored in that flow, not only the custom ones. To run a custom component in a shared **Playground** without relaxing that, install the component on the server with `LANGFLOW_​COMPONENTS_​PATH` instead. For more information, see [Custom components in publicly shared flows](https://docs.langflow.org/deployment-block-custom-components#public-flow-custom-components). |
| `LANGFLOW_​ALLOW_​COMPONENTS_​PATHS_​OVERRIDE` | Boolean | `True` | When `false` alongside `LANGFLOW_​ALLOW_​CUSTOM_​COMPONENTS=false`, components contributed by `LANGFLOW_​COMPONENTS_​PATH` and `LANGFLOW_​COMPONENTS_​INDEX_​PATH` no longer bypass the block. Has no effect when `LANGFLOW_​ALLOW_​CUSTOM_​COMPONENTS=true`. For more information, see [Block custom components](https://docs.langflow.org/deployment-block-custom-components). |
| `LANGFLOW_​SUBSTITUTE_​OUTDATED_​COMPONENT_​CODE` | Boolean | `True` | Only applies when `LANGFLOW_​ALLOW_​CUSTOM_​COMPONENTS=false`, where a flow's stored component code never runs anyway. By default, a node whose component type this server knows but whose stored code has drifted across an upgrade is rebuilt with this server's copy of that component, and the substitution is logged. Set to `false` to refuse those flows until each component is updated. Unrecognized component types are refused either way. For more information, see [Block custom components](https://docs.langflow.org/deployment-block-custom-components#upgrading-with-custom-components-blocked). |
| `LANGFLOW_​BLOCK_​CODE_​INTERPRETER_​COMPONENTS` | Boolean | `False` | If `true`, blocks built-in code-execution components (Python Interpreter, REPL/Code tools, Smart Transform, and code-running agents). See [Component hardening for untrusted users](https://docs.langflow.org/api-keys-and-authentication#multi-tenant-component-hardening). |
| `LANGFLOW_​RESTRICT_​LOCAL_​FILE_​ACCESS` | Boolean | `False` | If `true`, confines built-in file components to the upload storage directory and blocks local-file SQL dialects and local Git clones. See [Component hardening for untrusted users](https://docs.langflow.org/api-keys-and-authentication#multi-tenant-component-hardening). |
| `LANGFLOW_​MCP_​SERVER_​DOCKER_​HARDENING` | Boolean | `False` | If `true`, applies a strict Docker-argument policy to MCP stdio servers that use the `docker` transport. See [Component hardening for untrusted users](https://docs.langflow.org/api-keys-and-authentication#multi-tenant-component-hardening). |
| `LANGFLOW_​MCP_​SERVER_​ENV_​ALLOWLIST` | String | Not set | Comma-separated allowlist of environment-variable names an MCP stdio config may set. Production preflight warns when this is unset. An empty value blocks all tenant-supplied environment variables. See [MCP server environment variables](https://docs.langflow.org/mcp-server#mcp-server-environment-variables). |
| `LANGFLOW_​TWEAKS_​POLICY` | String | `permissive` | Which component fields a run request may set through `tweaks`. For more information, see [Restrict API tweaks](https://docs.langflow.org/deployment-tweaks-policy). |
| `LANGFLOW_​LOAD_​FLOWS_​PATH` | String | Not set | Path to a directory containing flow JSON files to be loaded on startup. Typically used when creating a Docker image with prepackaged flows. Requires `LANGFLOW_​AUTO_​LOGIN=True`. |
| `LANGFLOW_​LOAD_​FLOWS_​OVERWRITE_​ON_​NAME_​MATCH` | Boolean | `False` | When a flow file in `LANGFLOW_​LOAD_​FLOWS_​PATH` shares a name with an existing DB row but has a different `id`, controls whether to overwrite the existing row. `False` (default) skips with a warning so UI edits are preserved on restart when file UUIDs regenerate. Set to `True` to opt into prepackaged-flows-are-source-of-truth semantics, typically for CI/CD pipelines. |
| `LANGFLOW_​LOAD_​FLOWS_​PRESERVE_​VARIABLE_​BINDINGS` | Boolean | `True` | Preserve global-variable bindings configured in the visual editor when an existing flow is reloaded from `LANGFLOW_​LOAD_​FLOWS_​PATH`. Bindings explicitly configured in the flow file still take precedence. Set to `False` to restore blind replacement of the flow data on restart. |
| `LANGFLOW_​CREATE_​STARTER_​PROJECTS` | Boolean | `True` | Whether to create templates during initialization. If `false`, Langflow doesn't create templates, and `LANGFLOW_​UPDATE_​STARTER_​PROJECTS` is treated as `false`. |
| `LANGFLOW_​UPDATE_​STARTER_​PROJECTS` | Boolean | `True` | Whether to update templates with the latest component versions when initializing after an upgrade. |
| `LANGFLOW_​LAZY_​LOAD_​COMPONENTS` | Boolean | `False` | If `true`, Langflow only partially loads components at startup and fully loads them on demand. This significantly reduces startup time but can cause a slight delay when a component is first used. |
| `LANGFLOW_​EVENT_​DELIVERY` | String | `streaming` | How to deliver build events to the frontend: `polling`, `streaming` or `direct`. |
| `LANGFLOW_​FRONTEND_​PATH` | String | `./frontend` | Path to the frontend directory containing build files. For development purposes only when you need to serve specific frontend code. |
| `LANGFLOW_​FS_​TOOL_​BASE_​DIR` | String | `~/.langflow/fs_​tool/fs_​sandbox` | Base directory for the [**File System** component](https://docs.langflow.org/file-system) sandbox. All agent file operations are confined to this directory. |
| `LANGFLOW_​MAX_​ITEMS_​LENGTH` | Integer | `100` | Maximum number of items to store and display in the visual editor. Lists longer than this will be truncated when displayed in the visual editor. Doesn't affect outputs or data passed between components. |
| `LANGFLOW_​MAX_​TEXT_​LENGTH` | Integer | `1000` | Maximum number of characters to store and display in the visual editor. Responses longer than this will be truncated when displayed in the visual editor. Doesn't truncate outputs or responses passed between components. |
| `LANGFLOW_​MAX_​TRANSACTIONS_​TO_​KEEP` | Integer | `3000` | Maximum number of flow transaction events to keep in the database. |
| `LANGFLOW_​MAX_​VERTEX_​BUILDS_​TO_​KEEP` | Integer | `3000` | Maximum number of vertex builds to keep in the database. Relates to [Playground](https://docs.langflow.org/concepts-playground) functionality. |
| `LANGFLOW_​MAX_​VERTEX_​BUILDS_​PER_​VERTEX` | Integer | `2` | Maximum number of builds to keep per vertex. Older builds are deleted. Relates to [Playground](https://docs.langflow.org/concepts-playground) functionality. |
| `LANGFLOW_​PUBLIC_​FLOW_​CLEANUP_​INTERVAL` | Integer | `3600` | The interval in seconds at which data for [shared Playground](https://docs.langflow.org/concepts-playground#share-a-flows-playground) flows are cleaned up. Default: 3600 seconds (1 hour). Minimum: 600 seconds (10 minutes). |
| `LANGFLOW_​PUBLIC_​FLOW_​EXPIRATION` | Integer | `86400` | The time in seconds after which a [shared Playground](https://docs.langflow.org/concepts-playground#share-a-flows-playground) flow is considered expired and eligible for cleanup. Default: 86400 seconds (24 hours). Minimum: 600 seconds (10 minutes). |


### Hide UI elements with embedded mode [​](https://docs.langflow.org/environment-variables#embedded-mode)


When you embed the Langflow visual editor in another application, such as an iframe within a host portal, you can hide UI elements that are usually visible in the visual editor.


The embedded mode environment variables control which UI elements appear in the visual editor. Embedded mode controls UI visibility only, and does not block API endpoints or deploy Langflow.


Embedded mode is distinct from the [embedded chat widget](https://docs.langflow.org/concepts-publish#embedded-chat-widget), which embeds a single flow's chat UI in a website.


When `LANGFLOW_EMBEDDED_MODE=true`, Langflow hides the following buttons in the UI:


- **Logout**
- **New project**
- **New flow**
- **Starter projects**


You can hide individual elements without enabling the umbrella flag.


| Variable | Format | Default | Description |
| --- | --- | --- | --- |
| `LANGFLOW_​EMBEDDED_​MODE` | Boolean | `False` | Umbrella flag for embedded or iframe deployments. When `true`, hides standalone UI elements: logout, new project, new flow, and starter projects. Individual hide flags can also be set without enabling this flag. |
| `LANGFLOW_​HIDE_​LOGOUT_​BUTTON` | Boolean | `False` | If `true`, hides the logout button in the account menu. Automatically enabled when `LANGFLOW_​EMBEDDED_​MODE=true`. |
| `LANGFLOW_​HIDE_​NEW_​PROJECT_​BUTTON` | Boolean | `False` | If `true`, hides the new project/folder button in the sidebar. Automatically enabled when `LANGFLOW_​EMBEDDED_​MODE=true`. |
| `LANGFLOW_​HIDE_​NEW_​FLOW_​BUTTON` | Boolean | `False` | If `true`, hides the new flow button in the header. Automatically enabled when `LANGFLOW_​EMBEDDED_​MODE=true`. |
| `LANGFLOW_​HIDE_​STARTER_​PROJECTS` | Boolean | `False` | If `true`, hides the starter projects tab in the templates modal. Does not affect database seeding of starter projects. Automatically enabled when `LANGFLOW_​EMBEDDED_​MODE=true`. |
| `LANGFLOW_​HIDE_​GETTING_​STARTED_​PROGRESS` | Boolean | `False` | If `true`, hides the getting-started onboarding progress UI. Not automatically enabled when `LANGFLOW_​EMBEDDED_​MODE=true`. |


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)

- [Configure environment variables for Langflow OSS](https://docs.langflow.org/environment-variables#configure-environment-variables-for-langflow-oss)
  - [Precedence](https://docs.langflow.org/environment-variables#precedence)
  - [Set environment variables in your terminal](https://docs.langflow.org/environment-variables#configure-variables-terminal)
  - [Import environment variables from a .env file](https://docs.langflow.org/environment-variables#configure-variables-env-file)
  - [Configure environment variables for development](https://docs.langflow.org/environment-variables#configure-environment-variables-for-development)- [Set environment variables for Langflow Desktop](https://docs.langflow.org/environment-variables#set-environment-variables-for-langflow-desktop)
- [Supported environment variables](https://docs.langflow.org/environment-variables#supported-variables)
  - [Authentication and security](https://docs.langflow.org/environment-variables#authentication-and-security)
  - [Global variables](https://docs.langflow.org/environment-variables#global-variables)
  - [Logs](https://docs.langflow.org/environment-variables#logging)
  - [MCP servers](https://docs.langflow.org/environment-variables#mcp)
  - [A2A agents](https://docs.langflow.org/environment-variables#a2a)
  - [Multi-worker deployments](https://docs.langflow.org/environment-variables#multi-worker-deployments)
  - [Monitoring and metrics](https://docs.langflow.org/environment-variables#monitoring-and-metrics)
  - [Server](https://docs.langflow.org/environment-variables#server)
  - [Storage](https://docs.langflow.org/environment-variables#storage)
  - [Telemetry](https://docs.langflow.org/environment-variables#telemetry)
  - [OpenTelemetry](https://docs.langflow.org/environment-variables#opentelemetry)
  - [Python Interpreter sandbox](https://docs.langflow.org/environment-variables#langflow-sandbox)
  - [Visual editor and Playground behavior](https://docs.langflow.org/environment-variables#visual-editor-and-playground-behavior)
  - [Hide UI elements with embedded mode](https://docs.langflow.org/environment-variables#embedded-mode)[Manage Privacy Choices](https://docs.langflow.org/environment-variables#)

---

# Flow management endpoints | Langflow Documentation

`https://docs.langflow.org/api-flows`

# Flow management endpoints
*If you want to use the Langflow API to run a flow, see Flow trigger endpoints.*

## Create flow​
## Create flows​
## Read flow​
## Read flows​
*To retrieve flows from a specific project, use the project_id query parameter:*

## Read sample flows​
## Update flow​
## Delete flow​
## Export flows​
## Import flows​










Use the /flows endpoint to create, read, update, and delete flows.

Copy page ⌥C Version: 1.12.x On this page

Use the `/flows` endpoint to create, read, update, and delete flows.


If you want to use the Langflow API to run a flow, see [Flow trigger endpoints](https://docs.langflow.org/api-flows-run).


## Create flow [​](https://docs.langflow.org/api-flows#create-flow)


Creates a new flow.


- Python
- JavaScript
- curl


```python
import os

import requests

url = f"{os.getenv('LANGFLOW_URL', '')}/api/v1/flows/"

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
    "x-api-key": f"{os.getenv('LANGFLOW_API_KEY', '')}",
}

payload = {
    "name": "string2",
    "description": "string",
    "icon": "string",
    "icon_bg_color": "#FF0000",
    "gradient": "string",
    "data": {},
    "is_component": False,
    "updated_at": "2024-12-30T15:48:01.519Z",
    "webhook": False,
    "endpoint_name": "string",
    "tags": ["string"],
}

response = requests.request("POST", url, headers=headers, json=payload)
response.raise_for_status()

print(response.text)
```


```js
const url = `${process.env.LANGFLOW_URL ?? ""}/api/v1/flows/`;

const options = {
  method: 'POST',
  headers: {
    "accept": `application/json`,
    "Content-Type": `application/json`,
    "x-api-key": `${process.env.LANGFLOW_API_KEY ?? ""}`,
  },
  body: JSON.stringify({
  "name": "string2",
  "description": "string",
  "icon": "string",
  "icon_bg_color": "#FF0000",
  "gradient": "string",
  "data": {},
  "is_component": false,
  "updated_at": "2024-12-30T15:48:01.519Z",
  "webhook": false,
  "endpoint_name": "string",
  "tags": [
    "string"
  ]
}),
};

fetch(url, options)
  .then(async (response) => {
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    const text = await response.text();
    console.log(text);
  })
  .catch((error) => console.error(error));
```


```bash
curl -X POST \
  "$LANGFLOW_URL/api/v1/flows/" \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -H "x-api-key: $LANGFLOW_API_KEY" \
  -d '{
  "name": "string2",
  "description": "string",
  "icon": "string",
  "icon_bg_color": "#FF0000",
  "gradient": "string",
  "data": {},
  "is_component": false,
  "updated_at": "2024-12-30T15:48:01.519Z",
  "webhook": false,
  "endpoint_name": "string",
  "tags": [
    "string"
  ]
}'
```


## Create flows [​](https://docs.langflow.org/api-flows#create-flows)


Creates multiple new flows, returning an array of flow objects.


- Python
- JavaScript
- curl


```python
import os
import uuid

import requests

base = os.environ.get("LANGFLOW_URL", "")
api_key = os.environ.get("LANGFLOW_API_KEY", "")
folder_id = (os.environ.get("PROJECT_ID") or os.environ.get("FOLDER_ID") or "").strip()

headers = {"accept": "application/json", "Content-Type": "application/json", "x-api-key": api_key}


def _flow_doc(suffix: str) -> dict:
    doc = {
        "name": f"batch-flow-{uuid.uuid4().hex[:8]}",
        "description": f"Docs batch example {suffix}",
        "data": {"nodes": [], "edges": []},
    }
    if folder_id:
        doc["folder_id"] = folder_id
    return doc


payload = {"flows": [_flow_doc("A"), _flow_doc("B")]}

response = requests.post(f"{base}/api/v1/flows/batch/", headers=headers, json=payload, timeout=30)
response.raise_for_status()
print(response.text)
```


```js
const url = `${process.env.LANGFLOW_URL ?? ""}/api/v1/flows/batch/`;

const options = {
  method: 'POST',
  headers: {
    "accept": `application/json`,
    "Content-Type": `application/json`,
    "x-api-key": `${process.env.LANGFLOW_API_KEY ?? ""}`,
  },
  body: JSON.stringify({
  "flows": [
    {
      "name": "string",
      "description": "string",
      "icon": "string",
      "icon_bg_color": "string",
      "gradient": "string",
      "data": {},
      "is_component": false,
      "updated_at": "2024-12-30T18:36:02.737Z",
      "webhook": false,
      "endpoint_name": "string",
      "tags": [
        "string"
      ],
      "locked": false,
      "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "project_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
    },
    {
      "name": "string",
      "description": "string",
      "icon": "string",
      "icon_bg_color": "string",
      "gradient": "string",
      "data": {},
      "is_component": false,
      "updated_at": "2024-12-30T18:36:02.737Z",
      "webhook": false,
      "endpoint_name": "string",
      "tags": [
        "string"
      ],
      "locked": false,
      "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "project_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
    }
  ]
}),
};

fetch(url, options)
  .then(async (response) => {
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    const text = await response.text();
    console.log(text);
  })
  .catch((error) => console.error(error));
```


```bash
curl -X POST \
  "$LANGFLOW_URL/api/v1/flows/batch/" \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -H "x-api-key: $LANGFLOW_API_KEY" \
  -d '{
  "flows": [
    {
      "name": "string",
      "description": "string",
      "icon": "string",
      "icon_bg_color": "string",
      "gradient": "string",
      "data": {},
      "is_component": false,
      "updated_at": "2024-12-30T18:36:02.737Z",
      "webhook": false,
      "endpoint_name": "string",
      "tags": [
        "string"
      ],
      "locked": false,
      "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "project_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
    },
    {
      "name": "string",
      "description": "string",
      "icon": "string",
      "icon_bg_color": "string",
      "gradient": "string",
      "data": {},
      "is_component": false,
      "updated_at": "2024-12-30T18:36:02.737Z",
      "webhook": false,
      "endpoint_name": "string",
      "tags": [
        "string"
      ],
      "locked": false,
      "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "project_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
    }
  ]
}'
```


## Read flow [​](https://docs.langflow.org/api-flows#read-flow)


Retrieves a specific flow by its ID.


- Python
- JavaScript
- curl


```python
import os

import requests

url = f"{os.getenv('LANGFLOW_URL', '')}/api/v1/flows/{os.getenv('FLOW_ID', '')}"

headers = {
    "accept": "application/json",
    "x-api-key": f"{os.getenv('LANGFLOW_API_KEY', '')}",
}

response = requests.request("GET", url, headers=headers)
response.raise_for_status()

print(response.text)
```


```js
const url = `${process.env.LANGFLOW_URL ?? ""}/api/v1/flows/${process.env.FLOW_ID ?? ""}`;

const options = {
  method: 'GET',
  headers: {
    "accept": `application/json`,
    "x-api-key": `${process.env.LANGFLOW_API_KEY ?? ""}`,
  },
};

fetch(url, options)
  .then(async (response) => {
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    const text = await response.text();
    console.log(text);
  })
  .catch((error) => console.error(error));
```


```bash
curl -X GET \
  "$LANGFLOW_URL/api/v1/flows/$FLOW_ID" \
  -H "accept: application/json" \
  -H "x-api-key: $LANGFLOW_API_KEY"
```


## Read flows [​](https://docs.langflow.org/api-flows#read-flows)


Returns a JSON object containing a list of flows.


Retrieve all flows with pagination:


- Python
- JavaScript
- curl


```python
import os

import requests

url = f"{os.getenv('LANGFLOW_URL', '')}/api/v1/flows/?remove_example_flows=false&components_only=false&get_all=true&header_flows=false&page=1&size=50"

headers = {
    "accept": "application/json",
    "x-api-key": f"{os.getenv('LANGFLOW_API_KEY', '')}",
}

response = requests.request("GET", url, headers=headers)
response.raise_for_status()

print(response.text)
```


```js
const url = `${process.env.LANGFLOW_URL ?? ""}/api/v1/flows/?remove_example_flows=false&components_only=false&get_all=true&header_flows=false&page=1&size=50`;

const options = {
  method: 'GET',
  headers: {
    "accept": `application/json`,
    "x-api-key": `${process.env.LANGFLOW_API_KEY ?? ""}`,
  },
};

fetch(url, options)
  .then(async (response) => {
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    const text = await response.text();
    console.log(text);
  })
  .catch((error) => console.error(error));
```


```bash
curl -X GET \
  "$LANGFLOW_URL/api/v1/flows/?remove_example_flows=false&components_only=false&get_all=true&header_flows=false&page=1&size=50" \
  -H "accept: application/json" \
  -H "x-api-key: $LANGFLOW_API_KEY"
```


To retrieve flows from a specific project, use the `project_id` query parameter:


- Python
- JavaScript
- curl


```python
import os

import requests

url = f"{os.getenv('LANGFLOW_URL', '')}/api/v1/flows/?remove_example_flows=true&components_only=false&get_all=false&project_id={os.getenv('PROJECT_ID', '')}&header_flows=false&page=1&size=1"

headers = {
    "accept": "application/json",
    "x-api-key": f"{os.getenv('LANGFLOW_API_KEY', '')}",
}

response = requests.request("GET", url, headers=headers)
response.raise_for_status()

print(response.text)
```


```js
const url = `${process.env.LANGFLOW_URL ?? ""}/api/v1/flows/?remove_example_flows=true&components_only=false&get_all=false&project_id=${process.env.PROJECT_ID ?? ""}&header_flows=false&page=1&size=1`;

const options = {
  method: 'GET',
  headers: {
    "accept": `application/json`,
    "x-api-key": `${process.env.LANGFLOW_API_KEY ?? ""}`,
  },
};

fetch(url, options)
  .then(async (response) => {
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    const text = await response.text();
    console.log(text);
  })
  .catch((error) => console.error(error));
```


```bash
curl -X GET \
  "$LANGFLOW_URL/api/v1/flows/?remove_example_flows=true&components_only=false&get_all=false&project_id=$PROJECT_ID&header_flows=false&page=1&size=1" \
  -H "accept: application/json" \
  -H "x-api-key: $LANGFLOW_API_KEY"
```


## Read sample flows [​](https://docs.langflow.org/api-flows#read-sample-flows)


Retrieves a list of sample flows:


- Python
- JavaScript
- curl


```python
import os

import requests

url = f"{os.getenv('LANGFLOW_URL', '')}/api/v1/flows/basic_examples/"

headers = {
    "accept": "application/json",
    "x-api-key": f"{os.getenv('LANGFLOW_API_KEY', '')}",
}

response = requests.request("GET", url, headers=headers)
response.raise_for_status()

print(response.text)
```


```js
const url = `${process.env.LANGFLOW_URL ?? ""}/api/v1/flows/basic_examples/`;

const options = {
  method: 'GET',
  headers: {
    "accept": `application/json`,
    "x-api-key": `${process.env.LANGFLOW_API_KEY ?? ""}`,
  },
};

fetch(url, options)
  .then(async (response) => {
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    const text = await response.text();
    console.log(text);
  })
  .catch((error) => console.error(error));
```


```bash
curl -X GET \
  "$LANGFLOW_URL/api/v1/flows/basic_examples/" \
  -H "accept: application/json" \
  -H "x-api-key: $LANGFLOW_API_KEY"
```


## Update flow [​](https://docs.langflow.org/api-flows#update-flow)


Updates an existing flow by its ID.


This example changes the value for `endpoint_name` from a random UUID to `my_new_endpoint_name`.


- Python
- JavaScript
- curl


```python
import os
import uuid

import requests

base = os.environ.get("LANGFLOW_URL") or os.environ.get("LANGFLOW_SERVER_URL", "")
flow_id = os.environ.get("FLOW_ID", "")
api_key = os.environ.get("LANGFLOW_API_KEY", "")

headers = {"accept": "application/json", "Content-Type": "application/json", "x-api-key": api_key}

payload = {
    "name": f"docs-example-updated-flow-{uuid.uuid4().hex[:8]}",
    "description": "Updated via API docs Python example",
    "locked": False,
}

response = requests.patch(f"{base}/api/v1/flows/{flow_id}", headers=headers, json=payload, timeout=30)
response.raise_for_status()
print(response.text)
```


```js
const url = `${process.env.LANGFLOW_URL ?? ""}/api/v1/flows/${process.env.FLOW_ID ?? ""}`;

const options = {
  method: 'PATCH',
  headers: {
    "accept": `application/json`,
    "Content-Type": `application/json`,
    "x-api-key": `${process.env.LANGFLOW_API_KEY ?? ""}`,
  },
  body: JSON.stringify({
  "name": "string",
  "description": "string",
  "data": {},
  "project_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "endpoint_name": "my_new_endpoint_name",
  "locked": true
}),
};

fetch(url, options)
  .then(async (response) => {
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    const text = await response.text();
    console.log(text);
  })
  .catch((error) => console.error(error));
```


```bash
curl -X PATCH \
  "$LANGFLOW_URL/api/v1/flows/$FLOW_ID" \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -H "x-api-key: $LANGFLOW_API_KEY" \
  -d '{
  "name": "string",
  "description": "string",
  "data": {},
  "project_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "endpoint_name": "my_new_endpoint_name",
  "locked": true
}'
```


## Delete flow [​](https://docs.langflow.org/api-flows#delete-flow)


Deletes a specific flow by its ID.


- Python
- JavaScript
- curl


```python
import os

import requests

base = os.environ.get("LANGFLOW_URL", "")
api_key = os.environ.get("LANGFLOW_API_KEY", "")

headers = {"accept": "application/json", "Content-Type": "application/json", "x-api-key": api_key}

create = requests.post(
    f"{base}/api/v1/flows/",
    headers=headers,
    json={
        "name": "docs-example-delete-me",
        "description": "Temporary flow for delete-flow example",
        "data": {"nodes": [], "edges": []},
    },
    timeout=30,
)
create.raise_for_status()
flow_id = create.json()["id"]

delete = requests.delete(f"{base}/api/v1/flows/{flow_id}", headers=headers, timeout=30)
delete.raise_for_status()
print(delete.text)
```


```js
const url = `${process.env.LANGFLOW_URL ?? ""}/api/v1/flows/${process.env.FLOW_ID ?? ""}`;

const options = {
  method: 'DELETE',
  headers: {
    "accept": `application/json`,
    "x-api-key": `${process.env.LANGFLOW_API_KEY ?? ""}`,
  },
};

fetch(url, options)
  .then(async (response) => {
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    const text = await response.text();
    console.log(text);
  })
  .catch((error) => console.error(error));
```


```bash
curl -X DELETE \
  "$LANGFLOW_URL/api/v1/flows/$FLOW_ID" \
  -H "accept: application/json" \
  -H "x-api-key: $LANGFLOW_API_KEY"
```


## Export flows [​](https://docs.langflow.org/api-flows#export-flows)


Exports specified flows to a ZIP file.


This endpoint downloads a ZIP file containing [Langflow JSON files](https://docs.langflow.org/concepts-flows-import#langflow-json-file-contents) for each flow ID listed in the request body.


- Python
- JavaScript
- curl


```python
import os

import requests

base = os.environ.get("LANGFLOW_URL", "")
api_key = os.environ.get("LANGFLOW_API_KEY", "")
flow_id = os.environ.get("FLOW_ID", "")
folder_id = os.environ.get("PROJECT_ID") or os.environ.get("FOLDER_ID", "")

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
    "x-api-key": api_key,
}

# Export needs at least two flows to return a ZIP; a single id returns JSON.
extra = requests.post(
    f"{base}/api/v1/flows/",
    headers=headers,
    json={
        "name": "docs-export-temp-flow",
        "description": "Temporary second flow for export example",
        "data": {"nodes": [], "edges": []},
        **({"folder_id": folder_id} if folder_id else {}),
    },
    timeout=30,
)
extra.raise_for_status()
extra_id = extra.json()["id"]

payload = [flow_id, extra_id]

response = requests.post(f"{base}/api/v1/flows/download/", headers=headers, json=payload, timeout=60)
response.raise_for_status()

with open("langflow-flows.zip", "wb") as f:
    f.write(response.content)
print("Saved response to langflow-flows.zip")

requests.delete(f"{base}/api/v1/flows/{extra_id}", headers=headers, timeout=30)
```


```js
const url = `${process.env.LANGFLOW_URL ?? ""}/api/v1/flows/download/`;

const options = {
  method: 'POST',
  headers: {
    "accept": `application/json`,
    "Content-Type": `application/json`,
    "x-api-key": `${process.env.LANGFLOW_API_KEY ?? ""}`,
  },
  body: JSON.stringify([
  "e1e40c77-0541-41a9-88ab-ddb3419398b5",
  "92f9a4c5-cfc8-4656-ae63-1f0881163c28"
]),
};

fetch(url, options)
  .then(async (response) => {
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    const data = await response.arrayBuffer();
    console.log("Received binary response for langflow-flows.zip", data.byteLength);
  })
  .catch((error) => console.error(error));
```


```bash
curl -X POST \
  "$LANGFLOW_URL/api/v1/flows/download/" \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -H "x-api-key: $LANGFLOW_API_KEY" \
  -d '[
  "e1e40c77-0541-41a9-88ab-ddb3419398b5",
  "92f9a4c5-cfc8-4656-ae63-1f0881163c28"
]' \
  --output langflow-flows.zip
```


## Import flows [​](https://docs.langflow.org/api-flows#import-flows)


Imports flows by uploading a [Langflow-compatible JSON file](https://docs.langflow.org/concepts-flows-import#langflow-json-file-contents).


To specify a target project for the flow, include the query parameter `folder_id`. The target `folder_id` must already exist before uploading a flow. Call the [/api/v1/projects/](https://docs.langflow.org/api-projects#read-projects) endpoint for a list of available folders and projects.


This example uploads a local file named `agent-with-astra-db-tool.json` to a folder specified by a `FOLDER_ID` variable:


- Python
- JavaScript
- curl


```python
import os

import requests

url = f"{os.getenv('LANGFLOW_URL', '')}/api/v1/flows/upload/?folder_id={os.getenv('FOLDER_ID', '')}"

headers = {
    "accept": "application/json",
    "x-api-key": f"{os.getenv('LANGFLOW_API_KEY', '')}",
}

files = {
    "file": open(os.getenv("FLOW_IMPORT_FILE", "docs/docs/API-Reference/fixtures/flow-import.json"), "rb"),
}

response = requests.request("POST", url, headers=headers, files=files)
response.raise_for_status()

print(response.text)

for _f in files.values():
    if hasattr(_f, "close"):
        _f.close()
```


```js
const fs = require("fs");
const path = require("path");

const fixturesDir = path.join(__dirname, "../../fixtures");
const defaultFlowImport = path.join(fixturesDir, "flow-import.json");
const flowImportPath = process.env.FLOW_IMPORT_FILE || defaultFlowImport;
const flowBuf = fs.readFileSync(flowImportPath);
const flowName = path.basename(flowImportPath);

const url = `${process.env.LANGFLOW_URL ?? ""}/api/v1/flows/upload/?folder_id=${process.env.FOLDER_ID ?? ""}`;

const formData = new FormData();
formData.append("file", new Blob([flowBuf], { type: "application/json" }), flowName);

const options = {
  method: "POST",
  headers: {
    accept: "application/json",
    "x-api-key": `${process.env.LANGFLOW_API_KEY ?? ""}`,
  },
  body: formData,
};

fetch(url, options)
  .then(async (response) => {
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    const text = await response.text();
    console.log(text);
  })
  .catch((error) => console.error(error));
```


```bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEFAULT_FLOW_IMPORT_FILE="$SCRIPT_DIR/../../fixtures/flow-import.json"
FLOW_IMPORT_FILE="${FLOW_IMPORT_FILE:-$DEFAULT_FLOW_IMPORT_FILE}"

curl -X POST \
  "$LANGFLOW_URL/api/v1/flows/upload/?folder_id=$FOLDER_ID" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -H "x-api-key: $LANGFLOW_API_KEY" \
  -F "file=@${FLOW_IMPORT_FILE};type=application/json"
```


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)

- [Create flow](https://docs.langflow.org/api-flows#create-flow)
- [Create flows](https://docs.langflow.org/api-flows#create-flows)
- [Read flow](https://docs.langflow.org/api-flows#read-flow)
- [Read flows](https://docs.langflow.org/api-flows#read-flows)
- [Read sample flows](https://docs.langflow.org/api-flows#read-sample-flows)
- [Update flow](https://docs.langflow.org/api-flows#update-flow)
- [Delete flow](https://docs.langflow.org/api-flows#delete-flow)
- [Export flows](https://docs.langflow.org/api-flows#export-flows)
- [Import flows](https://docs.langflow.org/api-flows#import-flows)[Manage Privacy Choices](https://docs.langflow.org/api-flows#)

---

# Global variables | Langflow Documentation

`https://docs.langflow.org/configuration-global-variables`

Copy page ⌥C Version: 1.12.x On this page
## Create a global variable​
## Edit a global variable​
## Delete a global variable​
## Add custom global variables from the environment​
## Store global variables in Kubernetes secrets​
## Disallow global variables from the environment​
## Use environment variables for missing global variables​








Use global variables to store and reuse credentials and generic values across all of your flows. Global variables are typically used by components in flow, and you can use them in any field with the global variable icon.


In contrast, [environment variables](https://docs.langflow.org/environment-variables), like `LANGFLOW_PORT` or `LANGFLOW_LOG_LEVEL`, are generally for broader settings that configure how Langflow runs. However, Langflow can also source global variables from environment variables.


Langflow stores global variables in its internal database, and it encrypts the values using a secret key.


## Create a global variable [​](https://docs.langflow.org/configuration-global-variables#create-a-global-variable)


To create a new global variable, follow these steps.


1. In the Langflow header, click your profile icon, and then select **Settings**.
2. Click **Global Variables**.
3. Click **Add New**.
4. In the **Create Variable** dialog, enter a name for your variable in the **Variable Name** field.
5. Optional: Select a **Type** for your global variable. The available types are **Generic** (default) and **Credential**. Langflow encrypts both **Generic** and **Credential** type global variables. However, **Generic** variables aren't masked in the visual editor, whereas **Credential** variables are masked. **Session ID** fields don't accept **Credential** (masked) variables.
6. Enter the **Value** for your global variable.
7. Optional: Use the **Apply To Fields** menu to select one or more fields that you want Langflow to automatically apply your global variable to. For example, if you select **OpenAI API Key**, Langflow automatically applies the variable to any **OpenAI API Key** field.
8. Click **Save Variable**.


You can now select your global variable from any text input field that displays the **Globe** icon.


## Edit a global variable [​](https://docs.langflow.org/configuration-global-variables#edit-a-global-variable)


1. In the Langflow header, click your profile icon, and then select **Settings**.
2. Click **Global Variables**.
3. Click on the global variable you want to edit.
4. In the **Update Variable** dialog, you can edit the following fields: **Variable Name**, **Value**, and **Apply To Fields**.
5. Click **Update Variable**.


## Delete a global variable [​](https://docs.langflow.org/configuration-global-variables#delete-a-global-variable)


Deleting a global variable permanently deletes the value from the database. Flows that reference the deleted global variable will fail.


1. In the Langflow header, click your profile icon, and then select **Settings**.
2. Click **Global Variables**.
3. Click the checkbox next to the global variable that you want to delete.
4. Click **Delete**.


The global variable is deleted from the database.


## Add custom global variables from the environment [​](https://docs.langflow.org/configuration-global-variables#add-custom-global-variables-from-the-environment)


Langflow can source custom global variables from your runtime environment. For information about how Langflow detects and applies environment variables, see [Langflow environment variables](https://docs.langflow.org/environment-variables).


Langflow automatically generates global variables based on [`constants.py`](https://github.com/langflow-ai/langflow/blob/main/src/lfx/src/lfx/services/settings/constants.py) if it detects any matching environment variables. For example, if you set `OPENAI_API_KEY` in your runtime environment, Langflow automatically generates a global variable using that value.


You can declare additional variables in `LANGFLOW_VARIABLES_TO_GET_FROM_ENVIRONMENT`. For example, `LANGFLOW_VARIABLES_TO_GET_FROM_ENVIRONMENT=WATSONX_PROJECT_ID,WATSONX_API_KEY` creates global variables named `WATSONX_PROJECT_ID` and `WATSONX_API_KEY` in Langflow's database. Then, you can use these variables wherever they are needed in your component settings.


- Local
- Docker


If you installed Langflow locally, set `LANGFLOW_VARIABLES_TO_GET_FROM_ENVIRONMENT` in your Langflow `.env` file:


1. Create or edit your Langflow `.env` file.
2. Add the `LANGFLOW_VARIABLES_TO_GET_FROM_ENVIRONMENT` environment variable as follows: You can specify the variables either as a comma-separated string with no spaces, or as a JSON list: ```text # Option 1: Comma-separated string (no spaces) LANGFLOW_VARIABLES_TO_GET_FROM_ENVIRONMENT=VARIABLE1,VARIABLE2 # Option 2: JSON list format LANGFLOW_VARIABLES_TO_GET_FROM_ENVIRONMENT=["VARIABLE1", "VARIABLE2"] ``` Replace `VARIABLE1,VARIABLE2` with your additional variables that you want Langflow to source from the environment, such as `CUSTOM_API_KEY,INTERNAL_SERVICE_URL` or `["CUSTOM_API_KEY", "INTERNAL_SERVICE_URL"]`.
3. Save and close the file.
4. Start Langflow with the `.env` file: ```bash uv run langflow run --env-file .env ``` Alternatively, you can set environment variables directly in the command line: ```bash VARIABLE1="VALUE1" VARIABLE2="VALUE2" uv run langflow run --env-file .env ``` The command-line variables override matching variables in the `.env` file. Expose your environment variables to Langflow in a manner that best suits your own environment.
5. Confirm that Langflow successfully sourced the global variables from the environment:
  1. In the Langflow header, click your profile icon, and then select **Settings**.
  2. Click **Global Variables**, and then make sure that your environment variables appear in the **Global Variables** list.


If you're using Docker, there are two ways that you can set `LANGFLOW_VARIABLES_TO_GET_FROM_ENVIRONMENT`:


- On the command line: ```bash docker run -it --rm \ -p 7860:7860 \ -e LANGFLOW_VARIABLES_TO_GET_FROM_ENVIRONMENT="VARIABLE1,VARIABLE2" \ -e VARIABLE1="VALUE1" \ -e VARIABLE2="VALUE2" \ langflowai/langflow:latest ```
- In your `.env` file: ```bash docker run -it --rm \ -p 7860:7860 \ --env-file .env \ -e VARIABLE1="VALUE1" \ -e VARIABLE2="VALUE2" \ langflowai/langflow:latest ```


The list in `LANGFLOW_VARIABLES_TO_GET_FROM_ENVIRONMENT` includes only the variable names. You must ensure that these environment variables are defined in your Docker environment, such as with `-e` or otherwise.


After starting Langflow, go to your Langflow **Settings** to confirm that the variables were created.


Only the **Name** and **Value** are taken from the environment. You can edit the variables in your Langflow **Settings** if you want to configure additional options, such as the **Apply To Fields** option.


Global variables sourced from the environment are assigned the **Credential** type, which masks the values in the visual editor. However, Langflow automatically encrypts *all* global variables stored in the database.


## Store global variables in Kubernetes secrets [​](https://docs.langflow.org/configuration-global-variables#kubernetes-secrets)


By default, Langflow stores global variables encrypted in its database at `langflow.db`. When running Langflow in Kubernetes, you can switch to storing global variables in [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/), to keep sensitive credentials out of the Langflow database entirely.


When Kubernetes secrets are enabled, each user's global variables are stored in a dedicated `Opaque` Secret in the `langflow` namespace, named after the user's UUID. Credentials are stored with a `credential_` prefix on the secret key.


### Prerequisites [​](https://docs.langflow.org/configuration-global-variables#prerequisites)


- Langflow running inside a Kubernetes cluster. See [Kubernetes deployment](https://docs.langflow.org/deployment-kubernetes-dev).


### Grant Langflow permission to manage Kubernetes Secrets [​](https://docs.langflow.org/configuration-global-variables#grant-langflow-permission-to-manage-kubernetes-secrets)


1. Create a manifest for the `ServiceAccount`, `Role`, and `RoleBinding` resources, and save it as `langflow-rbac.yaml`: ```yaml apiVersion: v1 kind: ServiceAccount metadata: name: langflow namespace: langflow --- apiVersion: rbac.authorization.k8s.io/v1 kind: Role metadata: name: langflow-secret-manager namespace: langflow rules: - apiGroups: [""] resources: ["secrets"] verbs: ["get", "create", "update", "patch", "delete"] --- apiVersion: rbac.authorization.k8s.io/v1 kind: RoleBinding metadata: name: langflow-secret-manager namespace: langflow subjects: - kind: ServiceAccount name: langflow namespace: langflow roleRef: kind: Role name: langflow-secret-manager apiGroup: rbac.authorization.k8s.io ```
2. Apply the resources to your cluster: ```bash kubectl apply -f langflow-rbac.yaml ```
3. Set `serviceAccountName` and the `LANGFLOW_VARIABLE_STORE` environment variable in your Deployment: ```yaml spec: serviceAccountName: langflow containers: - name: langflow image: langflowai/langflow:latest env: - name: LANGFLOW_VARIABLE_STORE value: "kubernetes" ```
4. To apply the updated Deployment, and then confirm the pod found the service account, run: ```bash kubectl apply -f langflow-deployment.yaml kubectl describe pod -n langflow -l app.kubernetes.io/name=langflow | grep "Service Account" ```
5. Log in to Langflow, navigate to **Settings** > **Global Variables**, and then create a global variable.
6. To confirm that Langflow created a corresponding Kubernetes Secret, run: ```bash kubectl get secrets -n langflow ``` The output should include a Secret named after the user's UUID.
7. Inspect the Secret's keys to confirm your variable was stored, replacing **YOUR_USER_ID** with the user's UUID: ```bash kubectl get secret uuid-YOUR_USER_ID -n langflow -o jsonpath='{.data}' | python3 -m json.tool ``` Credential-type variables appear with a `credential_` prefix. Generic-type variables use the variable name directly as the key.


## Disallow global variables from the environment [​](https://docs.langflow.org/configuration-global-variables#disallow-global-variables-from-the-environment)


If you want to explicitly prevent Langflow from sourcing global variables from the environment, set `LANGFLOW_STORE_ENVIRONMENT_VARIABLES=False` in your `.env` file.


## Use environment variables for missing global variables [​](https://docs.langflow.org/configuration-global-variables#use-environment-variables-for-missing-global-variables)


If you want to automatically set fallback values for your global variables to environment variables, set `LANGFLOW_FALLBACK_TO_ENV_VAR=True` in your `.env` file. When this setting is enabled, if a global variable isn't found, Langflow attempts to use an environment variable with the same name as a backup.


For example, assume you have the following Langflow `.env` configuration, and your flow has a component that expects a `WATSONX_API_KEY` global variable:


```text
LANGFLOW_FALLBACK_TO_ENV_VAR=True
WATSONX_PROJECT_ID=your_project_id
WATSONX_API_KEY=your_api_key
```


When you run the flow, if there is no global variable named `WATSONX_API_KEY`, Langflow looks for an environment variable named `WATSONX_API_KEY`. In this example, Langflow uses the `WATSONX_API_KEY` value from the `.env` to run the flow.


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)

- [Create a global variable](https://docs.langflow.org/configuration-global-variables#create-a-global-variable)
- [Edit a global variable](https://docs.langflow.org/configuration-global-variables#edit-a-global-variable)
- [Delete a global variable](https://docs.langflow.org/configuration-global-variables#delete-a-global-variable)
- [Add custom global variables from the environment](https://docs.langflow.org/configuration-global-variables#add-custom-global-variables-from-the-environment)
- [Store global variables in Kubernetes secrets](https://docs.langflow.org/configuration-global-variables#kubernetes-secrets)
  - [Prerequisites](https://docs.langflow.org/configuration-global-variables#prerequisites)
  - [Grant Langflow permission to manage Kubernetes Secrets](https://docs.langflow.org/configuration-global-variables#grant-langflow-permission-to-manage-kubernetes-secrets)- [Disallow global variables from the environment](https://docs.langflow.org/configuration-global-variables#disallow-global-variables-from-the-environment)
- [Use environment variables for missing global variables](https://docs.langflow.org/configuration-global-variables#use-environment-variables-for-missing-global-variables)[Manage Privacy Choices](https://docs.langflow.org/configuration-global-variables#)

---

# Memory management options | Langflow Documentation

`https://docs.langflow.org/memory`

# Memory management options

Langflow's default storage option is a SQLite database. The default storage path depends on your operating system and installation method:

Copy page ⌥C Version: 1.12.x On this page
## Storage options and paths​
## Langflow database tables​
*For more information, see the database models in the source code.*

## Configure external memory​
## Configure cache memory​
## Store chat memory​
*Chat history and memories are grouped by session ID (session_id).*

## See also​







Langflow provides flexible memory management options for storage and retrieval of data relevant to your flows and your Langflow server. This includes essential Langflow database tables, file management, caching, and chat memory.


## Storage options and paths [​](https://docs.langflow.org/memory#storage-options-and-paths)


Langflow supports both local memory and external memory options.


Langflow's default storage option is a [SQLite](https://www.sqlite.org/) database. The default storage path depends on your operating system and installation method:


- **Langflow Desktop**:
  - **macOS**: `/Users/<username>/.langflow/data/database.db`
  - **Windows**: `C:\Users\<name>\AppData\Roaming\com.LangflowDesktop\data\database.db`- **Langflow OSS**
  - **macOS/Windows/Linux/WSL with `uv pip install`**: `<path_to_venv>/lib/python3.12/site-packages/langflow/langflow.db` (Python version can vary. Database isn't shared between virtual environments because it is tied to the venv path.)
  - **macOS/Windows/Linux/WSL with `git clone`**: `<path_to_clone>/src/backend/base/langflow/langflow.db`


Langflow offers a few alternatives to the default database path:


- **Config directory**: Set `LANGFLOW_SAVE_DB_IN_CONFIG_DIR=True` to store the database in your Langflow config directory as set in [`LANGFLOW_CONFIG_DIR`](https://docs.langflow.org/logging).
- **External PostgreSQL database**: You can use an external PostgreSQL database for all of your Langflow storage. For more information, see [Configure external memory](https://docs.langflow.org/memory#configure-external-memory) External storage can be useful if you want to preserve the data after uninstalling Langflow or to share the same database between multiple virtual environments.
- **Separate chat memory**: You can selectively use external storage for chat memory only, separate from other Langflow storage. For more information, see [Store chat memory](https://docs.langflow.org/memory#store-chat-memory).
- **No database**: To disable all database operations and run a no-op session, set `LANGFLOW_USE_NOOP_DATABASE=True` in your [Langflow environment variables](https://docs.langflow.org/environment-variables). This is useful for testing when you don't want to persist any data.


## Langflow database tables [​](https://docs.langflow.org/memory#langflow-database-tables)


The following tables are stored in Langflow's application database. This list covers the main product tables. On OSS, the default is the SQLite file `langflow.db`. Desktop uses `database.db`. You can also use an [external PostgreSQL database](https://docs.langflow.org/memory#configure-external-memory).


• **ApiKey**: Manages Langflow API authentication keys. Component API keys are stored in the **Variables** table. For more information, see [API keys and authentication](https://docs.langflow.org/api-keys-and-authentication).


• **A2ATask** and **A2ACheckpoint**: Persist Agent-to-Agent (A2A) protocol tasks and human-in-the-loop graph checkpoints so A2A runs survive restarts and can resume across workers.


• **Deployment**: Tracks deployments of Langflow flows to external providers, including the deployment name, provider resource key, and associated project and provider account.


• **DeploymentProviderAccount**: Stores configured connections to external deployment providers, including provider URL, tenant settings, and encrypted credentials.


• **File**: Stores metadata for files uploaded to Langflow's file management system, including file names, paths, sizes, and storage providers. For more information, see [Manage files](https://docs.langflow.org/concepts-file-management).


• **Flow**: Contains flow definitions, including nodes, edges, and components, stored as JSON or database records. For more information, see [Build flows](https://docs.langflow.org/concepts-flows).


• **FlowVersion**: Stores numbered snapshots of flow definitions, enabling version history. Each row captures a complete flow data snapshot linked to a flow and identified by a sequential version number. For more information, see [Save and restore flow versions](https://docs.langflow.org/concepts-flows#save-and-restore-flow-versions).


• **FlowVersionDeploymentAttachment**: Links specific flow versions to provider deployments, tracking which flow version is deployed where and the provider's opaque snapshot identifier for that version.


• **Folder**: Provides a structure for flow storage, including single-user folders and shared folders accessed by multiple users. For more information, see [Manage flows in projects](https://docs.langflow.org/concepts-flows#projects).


• **IngestionRun**: Records knowledge base ingestion run history, including aggregate counters (chunks created, bytes processed, files succeeded/failed/skipped) and per-file outcome details for each ingestion job. For more information, see [Knowledge bases](https://docs.langflow.org/knowledge-base).


• **Job**: Background job queue for asynchronous tasks including flow workflow execution and knowledge base ingestion. Tracks job type (`workflow`, `ingestion`, `evaluation`), status (`queued`, `in_progress`, `completed`, `failed`), timestamps, and per-job progress metadata.


• **KnowledgeBase**: Stores knowledge base configurations, including the embedding model, chunking settings, backend type, status, and cached statistics (chunk count, word count, total size). For more information, see [Knowledge bases](https://docs.langflow.org/knowledge-base).


• **MemoryBase**: Stores memory base configurations for a flow, including display name, linked `kb_name`, embedding model, ingestion threshold, auto-capture, and optional preprocessing settings. Vector-store `backend_type` / `backend_config` are not columns on this table; they live on the linked **KnowledgeBase** row. For more information, see [Manage memory bases](https://docs.langflow.org/memory-bases).


• **MemoryBasePreprocessingOutput**: Captures LLM-distilled preprocessing output before vector-store writes. Each row represents one preprocessing batch and tracks the status (`processed`, `ingested`, or `skipped`) to support resumable two-phase commit (LLM call → knowledge base write).


• **MemoryBaseSession**: Tracks per-session state for each memory base, including the sync cursor position and total count of processed messages.


• **MemoryBaseWorkflowRun**: Records workflow job runs per memory base and session to support threshold-based ingestion, linking each workflow job to its resulting ingestion job.


• **Message**: Stores chat messages and interactions that occur between components. For more information, see [Message objects](https://docs.langflow.org/data-types#message) and [Store chat memory](https://docs.langflow.org/memory#store-chat-memory).


• **MessageIngestionRecord**: Records which messages have been ingested into a memory base and by which job. Serves as a join table between messages and memory bases, ensuring each message is not re-ingested.


• **Trace** and **Span**: Stores traces and spans for flows and components. For more information, see [Traces](https://docs.langflow.org/traces).


• **Transactions**: Records execution history and results of flow runs. This information is used for [logging](https://docs.langflow.org/logging).


• **User**: Stores user account information including credentials, permissions, profiles, and user management settings. For more information, see [API keys and authentication](https://docs.langflow.org/api-keys-and-authentication).


• **Variables**: Stores global encrypted values and credentials. For more information, see [Global variables](https://docs.langflow.org/configuration-global-variables) and [Component API keys](https://docs.langflow.org/api-keys-and-authentication#component-api-keys).


• **VertexBuild**: Tracks the build status of individual nodes within flows. For more information, see [Test flows in the Playground](https://docs.langflow.org/concepts-playground).


Additional tables support authorization, SSO, and governance, including **AuthzRole**, **AuthzRoleAssignment**, **AuthzShare**, **AuthzTeam**, **AuthzAuditLog**, **CasbinRule**, **SSOConfig**, **SSOSettings**, **SSOUserProfile**, **CatalogPolicyRule**, **ModelProviderPolicy**, and policy bundle tables. For more information, see [Authorization](https://docs.langflow.org/authorization) and [External authentication](https://docs.langflow.org/external-authentication).


For more information, see the database models in the [source code](https://github.com/langflow-ai/langflow/tree/main/src/backend/base/langflow/services/database/models).


## Configure external memory [​](https://docs.langflow.org/memory#configure-external-memory)


To replace the default Langflow SQLite database with another database, set the `LANGFLOW_DATABASE_URL` environment variable to your database URL, and then start Langflow with your `.env` file. For more information and examples, see [Configure an external PostgreSQL database](https://docs.langflow.org/configuration-custom-database).


```text
LANGFLOW_DATABASE_URL=postgresql://user:password@localhost:5432/langflow
```


To fine-tune your database connection pool and timeout settings, you can set the following additional environment variables:


- `LANGFLOW_DATABASE_CONNECTION_RETRY`: Whether to retry lost connections to your Langflow database. If `true`, Langflow tries to connect to the database again if the connection fails. Default: `false`.
- `LANGFLOW_DB_CONNECT_TIMEOUT`: The number of seconds to wait before giving up on a lock to be released or establishing a connection to the database. This may be separate from the `pool_timeout` in `LANGFLOW_DB_CONNECTION_SETTINGS`. Default: 30.
- `LANGFLOW_DB_CONNECTION_SETTINGS`: A JSON dictionary containing the following database connection pool settings: For example: ```text LANGFLOW_DB_CONNECTION_SETTINGS='{"pool_size": 20, "max_overflow": 30, "pool_timeout": 30, "pool_pre_ping": true, "pool_recycle": 1800, "echo": false}' ``` Don't use the deprecated environment variables `LANGFLOW_DB_POOL_SIZE` or `LANGFLOW_DB_MAX_OVERFLOW`. Instead, use `pool_size` and `max_overflow` in `LANGFLOW_DB_CONNECTION_SETTINGS`.
  - `pool_size`: The base number of connections to keep open in the connection pool. Default: 20.
  - `max_overflow`: Maximum number of connections that can be created in excess of `pool_size` if needed. Default: 30.
  - `pool_timeout`: Number of seconds to wait for a connection from the pool before timing out. Default: 30.
  - `pool_pre_ping`: If `true`, the pool tests connections for liveness upon each checkout. Default: `true`.
  - `pool_recycle`: Number of seconds after which a connection is automatically recycled. Default: 1800 (30 minutes).
  - `echo`: If `true`, SQL queries are logged for debugging purposes. Default: `false`.- `LANGFLOW_MIGRATION_LOCK_NAMESPACE`: Optional namespace for PostgreSQL advisory locks used during database migrations. If unset, Alembic uses the static lock key `11223344`, which coordinates every Langflow instance on the same PostgreSQL server. If set, Alembic hashes the namespace to derive the lock key. Set this variable to isolate different Langflow deployments that share one PostgreSQL server, and use the same value on every instance in that deployment. This setting only applies when using PostgreSQL as your database backend.


## Configure cache memory [​](https://docs.langflow.org/memory#configure-cache-memory)


The default Langflow caching behavior is an asynchronous, in-memory cache:


```text
LANGFLOW_LANGCHAIN_CACHE=InMemoryCache
LANGFLOW_CACHE_TYPE=async
```


Langflow officially supports only the default asynchronous, in-memory cache, which is suitable for most use cases. Other cache options, such as Redis, are experimental and can change without notice. If you want to use a non-default cache setting, you can use the following environment variables:


| Variable | Type | Default | Description |
| --- | --- | --- | --- |
| `LANGFLOW_​CACHE_​TYPE` | String | `async` | Set the cache type for Langflow's internal caching system. Possible values: `async`, `redis`, `memory`. If you set the type to `redis`, then you must also set the `LANGFLOW_​REDIS_​*` environment variables. The `disk` backend was removed in 1.10 — switch to `async` for in-memory or `redis` for cross-worker. |
| `LANGFLOW_​LANGCHAIN_​CACHE` | String | `InMemoryCache` | Set the cache storage type for the LangChain caching system (a Langflow dependency), either `InMemoryCache` or `SQLiteCache`. |
| `LANGFLOW_​REDIS_​HOST` | String | `localhost` | Redis server hostname if `LANGFLOW_​CACHE_​TYPE=redis`. |
| `LANGFLOW_​REDIS_​PORT` | Integer | `6379` | Redis server port if `LANGFLOW_​CACHE_​TYPE=redis`. |
| `LANGFLOW_​REDIS_​DB` | Integer | `0` | Redis database number if `LANGFLOW_​CACHE_​TYPE=redis`. |
| `LANGFLOW_​REDIS_​CACHE_​EXPIRE` | Integer | `3600` | Cache expiration time in seconds if `LANGFLOW_​CACHE_​TYPE=redis`. |
| `LANGFLOW_​REDIS_​PASSWORD` | String | Not set | Optional password for Redis authentication if `LANGFLOW_​CACHE_​TYPE=redis`. |


## Store chat memory [​](https://docs.langflow.org/memory#store-chat-memory)


Chat-based flows with a **Chat Input** or **Chat Output** component produce chat history that is stored in the Langflow `messages` table. At minimum, this serves as a chat log, but it isn't functionally the same as chat memory that provides historical context to an LLM.


To store and retrieve chat memories in flows, you can use a **Message History** component or the **Agent** component's built-in chat memory.


### Session ID and chat memory [​](https://docs.langflow.org/memory#session-id-and-chat-memory)


Chat history and memories are grouped by [session ID (`session_id`)](https://docs.langflow.org/session-id).


The default session ID is the flow ID, which means that all chat messages for a flow are stored under the same session ID as one large chat session.


For better segregation of chat memory, especially in flows used by multiple users, consider using custom session IDs. For example, if you use user IDs as session IDs, then each user's chat history is stored separately, isolating the context of their chats from other users' chats.


### Chat memory options [​](https://docs.langflow.org/memory#chat-memory-options)


Where and how chat memory is stored depends on the components used in your flow:


- **Agent component**: This component has built-in chat memory that is enabled by default. This memory allows the agent to retrieve and reference messages from previous conversations associated with the same session ID. All messages are stored in [Langflow storage](https://docs.langflow.org/memory#storage-options-and-paths), and the component provides minimal memory configuration options, such as the number of messages to retrieve. The **Agent** component's built-in chat memory is sufficient for most use cases. If you want to use external chat memory storage, retrieve memories outside the context of a chat, or use chat memory with a language model component (not an agent), you must use the **Message History** component (with or without a third-party chat memory component).
- **Message History component**: By default, this component stores and retrieves memories from Langflow storage, unless you attach a third-party chat memory component. It provides a few more options for sorting and filtering memories, although most of these options are also built-in to the **Agent** component as configurable or fixed parameters. You can use the **Message History** component with or without a language model or agent. For example, if you need to retrieve data from memories outside of chat, you can use the **Message History** component to fetch that data directly from your chat memory database without feeding it into a chat.
- **Third-party chat memory components**: Use one of these components only if you need to store or retrieve chat memories from a dedicated external chat memory database. Typically, this is necessary only if you have specific storage needs that aren't met by Langflow storage. For example, if you want to manage chat memory data by directly working with the database, or if you want to use a different database than the default Langflow storage.


For more information and examples, see [**Message History** component](https://docs.langflow.org/message-history) and [Agent memory](https://docs.langflow.org/agents#agent-memory).


## See also [​](https://docs.langflow.org/memory#see-also)


- [Manage memory bases](https://docs.langflow.org/memory-bases)
- [Configure vector database providers](https://docs.langflow.org/knowledge#configure-vector-database-providers)
- [Database migrations](https://docs.langflow.org/database-migrations)
- [Configure an external PostgreSQL database](https://docs.langflow.org/configuration-custom-database)
- [Langflow file management](https://docs.langflow.org/concepts-file-management)
- [Langflow logs](https://docs.langflow.org/logging)
- [Langflow environment variables](https://docs.langflow.org/environment-variables)


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)

- [Storage options and paths](https://docs.langflow.org/memory#storage-options-and-paths)
- [Langflow database tables](https://docs.langflow.org/memory#langflow-database-tables)
- [Configure external memory](https://docs.langflow.org/memory#configure-external-memory)
- [Configure cache memory](https://docs.langflow.org/memory#configure-cache-memory)
- [Store chat memory](https://docs.langflow.org/memory#store-chat-memory)
  - [Session ID and chat memory](https://docs.langflow.org/memory#session-id-and-chat-memory)
  - [Chat memory options](https://docs.langflow.org/memory#chat-memory-options)- [See also](https://docs.langflow.org/memory#see-also)[Manage Privacy Choices](https://docs.langflow.org/memory#)

---

# Logs | Langflow Documentation

`https://docs.langflow.org/logging`

Copy page ⌥C Version: 1.12.x On this page

Langflow produces logs for individual flows and the Langflow application itself using the [structlog](https://www.structlog.org) library for logging.


By default, OSS Langflow writes logs to stdout. To write logs to a file, set `LANGFLOW_LOG_FILE` to the desired path.


## Log storage [​](https://docs.langflow.org/logging#log-storage)


The `LANGFLOW_CONFIG_DIR` environment variable controls where Langflow stores its configuration and data files. The default location depends on your operating system:


- **Langflow Desktop**:
  - **macOS**: `/Users/<username>/Library/Logs/com.LangflowDesktop`
  - **Windows**: `C:\Users\<username>\AppData\Local\com.LangflowDesktop\logs`- **OSS Langflow** (all installation methods, including `uv pip install` and `git clone`):
  - **macOS**: `/Users/<username>/Library/Caches/langflow`
  - **Linux**: `/home/<username>/.cache/langflow`
  - **Windows/WSL**: `C:\Users\<username>\AppData\Local\langflow\langflow\Cache`


To customize log storage locations and behaviors, set the following [Langflow environment variables](https://docs.langflow.org/environment-variables) in your Langflow `.env` file, and then start Langflow with `uv run langflow run --env-file .env`:


| Variable | Format | Default | Description |
| --- | --- | --- | --- |
| `LANGFLOW_​CONFIG_​DIR` | String | Varies | Set the Langflow configuration directory where files and logs are stored. Default path depends on your installation, as described in the preceding list. |
| `LANGFLOW_​ENABLE_​LOG_​RETRIEVAL` | Boolean | `False` | Enables retrieval of logs from your Langflow instance with [Logs endpoints](https://docs.langflow.org/api-logs). |
| `LANGFLOW_​ENVIRONMENT` | String | Not set | Adds an `environment` field to every JSON log record when set (`staging`, `production`, etc.). Omitted otherwise. |
| `LANGFLOW_​LOG_​ENV` | String | `default` | Primary log format controller. `container` or `container_​json`: JSON format via [`JSONRenderer`](https://www.structlog.org/en/stable/api.html#structlog.processors.JSONRenderer). `container_​csv`: Key-value format. `default` or unset: uses `LANGFLOW_​PRETTY_​LOGS` to determine format. See [JSON log format](https://docs.langflow.org/logging#json-log-format). |
| `LANGFLOW_​LOG_​FILE` | String | Not set | Sets the log file storage location. For example, `LANGFLOW_​LOG_​FILE=path/to/logfile.log`. If not set, logs are written to stdout. |
| `LANGFLOW_​LOG_​FORMAT` | String | Not set | Set to `key_​value` for key-value format or `console` for [`ConsoleRenderer`](https://www.structlog.org/en/stable/console-output.html). Only applies when `LANGFLOW_​LOG_​ENV=default` and `LANGFLOW_​PRETTY_​LOGS=true`. |
| `LANGFLOW_​LOG_​LEVEL` | String | `ERROR` | Global log level. One of `DEBUG`, `INFO`, `WARNING`, `ERROR`, or `CRITICAL`. |
| `LANGFLOW_​LOG_​LEVELS` | String | Not set | Per-logger level overrides as `name=LEVEL,name=LEVEL`. Overrides `LANGFLOW_​LOG_​LEVEL` for specific loggers without changing the global default. Malformed entries raise a `UserWarning` at startup. Example: `sqlalchemy.engine=WARNING,httpx=INFO`. |
| `LANGFLOW_​LOG_​REDACT_​KEYS` | String | Not set | Comma-separated extra keys to scrub from JSON log records, on top of the defaults (`password`, `api_​key`, `token`, `authorization`, `cookie`, etc.). |
| `LANGFLOW_​LOG_​RETRIEVER_​BUFFER_​SIZE` | Integer | `10000` | Buffer size for log retrieval when `LANGFLOW_​ENABLE_​LOG_​RETRIEVAL=True`. Must be greater than `0`. |
| `LANGFLOW_​LOG_​ROTATION` | String | `1 day` | Controls log file rotation by time (`1 day`, `12 hours`, `1 week`) or size (`10 MB`, `1 GB`). Set to `None` to disable rotation. |
| `LANGFLOW_​LOG_​TRACE_​LOCALS` | Boolean | `false` | Include frame locals in structured tracebacks. Off by default because locals can leak secrets; enable only for local debugging. |
| `LANGFLOW_​NATIVE_​TRACING` | Boolean | `true` | Enables the tracer to record execution traces in the Langflow database for use in Trace View. Set to `false` to disable. |
| `LANGFLOW_​PRETTY_​LOGS` | Boolean | `True` | Controls output format when `LANGFLOW_​LOG_​ENV=default` or unset. `true`: [`ConsoleRenderer`](https://www.structlog.org/en/stable/console-output.html) (human-readable). `false`: JSON format. |
| `LANGFLOW_​SERVICE_​NAME` | String | `langflow` | Value of the `service` field on every JSON log record. Used as a label by log aggregators. See [Grafana Loki](https://docs.langflow.org/observability-grafana-loki). |
| `LANGFLOW_​VERSION` | String | Not set | Adds a `version` field to every JSON log record when set. Omitted otherwise. |


## View logs in real-time [​](https://docs.langflow.org/logging#view-logs-in-real-time)
## Log storage​
## View logs in real-time​
## Flow and component logs​
## Access Langflow Desktop logs​
## Log format​
## See also​








By default, OSS Langflow writes logs to stdout. To write logs to a file that you can tail, do the following:


1. Set `LANGFLOW_LOG_FILE` to a file path in your `.env` file: ```text LANGFLOW_LOG_FILE=/path/to/langflow.log ```
2. Start Langflow with your `.env` file: ```bash uv run langflow run --env-file .env ```
3. Change to the directory where you set `LANGFLOW_LOG_FILE`: - macOS - Windows ```bash cd /Users/**USERNAME**/Library/Caches/langflow ``` ```cmd cd C:\Users\**USERNAME**\AppData\Local\com.LangflowDesktop\logs ```
4. Tail the log file: - macOS - Windows ```bash tail -f langflow.log ``` ```cmd Get-Content -Wait -Path langflow.log ``` If you don't see new log entries, check that Langflow is running, and perform some actions to generate logs events. You can also check the terminal where you started Langflow to see if logs are being printed there.


## Flow and component logs [​](https://docs.langflow.org/logging#flow-and-component-logs)


After you run a flow, you can inspect the logs for each component and flow run. For example, you can inspect `Message` objects ingested and generated by [Input and Output components](https://docs.langflow.org/chat-input-and-output).


### View flow logs [​](https://docs.langflow.org/logging#view-flow-logs)


In the visual editor, click **Logs** to view logs for the entire flow:


![Logs pane](https://docs.langflow.org/assets/images/logs-cc30f076e63a5e443cf04855559703a3.png)


Then, click the cells in the **inputs** and **outputs** columns to inspect the `Message` objects. For example, the following `Message` data could be the output from a **Chat Input** component:


```text
    "messages": [
    {
        "message": "What's the recommended way to install Docker on Mac M1?",
        "sender": "User",
        "sender_name": "User",
        "session_id": "Session Apr 21, 17:37:04",
        "stream_url": null,
        "component_id": "ChatInput-4WKag",
        "files": [],
        "type": "text"
    }
    ],
```


In the case of Input/Output components, the original input might not be structured as a `Message` object. For example, a language model component can pass a raw text response to a **Chat Output** component that is then transformed into a `Message` object.


You can find `.log` files for flows at your Langflow installation's log storage location. For filepaths, see [Log storage](https://docs.langflow.org/logging#log-storage).


### View chat logs [​](https://docs.langflow.org/logging#view-chat-logs)


In the **Playground**, you can inspect the chat history for each chat session. For more information, see [View chat history](https://docs.langflow.org/concepts-playground#view-chat-history).


### View output from a single component [​](https://docs.langflow.org/logging#view-output-from-a-single-component)


When debugging issues with the format or content of a flow's output, it can help to inspect each component's output to determine where data is being lost or malformed.


To view the output produced by a single component during the most recent run, click **Inspect output** on the component in the visual editor.


## Access Langflow Desktop logs [​](https://docs.langflow.org/logging#desktop-logs)


If you encounter issues with Langflow Desktop, you might need to access startup logs for debugging. Follow the steps for your operating system.


- macOS
- Windows


1. Open Terminal and run: ```bash cd ~/Library/Logs/com.LangflowDesktop ```
2. To open the folder and view the log files, run the command: ```bash open . ```
3. Locate the `langflow.log` file.


1. Open the Command Prompt (CMD), and then run the following command: ```cmd cd %LOCALAPPDATA%\com.LangflowDesktop\cache ```
2. Open the folder and view the log files: ```cmd start . ```
3. Locate the `langflow.log` file.


You can use the log file to investigate the issue on your own, add context to a [GitHub Issue](https://docs.langflow.org/contributing-github-issues), or send it to [support](https://docs.langflow.org/luna-for-langflow) for debugging assistance.


The log file is only created when Langflow Desktop runs. If you don't see a log file, try starting Langflow Desktop first, then check for the log file.


## Log format [​](https://docs.langflow.org/logging#log-format)


By default, structlog uses [`ConsoleRenderer`](https://www.structlog.org/en/stable/api.html#structlog.dev.ConsoleRenderer) to produce human-readable output with the following structure:


For example:


```text
2026-05-17T18:18:29Z [info     ] incoming request    logger=langflow.api.run flow_id=flow-718 user_id=user-4823
```


### JSON log format [​](https://docs.langflow.org/logging#json-log-format)


Set `LANGFLOW_LOG_ENV=container` to switch structlog's terminal processor to [`JSONRenderer`](https://www.structlog.org/en/stable/api.html#structlog.processors.JSONRenderer), so every line written to stdout is a JSON object containing the event message, level, timestamp, logger name, exception structure, and service metadata.


A typical record in JSON mode looks like the following:


```json
{
  "event": "incoming request",
  "level": "info",
  "logger": "langflow.api.run",
  "timestamp": "2026-05-17T18:18:29.100798Z",
  "service": "langflow",
  "version": "1.10.0",
  "environment": "production",
  "user_id": "user-4823",
  "flow_id": "flow-718",
  "authorization": "***",
  "cookie": "***",
  "request_body": {
    "input": "Tell me a joke",
    "api_key": "***",
    "session_id": "Session Apr 21, 17:37:04"
  }
}
```


When a log record includes an exception, the `exception` field contains a structured traceback instead of a plain string:


```json
{
  "event": "flow run failed",
  "level": "error",
  "logger": "langflow.api.run",
  "timestamp": "2026-05-17T18:18:32.412Z",
  "service": "langflow",
  "exception": [
    {
      "exc_type": "ConnectionError",
      "exc_value": "upstream returned 503",
      "frames": [
        {"filename": "/app/.../runner.py", "lineno": 142, "name": "run_flow"}
      ]
    }
  ]
}
```


Frame locals, which are local variables at each stack frame, are intentionally excluded by default because they can contain API keys, request bodies, and environment values. Set `LANGFLOW_LOG_TRACE_LOCALS=true` to include them for local debugging.


#### Stdlib loggers [​](https://docs.langflow.org/logging#stdlib-loggers)


Third-party libraries that use Python's standard logging module (`uvicorn`, `sqlalchemy`, `httpx`, `langchain`, `asyncio`) are routed through the same JSON stream in container mode. Their original logger name is preserved on the `logger` field, so log queries that work for application loggers also work for library output.


#### OpenTelemetry trace correlation [​](https://docs.langflow.org/logging#opentelemetry-trace-correlation)


If `opentelemetry-api` is installed and an active span is present, every log record automatically picks up `trace_id` and `span_id`. OpenTelemetry is not a hard dependency; if it is not installed, the processor is a no-op and nothing else changes.


## See also [​](https://docs.langflow.org/logging#see-also)


- [Grafana Loki](https://docs.langflow.org/observability-grafana-loki)
- [Logs endpoints](https://docs.langflow.org/api-logs)
- [Memory management options](https://docs.langflow.org/memory)
- [Configure an external PostgreSQL database](https://docs.langflow.org/configuration-custom-database)
- [Grafana Loki](https://docs.langflow.org/observability-grafana-loki)


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)

- [Log storage](https://docs.langflow.org/logging#log-storage)
- [View logs in real-time](https://docs.langflow.org/logging#view-logs-in-real-time)
- [Flow and component logs](https://docs.langflow.org/logging#flow-and-component-logs)
  - [View flow logs](https://docs.langflow.org/logging#view-flow-logs)
  - [View chat logs](https://docs.langflow.org/logging#view-chat-logs)
  - [View output from a single component](https://docs.langflow.org/logging#view-output-from-a-single-component)- [Access Langflow Desktop logs](https://docs.langflow.org/logging#desktop-logs)
- [Log format](https://docs.langflow.org/logging#log-format)
  - [JSON log format](https://docs.langflow.org/logging#json-log-format)- [See also](https://docs.langflow.org/logging#see-also)[Manage Privacy Choices](https://docs.langflow.org/logging#)

---

# Use voice mode | Langflow Documentation

`https://docs.langflow.org/concepts-voice-mode`

# Use voice mode
## Prerequisites​
## Test voice mode in the Playground​
## Develop applications with websockets endpoints​
## See also​





Voice mode is deprecated as of Langflow 1.10.

Copy page ⌥C Version: 1.12.x On this page


You can use Langflow's voice mode to interact with your flows verbally through a microphone and speakers.


## Prerequisites [​](https://docs.langflow.org/concepts-voice-mode#prerequisites)


Voice mode requires the following:


- A flow with **Chat Input**, **Language Model**, and **Chat Output** components. If your flow has an **Agent** component, make sure the tools in your flow have accurate names and descriptions to help the agent choose which tools to use. Additionally, be aware that voice mode overrides typed instructions in the **Agent** component's **Agent Instructions** field.
- An [OpenAI](https://platform.openai.com/) account and an OpenAI API key because Langflow uses the OpenAI API to process voice input and generate responses.
- Optional: An [ElevenLabs](https://elevenlabs.io) API key to enable more voice options for the LLM's response.
- A microphone and speakers. A high quality microphone and minimal background noise are recommended for optimal voice comprehension.


## Test voice mode in the Playground [​](https://docs.langflow.org/concepts-voice-mode#test-voice-mode-in-the-playground)


In the **Playground**, click the **Microphone** to enable voice mode and verbally interact with your flows through a microphone and speakers.


The following steps use the **Simple Agent** template to demonstrate how to enable voice mode:


1. Create a flow based on the **Simple Agent** template.
2. Add your **OpenAI API key** credentials to the **Agent** component.
3. Click **Playground**.
4. Click the **Microphone** icon to open the **Voice mode** dialog.
5. Enter your OpenAI API key, and then click **Save**. Langflow saves the key as a [global variable](https://docs.langflow.org/configuration-global-variables).
6. If you are prompted to grant microphone access, you must allow microphone access to use voice mode. If microphone access is blocked, you won't be able to provide verbal input.
7. For **Audio Input**, select the input device to use with voice mode.
8. Optional: Add an ElevenLabs API key to enable more voices for the LLM's response. Langflow saves this key as a global variable.
9. For **Preferred Language**, select the language you want to use for your conversations with the LLM. This option changes both the expected input language and the response language.
10. Speak into your microphone to start the chat. If configured correctly, the waveform registers your input, and then the agent's logic and response are described verbally and in the **Playground**.


## Develop applications with websockets endpoints [​](https://docs.langflow.org/concepts-voice-mode#develop-applications-with-websockets-endpoints)


Langflow exposes an OpenAI Realtime API-compatible websocket endpoint for your flows. You can build applications against this endpoint the same way you would build against [OpenAI Realtime API websockets](https://platform.openai.com/docs/guides/realtime#connect-with-websockets).


The Langflow API's websocket endpoint requires an [OpenAI API key](https://platform.openai.com/docs/overview) for authentication, and supports an optional [ElevenLabs](https://elevenlabs.io) integration with an ElevenLabs API key.


Additionally, the endpoint requires that you provide the flow ID in the endpoint path.


### Speech-to-text audio transcription [​](https://docs.langflow.org/concepts-voice-mode#speech-to-text-audio-transcription)


The `/ws/flow_tts/$FLOW_ID` endpoint converts audio to text using [OpenAI Realtime voice transcription](https://platform.openai.com/docs/guides/realtime-transcription), and then directly invokes the specified flow for each transcript.


This is the mode used in the Langflow **Playground**.


### Session IDs for websockets endpoints [​](https://docs.langflow.org/concepts-voice-mode#session-ids-for-websockets-endpoints)


The endpoint accepts an optional `/$SESSION_ID` path parameter to provide a unique ID for the conversation. If omitted, Langflow uses the flow ID as the [session ID](https://docs.langflow.org/session-id).


However, be aware that voice mode only maintains context within the current conversation instance. When you close the **Playground** or end a chat, verbal chat history is discarded and not available for future chat sessions.


## See also [​](https://docs.langflow.org/concepts-voice-mode#see-also)


- [Test flows in the Playground](https://docs.langflow.org/concepts-playground)
- [Voice mode troubleshooting](https://docs.langflow.org/troubleshoot#voice-mode)


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)

- [Prerequisites](https://docs.langflow.org/concepts-voice-mode#prerequisites)
- [Test voice mode in the Playground](https://docs.langflow.org/concepts-voice-mode#test-voice-mode-in-the-playground)
- [Develop applications with websockets endpoints](https://docs.langflow.org/concepts-voice-mode#develop-applications-with-websockets-endpoints)
  - [Speech-to-text audio transcription](https://docs.langflow.org/concepts-voice-mode#speech-to-text-audio-transcription)
  - [Session IDs for websockets endpoints](https://docs.langflow.org/concepts-voice-mode#session-ids-for-websockets-endpoints)- [See also](https://docs.langflow.org/concepts-voice-mode#see-also)[Manage Privacy Choices](https://docs.langflow.org/concepts-voice-mode#)

---

# Connect to MCP servers from your application | Langflow Documentation

`https://docs.langflow.org/mcp-tutorial`

# Connect to MCP servers from your application
## Prerequisites​
## Create an agent flow​
## Add an MCP Tools component​
## Add a geolocation server​
## Create a Python application that connects to Langflow​
## Next steps​







This tutorial shows you how to connect MCP servers to your applications using Langflow's MCP Tools component.

Copy page ⌥C Version: 1.12.x On this page

This tutorial shows you how to connect MCP servers to your applications using Langflow's [**MCP Tools** component](https://docs.langflow.org/mcp-client).


The [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) helps agents integrate with LLMs through *MCP clients* and *MCP servers*. Specifically, MCP servers host tools that agents (MCP clients) use to complete specialized tasks. MCP servers are connected to MCP clients like Cursor. Then, you interact with the client, and the client uses tools from the connected servers as needed to complete your requests.


You can run Langflow as an MCP client and an MCP server:


- [Use Langflow as an MCP client](https://docs.langflow.org/mcp-client): When run as an MCP client, an **Agent** component in a Langflow flow can use connected components as tools to handle requests. You can use existing components as tools, and you can connect any MCP server to your flow to make that server's tools available to the agent.
- [Use Langflow as an MCP server](https://docs.langflow.org/mcp-server): When run as an MCP server, your flows become tools that can be used by an MCP client, which could be an external client or another Langflow flow.


In this tutorial, you will use the Langflow **MCP Tools** component to connect multiple MCP servers to your flow, and then you'll use a Python application to run your flow and chat with the agent programmatically.


## Prerequisites [​](https://docs.langflow.org/mcp-tutorial#prerequisites)


- [Install and start Langflow](https://docs.langflow.org/get-started-installation)
- Create a [Langflow API key](https://docs.langflow.org/api-keys-and-authentication)
- Create an [OpenAI API key](https://platform.openai.com/api-keys)


This tutorial uses an OpenAI LLM. If you want to use a different provider, you need a valid credential for that provider.


## Create an agent flow [​](https://docs.langflow.org/mcp-tutorial#create-an-agent-flow)


1. In Langflow, click **New Flow**, and then select the **Simple Agent** template.
2. In the **Agent** component, enter your OpenAI API key. If you want to use a different provider or model, edit the **Model Provider**, **Model Name**, and **API Key** fields accordingly.
3. To test the flow, click **Playground**, and then ask the LLM `Is it safe to go hiking in the Adirondacks today?` This query demonstrates how an LLM, by itself, might not have access to information or functions designed to address specialized queries. In this example, the default OpenAI model provides a vague response, although the agent does know the current date by using its internal `get_current_date` function. ```text Today is July 11, 2025. To determine if it's safe to go hiking in the Adirondacks today, you should check the current weather conditions, trail advisories, and any local alerts (such as bear activity or flooding). Would you like a detailed weather forecast or information on trail conditions for the Adirondacks today? ``` To improve the response, you can connect MCP servers to your flow that provide specialized tools for the agent to use when generating responses. In the next part of this tutorial, you'll connect an MCP server that provides the agent with real-time weather information so that it can generate a more specific response.


## Add an MCP Tools component [​](https://docs.langflow.org/mcp-tutorial#add-an-mcp-tools-component)


There are many MCP servers available online that offer different tools for different tasks. To use an MCP server with an MCP client, you have to make the server available to the client. With all MCP clients, there are several ways to do this:


- Install the server locally.
- Use `uvx` or `npx` to fetch and run a server package.
- Call a server running remotely, like those available on Smithery.


This tutorial demonstrates how to install a weather server locally with `uv pip install`, and how to use `npx` to run the geolocation server package. Your particular MCP server's requirements may vary.


In Langflow, you use the **MCP Tools** component to connect a specific MCP server to a flow. You need one **MCP Tools** component for each MCP server that you want your flow to use.


1. For this tutorial, install a [weather MCP server](https://github.com/isdaniel/mcp_weather_server) on your local machine with uv and Python: ```bash uv pip install mcp_weather_server ``` Make sure you install the server in the same Python environment where Langflow is running:
  - Langflow in a virtual environment: Activate the environment before installing the server.
  - Langflow Docker image: Install the server inside the Docker container.
  - Langflow Desktop or system-wide Langflow OSS: Install the server globally or in the same user environment where you run Langflow.2. In your **Simple Agent** flow, remove the **URL** and **Calculator** tools.
3. Open the **MCP** section in the left sidebar, click **Add MCP Server**, and register the weather MCP server.
4. In the **Add MCP Server** pane, provide the server startup command and arguments to connect the weather MCP server to your flow. For this tutorial, use either the **JSON** or **STDIO** option. Langflow runs the command to launch the server when the agent determines that it needs to use a tool provided by that server. Notice that both configurations provide the same information but in different formats. This means that if your MCP server repository only provides a JSON file for the server, you can still use those values with the STDIO option. - JSON - STDIO To provide the MCP server configuration as a JSON object, select **JSON**, and then paste the server configuration into the **JSON** field: ```json { "mcpServers": { "weather": { "command": "python", "args": [ "-m", "mcp_weather_server" ], "disabled": false, "autoApprove": [] } } } ``` To provide the MCP server configuration in a GUI format, select **STDIO**, and then enter the MCP server configuration values into the given fields: - **Name**: `weather` - **Command**: `python` - **Arguments**: - `-m` - `mcp_weather_server`
5. Click **Add Server**, and then wait for the **Actions** list to populate. This means that the MCP server successfully connected.
6. Drag the weather MCP server from the **MCP** sidebar onto the canvas to add the [**MCP Tools**](https://docs.langflow.org/mcp-client) component for that server. With this weather server, the **MCP Tools** component also adds an optional **City** field. For this tutorial, don't enter anything in this field. Instead, you will add a geolocation MCP server in the next step, which the agent will use to detect your location.
7. Click the **MCP Tools** component, enable **Tool Mode** in the [component's header menu](https://docs.langflow.org/concepts-components#component-menus), and then connect the component's **Toolset** port to the **Agent** component's **Tools** port. At this point your flow has four connected components: ![An Agent component connected to an MCP weather server](https://docs.langflow.org/assets/images/tutorial-mcp-weather-2073f7de52c423626a6ba308cd62da90.png)
  - The **Chat Input** component is connected to the **Agent** component's **Input** port. This allows to flow to be triggered by an incoming prompt from a user or application.
  - The **MCP Tools** component with the weather MCP server is connected to the **Agent** component's **Tools** port. The agent may not use this server for every request; the agent only uses this connection if it decides the server can help respond to the prompt.
  - The **Agent** component's **Output** port is connected to the **Chat Output** component, which returns the final response to the user or application.8. To test the weather MCP server, click **Playground**, and then ask the LLM `Is it safe to go hiking in the Adirondacks today?` The **Playground** shows you the agent's logic as it analyzes the request and select tools to use. Ideally, the agent's response will be more specific than the previous response because of the additional context provided by the weather MCP server. For example: ```text The current weather in Lake Placid, a central location in the Adirondacks, is foggy with a temperature of 17.2°C (about 63°F). If you plan to go hiking today, be cautious as fog can reduce visibility on trails and make navigation more difficult. ``` This is a better response, but what makes this MCP server more valuable than just calling a weather API? MCP servers are often customized for specific tasks, such as highly specialized actions or chained tools for complex, multi-step problem solving. Typically, you would have to write a custom script for a specific task, possibly including multiple API calls in a single script, and then you would have to either execute this script outside the context of the agent or provide it to your agent in some way. Instead, the MCP ensures that all MCP servers are added to agents in the same way, without having to know each server's specific endpoint structures or write custom integrations. The MCP is a standardized way to integrate many diverse tools into agentic applications. You don't have to learn a new API or write custom code every time you want to use a new MCP server. Additionally, you can attach many MCP servers to one agent, depending on the problems you want your application to solve. The more servers you add, the more specialized context the agent can use in its responses. In this tutorial, adding the weather MCP server already improved the quality of the LLM's response. In the next section of the tutorial, you will add a `ip_geolocation` MCP server so the agent can detect the user's location if they don't specify a location in their prompt.


## Add a geolocation server [​](https://docs.langflow.org/mcp-tutorial#add-a-geolocation-server)


The [Toolkit MCP server](https://github.com/cyanheads/toolkit-mcp-server) includes multiple MCP tools for network monitoring, including IP geolocation. It isn't extremely precise, but it doesn't require an API key.


Note that this tool returns the IP geolocation of your Langflow server, so if your server is deployed remotely, consider alternative approaches for getting user-specific location data, such as browser geolocation APIs.


This MCP server can be started with one [npx](https://docs.npmjs.com/cli/v8/commands/npx) command, which downloads and runs the [Toolkit MCP server Node registry package](https://www.npmjs.com/package/@cyanheads/toolkit-mcp-server) without installing the package locally.


To add the Toolkit MCP server to your flow, do the following:


1. Open the **MCP** sidebar, click **Add MCP Server**, and register a second server.
2. Select **STDIO**.
3. For **Name**, enter `ip_geolocation`.
4. For **Command**, enter `npx @cyanheads/toolkit-mcp-server`.
5. Click **Add Server**, and then wait for the **Actions** list to populate. This means that the MCP server successfully connected.
6. Drag the **ip_geolocation** MCP server from the **MCP** sidebar to the canvas to add the second **MCP Tools** component.
7. Click the new **MCP Tools** component, enable **Tool Mode** in the [component's header menu](https://docs.langflow.org/concepts-components#component-menus), and then connect the component's **Toolset** port to the **Agent** component's **Tools** port. Your flow now has an additional **MCP Tools** component for a total of five components. ![An Agent component connected to MCP weather and geolocation servers](https://docs.langflow.org/assets/images/tutorial-mcp-geolocation-b8140a46fa3a3ef20ed15dc6cf4a9060.png)


## Create a Python application that connects to Langflow [​](https://docs.langflow.org/mcp-tutorial#create-a-python-application-that-connects-to-langflow)


At this point, you can open the **Playground** and ask about the weather in your current location to test the IP geolocation tool. However, geolocation tools are most useful in applications where you or your users want to ask about the weather from different places around the world.


In the last part of this tutorial, you'll learn how to use the Langflow API to run a flow in a script. This could be part of a larger application, such as a mobile app where users want to know if the weather is good for a particular sport.


When you use the Langflow API to run a flow, you can change some aspects of the flow without changing the code. For example, you can add more MCP servers to your flow in Langflow, and then use the same script to run the flow. You can use the same input or a new input that prompts the agent to use other tools.


1. For this tutorial's Python script, gather the following information:
  - `LANGFLOW_SERVER_ADDRESS`: Your Langflow server's domain. The default value is `127.0.0.1:7860`. You can get this value from the code snippets on your flow's [**API access** pane](https://docs.langflow.org/concepts-publish#api-access).
  - `FLOW_ID`: Your flow's UUID or custom endpoint name. You can get this value from the code snippets on your flow's [**API access** pane](https://docs.langflow.org/concepts-publish#api-access).
  - `LANGFLOW_API_KEY`: A valid [Langflow API key](https://docs.langflow.org/api-keys-and-authentication).2. Copy the following script into a Python file, and then replace the placeholders with the information you gathered in the previous step: ```python import requests import os url = "LANGFLOW_SERVER_ADDRESS/api/v1/run/FLOW_ID" # The complete API endpoint URL for this flow # Request payload configuration payload = { "output_type": "chat", "input_type": "chat", "input_value": "What's the weather like where I am right now?" } # Request headers headers = { "Content-Type": "application/json", "x-api-key": "LANGFLOW_API_KEY" } try: # Send API request response = requests.request("POST", url, json=payload, headers=headers) response.raise_for_status() # Raise exception for bad status codes # Parse and print only the message text data = response.json() message = data["outputs"][0]["outputs"][0]["results"]["message"]["text"] print(message) except requests.exceptions.RequestException as e: print(f"Error making API request: {e}") except ValueError as e: print(f"Error parsing response: {e}") except (KeyError, IndexError) as e: print(f"Error extracting message from response: {e}") ``` Notice that this script uses a different prompt than the previous **Playground** examples. In this script, the `input_value` asks about the weather in the user's current location without providing any hints about the user's location, such as a particular city. Additionally, this script includes parsing code to extract the LLM's reply from the entire Langflow API response. You will want to use similar extraction in your own applications because the Langflow API response includes metadata and other information that isn't relevant to the reply passed to the user.
3. Save and run the script to send the request and test the flow. The agent uses the `ip_geolocation` tool to detect the requester's location, and then it uses the `weather` tool to retrieve weather information for that location. For example: ```text The weather in Waynesboro, Pennsylvania, is currently overcast with a temperature of 23.0°C (about 73.4°F). If you need more details or have any other questions, feel free to ask! ``` Remember, the `ip_geolocation` tool used in this tutorial uses your Langflow server's location, which can be different from your actual location.


## Next steps [​](https://docs.langflow.org/mcp-tutorial#next-steps)


To continue building on the concepts introduced in this tutorial, see the following:


- [Use Langflow as an MCP client](https://docs.langflow.org/mcp-client)
- [Use Langflow Agents](https://docs.langflow.org/agents)
- [Use Langflow as an MCP server](https://docs.langflow.org/mcp-server)
- [Langflow deployment overview](https://docs.langflow.org/deployment-overview)


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)

- [Prerequisites](https://docs.langflow.org/mcp-tutorial#prerequisites)
- [Create an agent flow](https://docs.langflow.org/mcp-tutorial#create-an-agent-flow)
- [Add an MCP Tools component](https://docs.langflow.org/mcp-tutorial#add-an-mcp-tools-component)
- [Add a geolocation server](https://docs.langflow.org/mcp-tutorial#add-a-geolocation-server)
- [Create a Python application that connects to Langflow](https://docs.langflow.org/mcp-tutorial#create-a-python-application-that-connects-to-langflow)
- [Next steps](https://docs.langflow.org/mcp-tutorial#next-steps)[Manage Privacy Choices](https://docs.langflow.org/mcp-tutorial#)

---

# Flow trigger endpoints | Langflow Documentation

`https://docs.langflow.org/api-flows-run`

# Flow trigger endpoints
*To create, read, update, and delete flows, see Flow management endpoints.*

## Run flow​
## Webhook run flow​
*Use the /webhook endpoint to start a flow by sending an HTTP POST request.*

## Deprecated flow trigger endpoints​




Use the /run and /webhook endpoints to run flows.

Copy page ⌥C Version: 1.12.x On this page

Use the `/run` and `/webhook` endpoints to run flows.


To create, read, update, and delete flows, see [Flow management endpoints](https://docs.langflow.org/api-flows).


## Run flow [​](https://docs.langflow.org/api-flows-run#run-flow)


Execute a specified flow by ID or name. Flow IDs can be found on the code snippets on the [**API access** pane](https://docs.langflow.org/concepts-publish#api-access) or in a flow's URL.


The following example runs the **Basic Prompting** template flow with flow parameters passed in the request body. This flow requires a chat input string (`input_value`), and uses default values for all other parameters.


- Python
- JavaScript
- curl


```python
import os

import requests

base = os.environ.get("LANGFLOW_URL") or os.environ.get("LANGFLOW_SERVER_URL", "")
flow_id = os.environ.get("FLOW_ID", "")
api_key = os.environ.get("LANGFLOW_API_KEY", "")

url = f"{base}/api/v1/run/{flow_id}"

headers = {
    "Content-Type": "application/json",
    "x-api-key": api_key,
}

payload = {
    "input_value": "Tell me about something interesting!",
    "session_id": "chat-123",
    "input_type": "chat",
    "output_type": "chat",
    "output_component": "",
}

response = requests.post(url, headers=headers, json=payload, timeout=60)
response.raise_for_status()
print(response.text)
```


```js
const url = `${process.env.LANGFLOW_SERVER_URL ?? ""}/api/v1/run/${process.env.FLOW_ID ?? ""}`;

const options = {
  method: 'POST',
  headers: {
    "Content-Type": `application/json`,
    "x-api-key": `${process.env.LANGFLOW_API_KEY ?? ""}`,
  },
  body: JSON.stringify({
  "input_value": "Tell me about something interesting!",
  "session_id": "chat-123",
  "input_type": "chat",
  "output_type": "chat",
  "output_component": ""
}),
};

fetch(url, options)
  .then(async (response) => {
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    const text = await response.text();
    console.log(text);
  })
  .catch((error) => console.error(error));
```


```bash
curl -X POST \
  "$LANGFLOW_SERVER_URL/api/v1/run/$FLOW_ID" \
  -H "Content-Type: application/json" \
  -H "x-api-key: $LANGFLOW_API_KEY" \
  -d '{
    "input_value": "Tell me about something interesting!",
    "session_id": "chat-123",
    "input_type": "chat",
    "output_type": "chat",
    "output_component": ""
  }'
```


The response from `/v1/run/$FLOW_ID` includes metadata, inputs, and outputs for the run.


If you are parsing the response in an application, you most likely need to extract the relevant content from the response, rather than pass the entire response back to the user. For an example of a script that extracts data from a Langflow API response, see the [Quickstart](https://docs.langflow.org/get-started-quickstart).


### Stream LLM token responses [​](https://docs.langflow.org/api-flows-run#stream-llm-token-responses)


With `/v1/run/$FLOW_ID`, the flow is executed as a batch with optional LLM token response streaming.


To stream LLM token responses, append the `?stream=true` query parameter to the request:


- Python
- JavaScript
- curl


```python
import os

import requests

url = f"{os.getenv('LANGFLOW_SERVER_URL', '')}/api/v1/run/{os.getenv('FLOW_ID', '')}?stream=true"

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
    "x-api-key": f"{os.getenv('LANGFLOW_API_KEY', '')}",
}

payload = {"message": "Tell me something interesting!", "session_id": "chat-123"}

response = requests.request("POST", url, headers=headers, json=payload)
response.raise_for_status()

print(response.text)
```


```js
const url = `${process.env.LANGFLOW_SERVER_URL ?? ""}/api/v1/run/${process.env.FLOW_ID ?? ""}?stream=true`;

const options = {
  method: 'POST',
  headers: {
    "accept": `application/json`,
    "Content-Type": `application/json`,
    "x-api-key": `${process.env.LANGFLOW_API_KEY ?? ""}`,
  },
  body: JSON.stringify({
  "message": "Tell me something interesting!",
  "session_id": "chat-123"
}),
};

fetch(url, options)
  .then(async (response) => {
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    const text = await response.text();
    console.log(text);
  })
  .catch((error) => console.error(error));
```


```bash
curl -X POST \
  "$LANGFLOW_SERVER_URL/api/v1/run/$FLOW_ID?stream=true" \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -H "x-api-key: $LANGFLOW_API_KEY" \
  -d '{
    "message": "Tell me something interesting!",
    "session_id": "chat-123"
  }'
```


LLM chat responses are streamed back as `token` events, culminating in a final `end` event that closes the connection.


### Run endpoint headers [​](https://docs.langflow.org/api-flows-run#run-endpoint-headers)


| Header | Info | Example |
| --- | --- | --- |
| Content-Type | Required. Specifies the JSON format. | "application/json" |
| accept | Optional. Specifies the response format. Defaults to JSON if not specified. | "application/json" |
| x-api-key | Required. Your Langflow API key for authentication. Can be passed as a header or query parameter. | "sk-..." |
| `X-LANGFLOW-GLOBAL-VAR-*` | Optional. Pass global variables to the flow. Variable names are automatically converted to uppercase. These variables take precedence over OS environment variables and are only available during this specific request execution. | `"X-LANGFLOW-GLOBAL-VAR-API_​KEY: sk-..."` |


### Run endpoint parameters [​](https://docs.langflow.org/api-flows-run#run-endpoint-parameters)


| Parameter | Type | Info |
| --- | --- | --- |
| flow_id | UUID/string | Required. Part of URL: `/run/$FLOW_​ID` |
| stream | Boolean | Optional. Query parameter: `/run/$FLOW_​ID?stream=true` |
| input_value | string | Optional. JSON body field. Main input text/prompt. Default: `null` |
| input_type | string | Optional. JSON body field. Input type ("chat" or "text"). Default: `"chat"` |
| output_type | string | Optional. JSON body field. Output type ("chat", "any", "debug"). Default: `"chat"` |
| output_component | string | Optional. JSON body field. Target component for output. Default: `""` |
| tweaks | object | Optional. JSON body field. Component adjustments. Default: `null`. Refused keys return `422` with `TWEAKS_​REFUSED`. For more information, see [Refused tweaks](https://docs.langflow.org/deployment-tweaks-policy#tweaks-refused). |
| session_id | string | Optional. JSON body field. Conversation context ID. See [Session ID](https://docs.langflow.org/session-id). Default: `null` |


### Request example with all headers and parameters [​](https://docs.langflow.org/api-flows-run#request-example-with-all-headers-and-parameters)


- Python
- JavaScript
- curl


```python
import os

import requests

base = os.environ.get("LANGFLOW_URL") or os.environ.get("LANGFLOW_SERVER_URL", "")
flow_id = os.environ.get("FLOW_ID", "")
api_key = os.environ.get("LANGFLOW_API_KEY", "")

headers = {
    "Content-Type": "application/json",
    "accept": "application/json",
    "x-api-key": api_key,
}

payload = {
    "input_value": "Tell me a story",
    "input_type": "chat",
    "output_type": "chat",
    "output_component": "chat_output",
    "session_id": "chat-123",
}

response = requests.post(
    f"{base}/api/v1/run/{flow_id}?stream=false",
    headers=headers,
    json=payload,
    timeout=60,
)
response.raise_for_status()
print(response.text)
```


```js
const url = `${process.env.LANGFLOW_SERVER_URL ?? ""}/api/v1/run/${process.env.FLOW_ID ?? ""}?stream=true`;

const options = {
  method: 'POST',
  headers: {
    "Content-Type": `application/json`,
    "accept": `application/json`,
    "x-api-key": `${process.env.LANGFLOW_API_KEY ?? ""}`,
  },
  body: JSON.stringify({
  "input_value": "Tell me a story",
  "input_type": "chat",
  "output_type": "chat",
  "output_component": "chat_output",
  "session_id": "chat-123",
  "tweaks": {
    "component_id": {
      "parameter_name": "value"
    }
  }
}),
};

fetch(url, options)
  .then(async (response) => {
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    const text = await response.text();
    console.log(text);
  })
  .catch((error) => console.error(error));
```


```bash
curl -X POST \
  "$LANGFLOW_SERVER_URL/api/v1/run/$FLOW_ID?stream=true" \
  -H "Content-Type: application/json" \
  -H "accept: application/json" \
  -H "x-api-key: $LANGFLOW_API_KEY" \
  -d '{
    "input_value": "Tell me a story",
    "input_type": "chat",
    "output_type": "chat",
    "output_component": "chat_output",
    "session_id": "chat-123",
    "tweaks": {
      "component_id": {
        "parameter_name": "value"
      }
    }
  }'
```


### Pass global variables in request headers [​](https://docs.langflow.org/api-flows-run#pass-global-variables-in-headers)


You can pass global variables to your flow using HTTP headers with the format `X-LANGFLOW-GLOBAL-VAR-{VARIABLE_NAME}`.


Variables passed in headers take precedence over OS environment variables. If a variable is provided in both a header and an environment variable, the header value is used. Variables are only available during this specific request execution and aren't persisted.


Variable names are automatically converted to uppercase. For example, `X-LANGFLOW-GLOBAL-VAR-api-key` becomes `API_KEY` in your flow.


You don't need to create these variables in Langflow's Global Variables section first. Pass any variable name using this header format.


- Python
- JavaScript
- curl


```python
import os

import requests

base = os.environ.get("LANGFLOW_URL") or os.environ.get("LANGFLOW_SERVER_URL", "")
flow_id = os.environ.get("FLOW_ID", "")
api_key = os.environ.get("LANGFLOW_API_KEY", "")

headers = {
    "Content-Type": "application/json",
    "x-api-key": api_key,
    "X-LANGFLOW-GLOBAL-VAR-USER_ID": "user123",
    "X-LANGFLOW-GLOBAL-VAR-ENVIRONMENT": "production",
}

payload = {
    "input_value": "Tell me about something interesting!",
    "input_type": "chat",
    "output_type": "chat",
}

response = requests.post(f"{base}/api/v1/run/{flow_id}", headers=headers, json=payload, timeout=60)
response.raise_for_status()
print(response.text)
```


```js
const url = `${process.env.LANGFLOW_SERVER_URL ?? ""}/api/v1/run/${process.env.FLOW_ID ?? ""}`;

const options = {
  method: 'POST',
  headers: {
    "Content-Type": `application/json`,
    "x-api-key": `${process.env.LANGFLOW_API_KEY ?? ""}`,
    "X-LANGFLOW-GLOBAL-VAR-OPENAI_API_KEY": `sk-...`,
    "X-LANGFLOW-GLOBAL-VAR-USER_ID": `user123`,
    "X-LANGFLOW-GLOBAL-VAR-ENVIRONMENT": `production`,
  },
  body: JSON.stringify({
  "input_value": "Tell me about something interesting!",
  "input_type": "chat",
  "output_type": "chat"
}),
};

fetch(url, options)
  .then(async (response) => {
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    const text = await response.text();
    console.log(text);
  })
  .catch((error) => console.error(error));
```


```bash
curl -X POST \
  "$LANGFLOW_SERVER_URL/api/v1/run/$FLOW_ID" \
  -H "Content-Type: application/json" \
  -H "x-api-key: $LANGFLOW_API_KEY" \
  -H "X-LANGFLOW-GLOBAL-VAR-OPENAI_API_KEY: sk-..." \
  -H "X-LANGFLOW-GLOBAL-VAR-USER_ID: user123" \
  -H "X-LANGFLOW-GLOBAL-VAR-ENVIRONMENT: production" \
  -d '{
    "input_value": "Tell me about something interesting!",
    "input_type": "chat",
    "output_type": "chat"
  }'
```


If your flow components reference variables that aren't provided in headers or your Langflow database, the flow fails by default. To avoid this, you can set `LANGFLOW_FALLBACK_TO_ENV_VAR=True` in your `.env` file, which allows the flow to use values from OS environment variables if they aren't otherwise specified.


## Webhook run flow [​](https://docs.langflow.org/api-flows-run#webhook-run-flow)


Use the `/webhook` endpoint to start a flow by sending an HTTP `POST` request.


- Python
- JavaScript
- curl


```python
import os

import requests

base = os.environ.get("LANGFLOW_URL") or os.environ.get("LANGFLOW_SERVER_URL", "")
flow_id = os.environ.get("FLOW_ID", "")
api_key = os.environ.get("LANGFLOW_API_KEY", "")

headers = {
    "Content-Type": "application/json",
    "x-api-key": api_key,
}

payload = {"data": "example-data"}

response = requests.post(
    f"{base}/api/v1/webhook/{flow_id}",
    headers=headers,
    json=payload,
    timeout=60,
)
response.raise_for_status()
print(response.text)
```


```js
const url = `${process.env.LANGFLOW_SERVER_URL ?? ""}/api/v1/webhook/${process.env.FLOW_ID ?? ""}`;

const options = {
  method: 'POST',
  headers: {
    "Content-Type": `application/json`,
    "x-api-key": `${process.env.LANGFLOW_API_KEY ?? ""}`,
  },
  body: JSON.stringify({
  "data": "example-data"
}),
};

fetch(url, options)
  .then(async (response) => {
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    const text = await response.text();
    console.log(text);
  })
  .catch((error) => console.error(error));
```


```bash
curl -X POST \
  "$LANGFLOW_SERVER_URL/api/v1/webhook/$FLOW_ID" \
  -H "Content-Type: application/json" \
  -H "x-api-key: $LANGFLOW_API_KEY" \
  -d '{"data": "example-data"}'
```


## Deprecated flow trigger endpoints [​](https://docs.langflow.org/api-flows-run#deprecated-flow-trigger-endpoints)


The following endpoints are deprecated and replaced by the `/run` endpoint:


- `/process`
- `/predict`


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)

- [Run flow](https://docs.langflow.org/api-flows-run#run-flow)
  - [Stream LLM token responses](https://docs.langflow.org/api-flows-run#stream-llm-token-responses)
  - [Run endpoint headers](https://docs.langflow.org/api-flows-run#run-endpoint-headers)
  - [Run endpoint parameters](https://docs.langflow.org/api-flows-run#run-endpoint-parameters)
  - [Request example with all headers and parameters](https://docs.langflow.org/api-flows-run#request-example-with-all-headers-and-parameters)
  - [Pass global variables in request headers](https://docs.langflow.org/api-flows-run#pass-global-variables-in-headers)- [Webhook run flow](https://docs.langflow.org/api-flows-run#webhook-run-flow)
- [Deprecated flow trigger endpoints](https://docs.langflow.org/api-flows-run#deprecated-flow-trigger-endpoints)[Manage Privacy Choices](https://docs.langflow.org/api-flows-run#)

---

# Human Input | Langflow Documentation

`https://docs.langflow.org/human-input`

Copy page ⌥C Version: 1.12.x On this page

The **Human Input** component pauses a flow so a human can review content and choose an action. Each configured **User Action** becomes a branch output. After the human makes a decision, the flow continues only on the selected branch.


## Use the Human Input component in a flow [​](https://docs.langflow.org/human-input#use-the-human-input-component-in-a-flow)


This example gates a flow with **Approve** and **Reject** branches:


1. Add a **Human Input** component from **Flow Controls**.
2. In **Form Content**, enter text for the human reviewer, such as `Review this summary before it is sent to the customer.`
3. In **User Actions**, keep the default values **Approve** and **Reject**. Optionally, add a custom label, such as **Escalate**. Each action adds a matching output handle to the component.
4. Connect the **Approve** output to the components to run when the request is approved.
5. Connect the **Reject** output to an alternate path, such as a [**Chat Output** component](https://docs.langflow.org/chat-input-and-output) that explains the rejection.
6. Run the flow in the **Playground**. When execution reaches the **Human Input** node, select an action in the approval pane to resume the flow.


### Configure timeouts and fallback [​](https://docs.langflow.org/human-input#configure-timeouts-and-fallback)


Enable fallback to create a new output handle from the component. If no decision arrives before the configured timeout, Langflow routes to this **Fallback** output.
## Use the Human Input component in a flow​
## Human Input parameters​
## Use HITL in a flow​
*For a video example, see the Langflow 1.11 release blog.*

## See also​






To handle unanswered requests, do the following:


1. In the [component inspection panel](https://docs.langflow.org/concepts-components#component-menus), select **Enable Fallback**.
2. Set the **Timeout** time.
3. Connect the **Fallback** output to the logic that should run when the timeout expires.


## Human Input parameters [​](https://docs.langflow.org/human-input#human-input-parameters)


| Name | Display name | Description |
| --- | --- | --- |
| `prompt` | Form Content | Content shown to the human for review. |
| `decisions` | User Actions | Actions the human can select. Each action becomes a component branch output. |
| `timeout` | Timeout | When **Enable Fallback** is on, how long to wait for a response before taking the fallback path. |
| `enable_​fallback` | Enable Fallback | When enabled, adds a **Fallback** output used when no user action is answered within the timeout. |


Some parameters are hidden by default in the visual editor. You can modify all component parameters through the [component inspection panel](https://docs.langflow.org/concepts-components#component-inspection-panel) that appears when you select a component.


## Use HITL in a flow [​](https://docs.langflow.org/human-input#use-hitl-in-a-flow)


For a video example, see the [Langflow 1.11 release blog](https://www.langflow.org/blog/langflow-1-11).


## See also [​](https://docs.langflow.org/human-input#see-also)


- [Human-in-the-Loop](https://docs.langflow.org/human-in-the-loop)
- [If-Else](https://docs.langflow.org/if-else)
- [Workflow API (Beta)](https://docs.langflow.org/workflow-api)


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)

- [Use the Human Input component in a flow](https://docs.langflow.org/human-input#use-the-human-input-component-in-a-flow)
  - [Configure timeouts and fallback](https://docs.langflow.org/human-input#configure-timeouts-and-fallback)- [Human Input parameters](https://docs.langflow.org/human-input#human-input-parameters)
- [Use HITL in a flow](https://docs.langflow.org/human-input#use-hitl-in-a-flow)
- [See also](https://docs.langflow.org/human-input#see-also)[Manage Privacy Choices](https://docs.langflow.org/human-input#)

---

# Monitor endpoints | Langflow Documentation

`https://docs.langflow.org/api-monitor`

# Monitor endpoints
## Vertex builds​
## Messages endpoints​
## Get traces​
*Use GET /monitor/traces and filter by flow_id:*

## Get transactions​
## See also​






The /monitor endpoints are for internal Langflow functionality, primarily related to running flows in the Playground, storing chat history, and generating flow logs.

Copy page ⌥C Version: 1.12.x On this page

The `/monitor` endpoints are for internal Langflow functionality, primarily related to running flows in the **Playground**, storing chat history, and generating flow logs.


This information is primarily for those who are building custom components or contributing to the Langflow codebase in a way that requires calling or understanding these endpoints.


For typical application development with Langflow, there are more appropriate options for monitoring, debugging, and memory management. For more information, see the following:


- [Logs](https://docs.langflow.org/logging): Langflow log storage locations, customization options, and where to view logs in the visual editor
- [Test flows in the Playground](https://docs.langflow.org/concepts-playground): Run flows and inspect message history
- [Memory management options](https://docs.langflow.org/memory): Langflow storage locations and options, including the database, cache, and chat history


## Vertex builds [​](https://docs.langflow.org/api-monitor#vertex-builds)


The Vertex build endpoints (`/monitor/builds`) are exclusively for **Playground** functionality.


When you run a flow in the **Playground**, Langflow calls the `/build/$FLOW_ID/flow` endpoint in [chat.py](https://github.com/langflow-ai/langflow/blob/main/src/backend/base/langflow/api/v1/chat.py#L130). This call retrieves the flow data, builds a graph, and executes the graph. As each component (or node) is executed, the `build_vertex` function calls `build_and_run`, which may call the individual components' `def_build` method, if it exists. If a component doesn't have a `def_build` function, the build still returns a component.


The `build` function allows components to execute logic at runtime. For example, the [**Recursive Character Text Splitter** component](https://github.com/langflow-ai/langflow/blob/main/src/lfx/src/lfx/components/langchain_utilities/recursive_character.py) is a child of the `LCTextSplitterComponent` class. When text needs to be processed, the parent class's `build` method is called, which creates a `RecursiveCharacterTextSplitter` object and uses it to split the text according to the defined parameters. The split text is then passed on to the next component. This all occurs when the component is built.


### Get Vertex builds [​](https://docs.langflow.org/api-monitor#get-vertex-builds)


Retrieve Vertex builds for a specific flow.


- Python
- JavaScript
- curl


```python
import os

import requests

url = f"{os.getenv('LANGFLOW_URL', '')}/api/v1/monitor/builds?flow_id={os.getenv('FLOW_ID', '')}"

headers = {
    "accept": "application/json",
    "x-api-key": f"{os.getenv('LANGFLOW_API_KEY', '')}",
}

response = requests.request("GET", url, headers=headers)
response.raise_for_status()

print(response.text)
```


```js
const url = `${process.env.LANGFLOW_URL ?? ""}/api/v1/monitor/builds?flow_id=${process.env.FLOW_ID ?? ""}`;

const options = {
  method: 'GET',
  headers: {
    "accept": `application/json`,
    "x-api-key": `${process.env.LANGFLOW_API_KEY ?? ""}`,
  },
};

fetch(url, options)
  .then(async (response) => {
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    const text = await response.text();
    console.log(text);
  })
  .catch((error) => console.error(error));
```


```bash
curl -X GET \
  "$LANGFLOW_URL/api/v1/monitor/builds?flow_id=$FLOW_ID" \
  -H "accept: application/json" \
  -H "x-api-key: $LANGFLOW_API_KEY"
```


Result

```json
{
  "vertex_builds": {
    "ChatInput-NCmix": [
      {
        "data": {
          "results": {
            "message": {
              "text_key": "text",
              "data": {
                "timestamp": "2024-12-23 19:10:57",
                "sender": "User",
                "sender_name": "User",
                "session_id": "01ce083d-748b-4b8d-97b6-33adbb6a528a",
                "text": "Hello",
                "files": [],
                "error": "False",
                "edit": "False",
                "properties": {
                  "text_color": "",
                  "background_color": "",
                  "edited": "False",
                  "source": {
                    "id": "None",
                    "display_name": "None",
                    "source": "None"
                  },
                  "icon": "",
                  "allow_markdown": "False",
                  "positive_feedback": "None",
                  "state": "complete",
                  "targets": []
                },
                "category": "message",
                "content_blocks": [],
                "id": "c95bed34-f906-4aa6-84e4-68553f6db772",
                "flow_id": "01ce083d-748b-4b8d-97b6-33adbb6a528a"
              },
              "default_value": "",
              "text": "Hello",
              "sender": "User",
              "sender_name": "User",
              "files": [],
              "session_id": "01ce083d-748b-4b8d-97b6-33adbb6a528a",
              "timestamp": "2024-12-23 19:10:57+00:00",
              "flow_id": "01ce083d-748b-4b8d-97b6-33adbb6a528a",
              "error": "False",
              "edit": "False",
              "properties": {
                "text_color": "",
                "background_color": "",
                "edited": "False",
                "source": {
                  "id": "None",
                  "display_name": "None",
                  "source": "None"
                },
                "icon": "",
                "allow_markdown": "False",
                "positive_feedback": "None",
                "state": "complete",
                "targets": []
              },
              "category": "message",
              "content_blocks": []
            }
          },
          "outputs": {
            "message": {
              "message": {
                "timestamp": "2024-12-23T19:10:57",
                "sender": "User",
                "sender_name": "User",
                "session_id": "01ce083d-748b-4b8d-97b6-33adbb6a528a",
                "text": "Hello",
                "files": [],
                "error": false,
                "edit": false,
                "properties": {
                  "text_color": "",
                  "background_color": "",
                  "edited": false,
                  "source": {
                    "id": null,
                    "display_name": null,
                    "source": null
                  },
                  "icon": "",
                  "allow_markdown": false,
                  "positive_feedback": null,
                  "state": "complete",
                  "targets": []
                },
                "category": "message",
                "content_blocks": [],
                "id": "c95bed34-f906-4aa6-84e4-68553f6db772",
                "flow_id": "01ce083d-748b-4b8d-97b6-33adbb6a528a"
              },
              "type": "object"
            }
          },
          "logs": { "message": [] },
          "message": {
            "message": "Hello",
            "sender": "User",
            "sender_name": "User",
            "files": [],
            "type": "object"
          },
          "artifacts": {
            "message": "Hello",
            "sender": "User",
            "sender_name": "User",
            "files": [],
            "type": "object"
          },
          "timedelta": 0.015060124918818474,
          "duration": "15 ms",
          "used_frozen_result": false
        },
        "artifacts": {
          "message": "Hello",
          "sender": "User",
          "sender_name": "User",
          "files": [],
          "type": "object"
        },
        "params": "- Files: []\n  Message: Hello\n  Sender: User\n  Sender Name: User\n  Type: object\n",
        "valid": true,
        "build_id": "40aa200e-74db-4651-b698-f80301d2b26b",
        "id": "ChatInput-NCmix",
        "timestamp": "2024-12-23T19:10:58.772766Z",
        "flow_id": "01ce083d-748b-4b8d-97b6-33adbb6a528a"
      }
    ],
    "Prompt-BEn9c": [
      {
        "data": {
          "results": {},
          "outputs": {
            "prompt": {
              "message": "Answer the user as if you were a GenAI expert, enthusiastic about helping them get started building something fresh.",
              "type": "text"
            }
          },
          "logs": { "prompt": [] },
          "message": {
            "prompt": {
              "repr": "Answer the user as if you were a GenAI expert, enthusiastic about helping them get started building something fresh.",
              "raw": "Answer the user as if you were a GenAI expert, enthusiastic about helping them get started building something fresh.",
              "type": "text"
            }
          },
          "artifacts": {
            "prompt": {
              "repr": "Answer the user as if you were a GenAI expert, enthusiastic about helping them get started building something fresh.",
              "raw": "Answer the user as if you were a GenAI expert, enthusiastic about helping them get started building something fresh.",
              "type": "text"
            }
          },
          "timedelta": 0.0057758750626817346,
          "duration": "6 ms",
          "used_frozen_result": false
        },
        "artifacts": {
          "prompt": {
            "repr": "Answer the user as if you were a GenAI expert, enthusiastic about helping them get started building something fresh.",
            "raw": "Answer the user as if you were a GenAI expert, enthusiastic about helping them get started building something fresh.",
            "type": "text"
          }
        },
        "params": "None",
        "valid": true,
        "build_id": "39bbbfde-97fd-42a5-a9ed-d42a5c5d532b",
        "id": "Prompt-BEn9c",
        "timestamp": "2024-12-23T19:10:58.781019Z",
        "flow_id": "01ce083d-748b-4b8d-97b6-33adbb6a528a"
      }
    ],
    "OpenAIModel-7AjrN": [
      {
        "data": {
          "results": {},
          "outputs": {
            "text_output": {
              "message": "Hello! 🌟 I'm excited to help you get started on your journey to building something fresh! What do you have in mind? Whether it's a project, an idea, or a concept, let's dive in and make it happen!",
              "type": "text"
            },
            "model_output": { "message": "", "type": "unknown" }
          },
          "logs": { "text_output": [] },
          "message": {
            "text_output": {
              "repr": "Hello! 🌟 I'm excited to help you get started on your journey to building something fresh! What do you have in mind? Whether it's a project, an idea, or a concept, let's dive in and make it happen!",
              "raw": "Hello! 🌟 I'm excited to help you get started on your journey to building something fresh! What do you have in mind? Whether it's a project, an idea, or a concept, let's dive in and make it happen!",
              "type": "text"
            }
          },
          "artifacts": {
            "text_output": {
              "repr": "Hello! 🌟 I'm excited to help you get started on your journey to building something fresh! What do you have in mind? Whether it's a project, an idea, or a concept, let's dive in and make it happen!",
              "raw": "Hello! 🌟 I'm excited to help you get started on your journey to building something fresh! What do you have in mind? Whether it's a project, an idea, or a concept, let's dive in and make it happen!",
              "type": "text"
            }
          },
          "timedelta": 1.034765167045407,
          "duration": "1.03 seconds",
          "used_frozen_result": false
        },
        "artifacts": {
          "text_output": {
            "repr": "Hello! 🌟 I'm excited to help you get started on your journey to building something fresh! What do you have in mind? Whether it's a project, an idea, or a concept, let's dive in and make it happen!",
            "raw": "Hello! 🌟 I'm excited to help you get started on your journey to building something fresh! What do you have in mind? Whether it's a project, an idea, or a concept, let's dive in and make it happen!",
            "type": "text"
          }
        },
        "params": "None",
        "valid": true,
        "build_id": "4f0ae730-a266-4d35-b89f-7b825c620a0f",
        "id": "OpenAIModel-7AjrN",
        "timestamp": "2024-12-23T19:10:58.790484Z",
        "flow_id": "01ce083d-748b-4b8d-97b6-33adbb6a528a"
      }
    ],
    "ChatOutput-sfUhT": [
      {
        "data": {
          "results": {
            "message": {
              "text_key": "text",
              "data": {
                "timestamp": "2024-12-23 19:10:58",
                "sender": "Machine",
                "sender_name": "AI",
                "session_id": "01ce083d-748b-4b8d-97b6-33adbb6a528a",
                "text": "Hello! 🌟 I'm excited to help you get started on your journey to building something fresh! What do you have in mind? Whether it's a project, an idea, or a concept, let's dive in and make it happen!",
                "files": [],
                "error": "False",
                "edit": "False",
                "properties": {
                  "text_color": "",
                  "background_color": "",
                  "edited": "False",
                  "source": {
                    "id": "OpenAIModel-7AjrN",
                    "display_name": "OpenAI",
                    "source": "gpt-4o-mini"
                  },
                  "icon": "OpenAI",
                  "allow_markdown": "False",
                  "positive_feedback": "None",
                  "state": "complete",
                  "targets": []
                },
                "category": "message",
                "content_blocks": [],
                "id": "5688356d-9f30-40ca-9907-79a7a2fc16fd",
                "flow_id": "01ce083d-748b-4b8d-97b6-33adbb6a528a"
              },
              "default_value": "",
              "text": "Hello! 🌟 I'm excited to help you get started on your journey to building something fresh! What do you have in mind? Whether it's a project, an idea, or a concept, let's dive in and make it happen!",
              "sender": "Machine",
              "sender_name": "AI",
              "files": [],
              "session_id": "01ce083d-748b-4b8d-97b6-33adbb6a528a",
              "timestamp": "2024-12-23 19:10:58+00:00",
              "flow_id": "01ce083d-748b-4b8d-97b6-33adbb6a528a",
              "error": "False",
              "edit": "False",
              "properties": {
                "text_color": "",
                "background_color": "",
                "edited": "False",
                "source": {
                  "id": "OpenAIModel-7AjrN",
                  "display_name": "OpenAI",
                  "source": "gpt-4o-mini"
                },
                "icon": "OpenAI",
                "allow_markdown": "False",
                "positive_feedback": "None",
                "state": "complete",
                "targets": []
              },
              "category": "message",
              "content_blocks": []
            }
          },
          "outputs": {
            "message": {
              "message": {
                "timestamp": "2024-12-23T19:10:58",
                "sender": "Machine",
                "sender_name": "AI",
                "session_id": "01ce083d-748b-4b8d-97b6-33adbb6a528a",
                "text": "Hello! 🌟 I'm excited to help you get started on your journey to building something fresh! What do you have in mind? Whether it's a project, an idea, or a concept, let's dive in and make it happen!",
                "files": [],
                "error": false,
                "edit": false,
                "properties": {
                  "text_color": "",
                  "background_color": "",
                  "edited": false,
                  "source": {
                    "id": "OpenAIModel-7AjrN",
                    "display_name": "OpenAI",
                    "source": "gpt-4o-mini"
                  },
                  "icon": "OpenAI",
                  "allow_markdown": false,
                  "positive_feedback": null,
                  "state": "complete",
                  "targets": []
                },
                "category": "message",
                "content_blocks": [],
                "id": "5688356d-9f30-40ca-9907-79a7a2fc16fd",
                "flow_id": "01ce083d-748b-4b8d-97b6-33adbb6a528a"
              },
              "type": "object"
            }
          },
          "logs": { "message": [] },
          "message": {
            "message": "Hello! 🌟 I'm excited to help you get started on your journey to building something fresh! What do you have in mind? Whether it's a project, an idea, or a concept, let's dive in and make it happen!",
            "sender": "Machine",
            "sender_name": "AI",
            "files": [],
            "type": "object"
          },
          "artifacts": {
            "message": "Hello! 🌟 I'm excited to help you get started on your journey to building something fresh! What do you have in mind? Whether it's a project, an idea, or a concept, let's dive in and make it happen!",
            "sender": "Machine",
            "sender_name": "AI",
            "files": [],
            "type": "object"
          },
          "timedelta": 0.017838125000707805,
          "duration": "18 ms",
          "used_frozen_result": false
        },
        "artifacts": {
          "message": "Hello! 🌟 I'm excited to help you get started on your journey to building something fresh! What do you have in mind? Whether it's a project, an idea, or a concept, let's dive in and make it happen!",
          "sender": "Machine",
          "sender_name": "AI",
          "files": [],
          "type": "object"
        },
        "params": "- Files: []\n  Message: Hello! 🌟 I'm excited to help you get started on your journey to building\n    something fresh! What do you have in mind? Whether it's a project, an idea, or\n    a concept, let's dive in and make it happen!\n  Sender: Machine\n  Sender Name: AI\n  Type: object\n",
        "valid": true,
        "build_id": "1e8b908b-aba7-403b-9e9b-eca92bb78668",
        "id": "ChatOutput-sfUhT",
        "timestamp": "2024-12-23T19:10:58.813268Z",
        "flow_id": "01ce083d-748b-4b8d-97b6-33adbb6a528a"
      }
    ]
  }
}
```


### Delete Vertex builds [​](https://docs.langflow.org/api-monitor#delete-vertex-builds)


Delete Vertex builds for a specific flow.


- Python
- JavaScript
- curl


```python
import os

import requests

url = f"{os.getenv('LANGFLOW_URL', '')}/api/v1/monitor/builds?flow_id={os.getenv('FLOW_ID', '')}"

headers = {
    "accept": "*/*",
    "x-api-key": f"{os.getenv('LANGFLOW_API_KEY', '')}",
}

response = requests.request("DELETE", url, headers=headers)
response.raise_for_status()

print(response.text)
```


```js
const url = `${process.env.LANGFLOW_URL ?? ""}/api/v1/monitor/builds?flow_id=${process.env.FLOW_ID ?? ""}`;

const options = {
  method: 'DELETE',
  headers: {
    "accept": `*/*`,
    "x-api-key": `${process.env.LANGFLOW_API_KEY ?? ""}`,
  },
};

fetch(url, options)
  .then(async (response) => {
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    const text = await response.text();
    console.log(text);
  })
  .catch((error) => console.error(error));
```


```bash
curl -X DELETE \
  "$LANGFLOW_URL/api/v1/monitor/builds?flow_id=$FLOW_ID" \
  -H "accept: */*" \
  -H "x-api-key: $LANGFLOW_API_KEY"
```


## Messages endpoints [​](https://docs.langflow.org/api-monitor#messages-endpoints)


The `/monitor/messages` endpoints store, retrieve, edit, and delete records in the message table in [`langflow.db`](https://docs.langflow.org/memory) Typically, these are called implicitly when running flows that produce message history, or when inspecting and modifying **Playground** memories.


### Get messages [​](https://docs.langflow.org/api-monitor#get-messages)


Retrieve a list of all messages:


- Python
- JavaScript
- curl


```python
import os

import requests

url = f"{os.getenv('LANGFLOW_URL', '')}/api/v1/monitor/messages"

headers = {
    "accept": "application/json",
    "x-api-key": f"{os.getenv('LANGFLOW_API_KEY', '')}",
}

response = requests.request("GET", url, headers=headers)
response.raise_for_status()

print(response.text)
```


```js
const url = `${process.env.LANGFLOW_URL ?? ""}/api/v1/monitor/messages`;

const options = {
  method: 'GET',
  headers: {
    "accept": `application/json`,
    "x-api-key": `${process.env.LANGFLOW_API_KEY ?? ""}`,
  },
};

fetch(url, options)
  .then(async (response) => {
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    const text = await response.text();
    console.log(text);
  })
  .catch((error) => console.error(error));
```


```bash
curl -X GET \
  "$LANGFLOW_URL/api/v1/monitor/messages" \
  -H "accept: application/json" \
  -H "x-api-key: $LANGFLOW_API_KEY"
```


To filter messages, use the `flow_id`, `session_id`, `sender`, and `sender_name` query parameters.


To sort the results, use `order_by` to select the field and `order` to select the direction. The `order_by` parameter defaults to `timestamp`, and `order` accepts `ASC` or `DESC` and defaults to `ASC`. With both defaults, the endpoint returns the oldest messages first.


To paginate the results, use `limit` to set the maximum number of messages returned and `offset` to skip messages from the beginning of the ordered result set.


This example retrieves up to 100 messages sent by `Machine` and `AI` in a given chat session (`session_id`), ordered from oldest to newest by timestamp.


- Python
- JavaScript
- curl


```python
import os

import requests

url = f"{os.getenv('LANGFLOW_URL', '')}/api/v1/monitor/messages?flow_id={os.getenv('FLOW_ID', '')}&session_id=01ce083d-748b-4b8d-97b6-33adbb6a528a&sender=Machine&sender_name=AI&order_by=timestamp&order=ASC&limit=100&offset=0"

headers = {
    "accept": "application/json",
    "x-api-key": f"{os.getenv('LANGFLOW_API_KEY', '')}",
}

response = requests.request("GET", url, headers=headers)
response.raise_for_status()

print(response.text)
```


```js
const url = `${process.env.LANGFLOW_URL ?? ""}/api/v1/monitor/messages?flow_id=${process.env.FLOW_ID ?? ""}&session_id=01ce083d-748b-4b8d-97b6-33adbb6a528a&sender=Machine&sender_name=AI&order_by=timestamp&order=ASC&limit=100&offset=0`;

const options = {
  method: 'GET',
  headers: {
    "accept": `application/json`,
    "x-api-key": `${process.env.LANGFLOW_API_KEY ?? ""}`,
  },
};

fetch(url, options)
  .then(async (response) => {
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    const text = await response.text();
    console.log(text);
  })
  .catch((error) => console.error(error));
```


```bash
curl -X GET \
  "$LANGFLOW_URL/api/v1/monitor/messages?flow_id=$FLOW_ID&session_id=01ce083d-748b-4b8d-97b6-33adbb6a528a&sender=Machine&sender_name=AI&order_by=timestamp&order=ASC&limit=100&offset=0" \
  -H "accept: application/json" \
  -H "x-api-key: $LANGFLOW_API_KEY"
```


### Delete messages [​](https://docs.langflow.org/api-monitor#delete-messages)


Delete specific messages by their IDs.


This example deletes the message retrieved in the previous `GET /messages` example.


- Python
- JavaScript
- curl


```python
import os
from uuid import UUID

import requests

base = os.environ.get("LANGFLOW_URL", "")
api_key = os.environ.get("LANGFLOW_API_KEY", "")
flow_id = os.environ.get("FLOW_ID", "")

headers = {"accept": "*/*", "Content-Type": "application/json", "x-api-key": api_key}

list_resp = requests.get(
    f"{base}/api/v1/monitor/messages",
    headers=headers,
    params={"flow_id": flow_id},
    timeout=30,
)
list_resp.raise_for_status()
messages = list_resp.json()
if not messages:
    print("No messages to delete.")
    raise SystemExit(0)

ids = [UUID(str(m["id"])) for m in messages[:2]]
params = [("message_ids", str(i)) for i in ids]

response = requests.delete(f"{base}/api/v1/monitor/messages", headers=headers, params=params, timeout=30)
response.raise_for_status()
print(response.status_code)
```


```js
const url = `${process.env.LANGFLOW_URL ?? ""}/api/v1/monitor/messages`;

const options = {
  method: 'DELETE',
  headers: {
    "accept": `*/*`,
    "Content-Type": `application/json`,
    "x-api-key": `${process.env.LANGFLOW_API_KEY ?? ""}`,
  },
  body: JSON.stringify([
  "MESSAGE_ID_1",
  "MESSAGE_ID_2"
]),
};

fetch(url, options)
  .then(async (response) => {
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    const text = await response.text();
    console.log(text);
  })
  .catch((error) => console.error(error));
```


```bash
curl -v -X DELETE \
  "$LANGFLOW_URL/api/v1/monitor/messages" \
  -H "accept: */*" \
  -H "Content-Type: application/json" \
  -H "x-api-key: $LANGFLOW_API_KEY" \
  -d '["MESSAGE_ID_1", "MESSAGE_ID_2"]'
```


### Update message [​](https://docs.langflow.org/api-monitor#update-message)


Update a specific message by its ID.


This example updates the `text` value of message `3ab66cc6-c048-48f8-ab07-570f5af7b160`.


- Python
- JavaScript
- curl


```python
import os

import requests

base = os.environ.get("LANGFLOW_URL", "")
api_key = os.environ.get("LANGFLOW_API_KEY", "")
flow_id = os.environ.get("FLOW_ID", "")

headers = {"accept": "application/json", "Content-Type": "application/json", "x-api-key": api_key}

list_resp = requests.get(
    f"{base}/api/v1/monitor/messages",
    headers=headers,
    params={"flow_id": flow_id},
    timeout=30,
)
list_resp.raise_for_status()
messages = list_resp.json()
if not messages:
    print("No messages to update.")
    raise SystemExit(0)

message_id = messages[0]["id"]
payload = {"text": "testing 1234"}

response = requests.put(
    f"{base}/api/v1/monitor/messages/{message_id}",
    headers=headers,
    json=payload,
    timeout=30,
)
response.raise_for_status()
print(response.text)
```


```js
const url = `${process.env.LANGFLOW_URL ?? ""}/api/v1/monitor/messages/3ab66cc6-c048-48f8-ab07-570f5af7b160`;

const options = {
  method: 'PUT',
  headers: {
    "accept": `application/json`,
    "Content-Type": `application/json`,
    "x-api-key": `${process.env.LANGFLOW_API_KEY ?? ""}`,
  },
  body: JSON.stringify({
  "text": "testing 1234"
}),
};

fetch(url, options)
  .then(async (response) => {
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    const text = await response.text();
    console.log(text);
  })
  .catch((error) => console.error(error));
```


```bash
curl -X PUT \
  "$LANGFLOW_URL/api/v1/monitor/messages/3ab66cc6-c048-48f8-ab07-570f5af7b160" \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -H "x-api-key: $LANGFLOW_API_KEY" \
  -d '{
  "text": "testing 1234"
}'
```


### Update session ID [​](https://docs.langflow.org/api-monitor#update-session-id)


Update the session ID for messages.


This example updates the `session_ID` value `01ce083d-748b-4b8d-97b6-33adbb6a528a` to `different_session_id`.


- Python
- JavaScript
- curl


```python
import os

import requests

base = os.environ.get("LANGFLOW_URL", "")
api_key = os.environ.get("LANGFLOW_API_KEY", "")
flow_id = os.environ.get("FLOW_ID", "")

headers = {"accept": "application/json", "x-api-key": api_key}

list_resp = requests.get(
    f"{base}/api/v1/monitor/messages",
    headers=headers,
    params={"flow_id": flow_id},
    timeout=30,
)
list_resp.raise_for_status()
messages = list_resp.json()
if not messages:
    print("No messages; cannot migrate session id.")
    raise SystemExit(0)

old_session_id = messages[0]["session_id"]
new_session_id = f"{old_session_id}-migrated"

response = requests.patch(
    f"{base}/api/v1/monitor/messages/session/{old_session_id}",
    headers=headers,
    params={"new_session_id": new_session_id},
    timeout=30,
)
response.raise_for_status()
print(response.text)
```


```js
const url = `${process.env.LANGFLOW_URL ?? ""}/api/v1/monitor/messages/session/01ce083d-748b-4b8d-97b6-33adbb6a528a?new_session_id=different_session_id`;

const options = {
  method: 'PATCH',
  headers: {
    "accept": `application/json`,
    "x-api-key": `${process.env.LANGFLOW_API_KEY ?? ""}`,
  },
};

fetch(url, options)
  .then(async (response) => {
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    const text = await response.text();
    console.log(text);
  })
  .catch((error) => console.error(error));
```


```bash
curl -X PATCH \
  "$LANGFLOW_URL/api/v1/monitor/messages/session/01ce083d-748b-4b8d-97b6-33adbb6a528a?new_session_id=different_session_id" \
  -H "accept: application/json" \
  -H "x-api-key: $LANGFLOW_API_KEY"
```


### Delete messages by session [​](https://docs.langflow.org/api-monitor#delete-messages-by-session)


Delete all messages for a specific session.


- Python
- JavaScript
- curl


```python
import os

import requests

url = f"{os.getenv('LANGFLOW_URL', '')}/api/v1/monitor/messages/session/different_session_id_2"

headers = {
    "accept": "*/*",
    "x-api-key": f"{os.getenv('LANGFLOW_API_KEY', '')}",
}

response = requests.request("DELETE", url, headers=headers)
response.raise_for_status()

print(response.text)
```


```js
const url = `${process.env.LANGFLOW_URL ?? ""}/api/v1/monitor/messages/session/different_session_id_2`;

const options = {
  method: 'DELETE',
  headers: {
    "accept": `*/*`,
    "x-api-key": `${process.env.LANGFLOW_API_KEY ?? ""}`,
  },
};

fetch(url, options)
  .then(async (response) => {
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    const text = await response.text();
    console.log(text);
  })
  .catch((error) => console.error(error));
```


```bash
curl -X DELETE \
  "$LANGFLOW_URL/api/v1/monitor/messages/session/different_session_id_2" \
  -H "accept: */*" \
  -H "x-api-key: $LANGFLOW_API_KEY"
```


## Get traces [​](https://docs.langflow.org/api-monitor#get-traces)


Retrieve trace metadata and span trees for a specific flow.


### Example request [​](https://docs.langflow.org/api-monitor#example-request)


Use `GET /monitor/traces` and filter by `flow_id`:


- Python
- TypeScript
- curl


```python
import os

import requests

base_url = os.environ.get("LANGFLOW_URL") or os.environ.get("LANGFLOW_SERVER_URL", "http://127.0.0.1:7860")
api_key = os.environ.get("LANGFLOW_API_KEY", "")
flow_id = os.environ.get("FLOW_ID", "")

response = requests.get(
    f"{base_url}/api/v1/monitor/traces",
    params={"flow_id": flow_id, "page": 1, "size": 50},
    headers={"x-api-key": api_key, "accept": "application/json"},
    timeout=30,
)
response.raise_for_status()
print(response.json())
```


```ts
const baseUrl = process.env.LANGFLOW_SERVER_URL ?? "http://localhost:7860";
const apiKey = process.env.LANGFLOW_API_KEY!;
const flowId = "YOUR_FLOW_ID";

async function listTraces() {
  const url = new URL("/api/v1/monitor/traces", baseUrl);
  url.searchParams.set("flow_id", flowId);
  url.searchParams.set("page", "1");
  url.searchParams.set("size", "50");

  const res = await fetch(url.toString(), {
    headers: {
      accept: "application/json",
      "x-api-key": apiKey,
    },
  });

  if (!res.ok) {
    throw new Error(`Request failed with status ${res.status}`);
  }

  const data = await res.json();
  console.log(data);
}

listTraces().catch(console.error);
```


```bash
export LANGFLOW_SERVER_URL="http://localhost:7860"
export LANGFLOW_API_KEY="YOUR_LANGFLOW_API_KEY"
export FLOW_ID="YOUR_FLOW_ID"

curl -s "$LANGFLOW_SERVER_URL/api/v1/monitor/traces?flow_id=$FLOW_ID&page=1&size=50" \
  -H "accept: application/json" \
  -H "x-api-key: $LANGFLOW_API_KEY" \
  | jq .
```


### Example response [​](https://docs.langflow.org/api-monitor#example-response)


```json
{
  "traces": [
    {
      "id": "426656db-fc3c-4a3a-acf8-c60acf099543",
      "name": "Simple Agent - 9e774f60-857b-44b4-bbcd-87bd23848ee8",
      "status": "ok",
      "startTime": "2026-03-03T19:13:30.692628Z",
      "totalLatencyMs": 18693,
      "totalTokens": 2050,
      "flowId": "9e774f60-857b-44b4-bbcd-87bd23848ee8",
      "sessionId": "9e774f60-857b-44b4-bbcd-87bd23848ee8",
      "input": {
        "input_value": "Use tools to teach me about vertex graphs"
      },
      "output": {
        "message": {
          "text_key": "text",
          "data": {
            "timestamp": "2026-03-03 19:13:30 UTC",
            "sender": "Machine",
            "sender_name": "AI",
            "session_id": "9e774f60-857b-44b4-bbcd-87bd23848ee8",
            "text": "I can teach you the concept, but I couldn’t pull the Wikipedia pages with the tool ... (truncated)"
          }
        }
      }
    }
  ],
  "total": 1,
  "pages": 1
}
```


## Get transactions [​](https://docs.langflow.org/api-monitor#get-transactions)


Retrieve all transactions, which are interactions between components, for a specific flow. This information is also available in [flow logs](https://docs.langflow.org/logging).


- Python
- JavaScript
- curl


```python
import os

import requests

url = f"{os.getenv('LANGFLOW_URL', '')}/api/v1/monitor/transactions?flow_id={os.getenv('FLOW_ID', '')}&page=1&size=50"

headers = {
    "accept": "application/json",
    "x-api-key": f"{os.getenv('LANGFLOW_API_KEY', '')}",
}

response = requests.request("GET", url, headers=headers)
response.raise_for_status()

print(response.text)
```


```js
const url = `${process.env.LANGFLOW_URL ?? ""}/api/v1/monitor/transactions?flow_id=${process.env.FLOW_ID ?? ""}&page=1&size=50`;

const options = {
  method: 'GET',
  headers: {
    "accept": `application/json`,
    "x-api-key": `${process.env.LANGFLOW_API_KEY ?? ""}`,
  },
};

fetch(url, options)
  .then(async (response) => {
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    const text = await response.text();
    console.log(text);
  })
  .catch((error) => console.error(error));
```


```bash
curl -X GET \
  "$LANGFLOW_URL/api/v1/monitor/transactions?flow_id=$FLOW_ID&page=1&size=50" \
  -H "accept: application/json" \
  -H "x-api-key: $LANGFLOW_API_KEY"
```


## See also [​](https://docs.langflow.org/api-monitor#see-also)


- [Use voice mode](https://docs.langflow.org/concepts-voice-mode)
- [Session ID](https://docs.langflow.org/session-id)


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)

- [Vertex builds](https://docs.langflow.org/api-monitor#vertex-builds)
  - [Get Vertex builds](https://docs.langflow.org/api-monitor#get-vertex-builds)
  - [Delete Vertex builds](https://docs.langflow.org/api-monitor#delete-vertex-builds)- [Messages endpoints](https://docs.langflow.org/api-monitor#messages-endpoints)
  - [Get messages](https://docs.langflow.org/api-monitor#get-messages)
  - [Delete messages](https://docs.langflow.org/api-monitor#delete-messages)
  - [Update message](https://docs.langflow.org/api-monitor#update-message)
  - [Update session ID](https://docs.langflow.org/api-monitor#update-session-id)
  - [Delete messages by session](https://docs.langflow.org/api-monitor#delete-messages-by-session)- [Get traces](https://docs.langflow.org/api-monitor#get-traces)
  - [Example request](https://docs.langflow.org/api-monitor#example-request)
  - [Example response](https://docs.langflow.org/api-monitor#example-response)- [Get transactions](https://docs.langflow.org/api-monitor#get-transactions)
- [See also](https://docs.langflow.org/api-monitor#see-also)[Manage Privacy Choices](https://docs.langflow.org/api-monitor#)

---

# Human-in-the-Loop | Langflow Documentation

`https://docs.langflow.org/human-in-the-loop`

Copy page ⌥C Version: 1.12.x On this page
## Use HITL in a flow​
*For a video example, see the Langflow 1.11 release blog.*

## See also​



Human-in-the-Loop (HITL) pauses a flow, creates a checkpoint, and waits for a human decision.


After you approve or reject the proposed action, the flow run resumes from the checkpoint using the selected branch. The previously completed steps are not executed again.


To include a HITL gate in a flow, add a [**Human Input** component](https://docs.langflow.org/human-input), or configure your Agent component to [require approval for agent tools](https://docs.langflow.org/agents-tools#require-approval-for-agent-tools).


For example, imagine you're building an agent that drafts Python code, and one of its tools can commit code to Git.


The **Human Input** component pauses the flow where you place the component, and creates one output branch per configured **User Action**. Place the component after the code generation steps, where a human selects an **Approve** or **Reject** user action. If a human selects **Approve**, the flow continues to the commit step, and if a human selects **Reject**, the flow sends the draft back for revision. For more information, see the [**Human Input** component](https://docs.langflow.org/human-input).


The **Agent** tool approval enables **Requires approval** on the Git commit tool *only*. The run pauses when the agent tries to call that tool, but doesn't add a branch. For more information, see [Require approval for agent tools](https://docs.langflow.org/agents-tools#require-approval-for-agent-tools).


## Use HITL in a flow [​](https://docs.langflow.org/human-in-the-loop#use-hitl-in-a-flow)


For a video example, see the [Langflow 1.11 release blog](https://www.langflow.org/blog/langflow-1-11).


## See also [​](https://docs.langflow.org/human-in-the-loop#see-also)


- [Human Input component](https://docs.langflow.org/human-input)
- [Agents](https://docs.langflow.org/components-agents)


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)

- [Use HITL in a flow](https://docs.langflow.org/human-in-the-loop#use-hitl-in-a-flow)
- [See also](https://docs.langflow.org/human-in-the-loop#see-also)[Manage Privacy Choices](https://docs.langflow.org/human-in-the-loop#)

---

# Block custom components | Langflow Documentation

`https://docs.langflow.org/deployment-block-custom-components`

# Block custom components

To block custom component creation on a Langflow server, set the following environment variable:

Copy page ⌥C Version: 1.12.x On this page
## Upgrading a server that blocks custom components​
## Custom components in publicly shared flows​
## Interaction with catalog governance​
## Configure a custom component allow-list​





Custom components and the component code editor allow Langflow users to create and execute Python code in the Langflow runtime. While this freedom is a feature of Langflow, in some deployments you might want to block the creation of custom Langflow components to prevent arbitrary code execution.


To block custom component creation on a Langflow server, set the following [environment variable](https://docs.langflow.org/environment-variables):


```bash
LANGFLOW_ALLOW_CUSTOM_COMPONENTS=false
```


When set to `false`, Langflow blocks creating custom components, changing code in the visual editor, and running [registered built-in code-execution components](https://docs.langflow.org/api-keys-and-authentication#multi-tenant-component-hardening).


When unset or `true`, Langflow allows custom code. Existing installations keep the default `true` behavior until you opt in to this restriction.


This environment variable is a beta feature, and should not be your only safeguard in production environments.


In the event that Langflow could execute untrusted or LLM-generated code, run Langflow in an isolated and containerized execution environment.


### Restrict custom component creation to superusers [​](https://docs.langflow.org/deployment-block-custom-components#restrict-custom-components-to-superusers)


To restrict custom component creation to superusers while keeping built-in components functional for users, set the following [environment variable](https://docs.langflow.org/environment-variables):


```bash
LANGFLOW_CUSTOM_COMPONENT_ADMIN_ONLY=true
```


When set to `true`, non-superusers can still view and use custom components in flows, but they cannot create new custom components or edit custom component code.


## Upgrading a server that blocks custom components [​](https://docs.langflow.org/deployment-block-custom-components#upgrading-with-custom-components-blocked)


While `LANGFLOW_ALLOW_CUSTOM_COMPONENTS=false`, Langflow never runs the component code stored in a flow. It looks up its own copy of that component and runs that instead. The code saved in the flow is only used to identify which component the node is.


This matters when you upgrade. Langflow releases change built-in component code, so after an upgrade the code saved in your flows no longer matches the code the new version ships. By default, Langflow rebuilds those nodes with its own current copy of the component and the flows keep running. Each substitution is logged, and the flow itself is left untouched. The visual editor continues to mark the component as outdated until you update it, but that marker doesn't block editor or Playground runs.


Nothing new becomes runnable: the code that runs is always the server's own, chosen by component type. A node whose component type this server doesn't recognize is still refused. This is the same rule Langflow already applies by default to unauthenticated public flow builds.


A node is also refused, rather than rebuilt, when more than one component claims its type — for example a component in `LANGFLOW_COMPONENTS_PATH` installed under a name a built-in already uses. Langflow can't tell which of the two the node meant, so it declines to guess and asks you to update the component instead.


To require an exact match instead, so that any flow containing a component whose stored code has drifted is refused until you update that component, set:


```bash
LANGFLOW_SUBSTITUTE_OUTDATED_COMPONENT_CODE=false
```


With this set, an upgrade that changes a built-in component blocks every saved flow using it, with an error naming the components to update:


```text
Flow build blocked: outdated components must be updated before running: <display_name> (<node_id>)
```


To update those components, open each flow in the visual editor and apply the component update, or update flow files with `lfx upgrade <flow.json>`. This setting has no effect while `LANGFLOW_ALLOW_CUSTOM_COMPONENTS` is `true`, since the flow's own code runs as authored.


## Custom components in publicly shared flows [​](https://docs.langflow.org/deployment-block-custom-components#public-flow-custom-components)


The [**Shareable Playground**](https://docs.langflow.org/concepts-playground#share-a-flows-playground) exposes a single flow at `/public_flow/$FLOW_ID` and runs it without authentication, as its owner. Because anyone holding the link can trigger that run, Langflow applies a stricter rule to public flow builds than to authenticated ones, and it applies regardless of how `LANGFLOW_ALLOW_CUSTOM_COMPONENTS` is set.


By default, on every unauthenticated public flow build Langflow replaces each node's stored code with its own copy of that component, selected by component type, and refuses any node whose type it doesn't recognize. A built-in component whose stored code has drifted across an upgrade still runs, because the server's current copy is what executes. A component the server doesn't know, such as one written in the visual editor's code editor and saved only inside the flow, has no server copy, so the build is refused and the visitor sees:


```text
This flow cannot be executed.
```


The server log names the components that were blocked:


```text
Public flow build blocked: unrecognized custom components are not allowed: <display_name> (<node_id>)
```


While `LANGFLOW_ALLOW_CUSTOM_COMPONENTS` is `true`, the same flow still runs in the visual editor, in the **Playground**, and through the Langflow API, because those calls are authenticated.


### Install the component on the server [​](https://docs.langflow.org/deployment-block-custom-components#install-the-component-on-the-server)


The recommended way to run a custom component in a shared **Playground** is to make it a component the server knows, by adding it to a directory in [`LANGFLOW_COMPONENTS_PATH`](https://docs.langflow.org/deployment-block-custom-components#configure-a-custom-component-allow-list):


```bash
LANGFLOW_COMPONENTS_PATH=/path/to/custom_components
```


Its code is then part of the server's template set, so public flow builds substitute the server's copy the same way they do for a built-in component, and the flow runs. Nothing is relaxed: the code that executes is still the operator-installed code on the server, not the code stored in the flow.


### Allow stored code on the public path [​](https://docs.langflow.org/deployment-block-custom-components#allow-stored-code-on-the-public-path)


To run the code stored in the flow instead, set:


```bash
LANGFLOW_ALLOW_PUBLIC_CUSTOM_COMPONENTS=true
```


The two settings combine as follows.


| `LANGFLOW_ALLOW_CUSTOM_COMPONENTS` | `LANGFLOW_ALLOW_PUBLIC_CUSTOM_COMPONENTS` | Public flow build |
| --- | --- | --- |
| `true` (default) | `false` (default) | The server's own component code runs. Components the server doesn't know are refused. |
| `true` | `true` | The code stored in the flow runs, for every node in the flow. |
| `false` | Either | The server's own component code runs. Components the server doesn't know are refused. |


## Interaction with catalog governance [​](https://docs.langflow.org/deployment-block-custom-components#interaction-with-catalog-governance)


Catalog governance takes precedence over the custom-code settings on the custom-component create, update, and code-validation endpoints. A catalog block has no superuser bypass.


| Submitted source | Catalog policy | Custom components | Admin-only mode | Result |
| --- | --- | --- | --- | --- |
| Known server template | Blocked | Either | Either | Denied for every user |
| Known server template | Allowed | Disabled | Either | Allowed using the trusted server source |
| Known server template | Allowed | Enabled | Non-superuser | Allowed using the trusted server source |
| Unknown custom source | Not blocked | Disabled | Either | Denied |
| Unknown custom source | Not blocked | Enabled | Non-superuser | Denied |
| Unknown custom source | Not blocked | Enabled | Superuser or admin-only disabled | Allowed |


For `POST /api/v1/validate/code`, this policy runs before the source is parsed or imports are inspected. In a restricted custom-code mode, known templates are validated from the trusted server copy, while unknown source follows the same disabled or admin-only rule as the component editor. On custom-component create and update, known blocked template source is rejected before the component is built, and the resolved component type is checked again before request-supplied frontend updates are applied.


An active catalog policy fails closed with a temporary `503` response while server template identities are still initializing. An empty catalog policy preserves the default behavior and does not require template identity lookups.


## Configure a custom component allow-list [​](https://docs.langflow.org/deployment-block-custom-components#configure-a-custom-component-allow-list)


`LANGFLOW_ALLOW_CUSTOM_COMPONENTS` works together with optional paths that define which component templates the server loads, and which code hashes are trusted.


Directories listed in the `LANGFLOW_COMPONENTS_PATH` environment variable are loaded as custom components and merged into the server’s template set. When `LANGFLOW_ALLOW_CUSTOM_COMPONENTS` is set to `false`, the components in the `LANGFLOW_COMPONENTS_PATH` directory **remain allowed**.


To allow some components while blocking others, include the allowed custom components directory in `LANGFLOW_COMPONENTS_PATH` and set `LANGFLOW_ALLOW_CUSTOM_COMPONENTS` to `false`.


`LANGFLOW_COMPONENTS_INDEX_PATH` points to a prebuilt component index JSON file at a local path or `http://` / `https://` URL. This environment variable replaces the default index bundled with the `lfx` package. It does **not** import Python modules from a directory on disk. To allow-list custom components, use the `LANGFLOW_COMPONENTS_PATH` environment variable.


If both environment variables are set, Langflow builds one combined set of components from the custom index *and* from `LANGFLOW_COMPONENTS_PATH`. If the same component category name exists in both, `LANGFLOW_COMPONENTS_PATH` replaces that whole category from the custom index.


### Disable the allow-list bypass [​](https://docs.langflow.org/deployment-block-custom-components#disable-the-allow-list-bypass)


The allow-list behavior above assumes the admin controls which env vars are set at startup. In deployments where that assumption doesn't hold, set:


```bash
LANGFLOW_ALLOW_COMPONENTS_PATHS_OVERRIDE=false
```


When this is `false` **and** `LANGFLOW_ALLOW_CUSTOM_COMPONENTS=false`, components contributed by `LANGFLOW_COMPONENTS_PATH` and `LANGFLOW_COMPONENTS_INDEX_PATH` are ignored and no longer bypass the block.


Default is `true`, which preserves existing behavior. The setting has no effect while `LANGFLOW_ALLOW_CUSTOM_COMPONENTS=true`, since nothing is being bypassed.


To hide or refuse named built-in components, starter templates, model providers, or models without turning off custom code entirely, use the superuser [catalog and model policy APIs](https://docs.langflow.org/api-governance-policy).


For more information, see:


- [Environment variables](https://docs.langflow.org/environment-variables#visual-editor-and-playground-behavior)
- [Security](https://docs.langflow.org/security)


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)

- [Restrict custom component creation to superusers](https://docs.langflow.org/deployment-block-custom-components#restrict-custom-components-to-superusers)
- [Upgrading a server that blocks custom components](https://docs.langflow.org/deployment-block-custom-components#upgrading-with-custom-components-blocked)
- [Custom components in publicly shared flows](https://docs.langflow.org/deployment-block-custom-components#public-flow-custom-components)
  - [Install the component on the server](https://docs.langflow.org/deployment-block-custom-components#install-the-component-on-the-server)
  - [Allow stored code on the public path](https://docs.langflow.org/deployment-block-custom-components#allow-stored-code-on-the-public-path)- [Interaction with catalog governance](https://docs.langflow.org/deployment-block-custom-components#interaction-with-catalog-governance)
- [Configure a custom component allow-list](https://docs.langflow.org/deployment-block-custom-components#configure-a-custom-component-allow-list)
  - [Disable the allow-list bypass](https://docs.langflow.org/deployment-block-custom-components#disable-the-allow-list-bypass)[Manage Privacy Choices](https://docs.langflow.org/deployment-block-custom-components#)

---

# Use session ID to manage communication between components | Langflow Documentation

`https://docs.langflow.org/session-id`

# Use session ID to manage communication between components

In the Langflow Playground, current sessions are listed on the left side of the pane.

Copy page ⌥C Version: 1.12.x On this page
## Customize session ID​
## Retrieval of messages from memory by session ID​



Session ID is a unique identifier for client/server connections. A single session equals the duration of a client's connection to a server.


In the Langflow **Playground**, current sessions are listed on the left side of the pane.


Langflow uses session IDs to track different chat interactions within flows. This allows multiple chat sessions to exist in a single flow. Messages are stored in the database with session IDs as a reference.


This differentiation between users per session is helpful in managing client/server connections, but is also important in maintaining separate conversational contexts within a single flow. LLMs rely on past interactions to generate responses to queries, and if these conversations aren't separated, the responses becomes less useful, or even confused.


## Customize session ID [​](https://docs.langflow.org/session-id#customize-session-id)


Custom session IDs can be set as part of the payload in API calls, or as advanced settings in individual components. The API session ID value takes precedence. If no session ID is specified, the flow ID is assigned.


If you set a custom session ID in a payload, all downstream components use the upstream component's session ID value. Replace `LANGFLOW_SERVER_ADDRESS`, `FLOW_ID`, and `LANGFLOW_API_KEY` with the values from your Langflow deployment.


```text
curl --request POST \
  --url "http://LANGFLOW_SERVER_ADDRESS/api/v1/run/FLOW_ID" \
  --header "Content-Type: application/json" \
  --header "x-api-key: $LANGFLOW_API_KEY" \
  --data '{
  "input_value": "Hello",
  "output_type": "chat",
  "input_type": "chat",
  "session_id": "my_custom_session_value"
}'
```


The `my_custom_session_value` value is used in components that accept it, and the stored messages from this flow are stored in `langflow.db` with their respective `session_id` values.


## Retrieval of messages from memory by session ID [​](https://docs.langflow.org/session-id#retrieval-of-messages-from-memory-by-session-id)


To retrieve messages from local Langflow memory, add a [**Message History** component](https://docs.langflow.org/message-history) to your flow. The component accepts `sessionID` as a filter parameter, and uses the session ID value from upstream automatically to retrieve message history by session ID from storage.


Messages can be retrieved by `session_id` from the Langflow API at `GET /v1/monitor/messages`. For more information, see [Monitor endpoints](https://docs.langflow.org/api-monitor).


For an example of session ID in action, see [Use Session IDs in Langflow](https://www.youtube.com/watch?v=nJiF_eF21MY).


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)

- [Customize session ID](https://docs.langflow.org/session-id#customize-session-id)
- [Retrieval of messages from memory by session ID](https://docs.langflow.org/session-id#retrieval-of-messages-from-memory-by-session-id)[Manage Privacy Choices](https://docs.langflow.org/session-id#)

---

# Workflow API quickstart | Langflow Documentation

`https://docs.langflow.org/workflow-api-quickstart`

# Workflow API quickstart
## Prerequisites​
*For more information, see Create a Langflow API key.*

## Run a flow synchronously​
## Stream LLM tokens​
## Run in the background​
*To connect to a background run, see Re-attach to a background run.*

## Next steps​






The Workflow API executes Langflow flows over POST /api/v2/workflows in three modes.

Copy page ⌥C Version: 1.12.x On this page

The [Workflow API](https://docs.langflow.org/workflow-api) executes Langflow flows over `POST /api/v2/workflows` in three modes.


Use the default **`sync`** mode when you want to wait for the full JSON result in one response. Use **`stream`** when you need live Server-Sent Events (SSE) emitted as the flow runs. Use **`background`** when you want to queue a job and then poll or re-attach to its event stream.


This quickstart runs the same flow with each mode, so you can use the mode that fits your application.


## Prerequisites [​](https://docs.langflow.org/workflow-api-quickstart#prerequisites)


- [Install and start Langflow](https://docs.langflow.org/get-started-installation) with the developer API enabled The Workflow API endpoints require the `developer_api_enabled` setting to be enabled. If this setting is disabled, these endpoints will return a 404 Not Found error. To enable the developer API endpoint, do the following: For more information about configuring environment variables, see [Environment variables](https://docs.langflow.org/environment-variables).
  1. In the Langflow `.env` file, set the environment variable to `true`: ```text LANGFLOW_DEVELOPER_API_ENABLED=true ```
  2. Start your Langflow server with the `.env` file enabled: ```text uv run langflow run --env-file .env ```- [Create a Langflow API key](https://docs.langflow.org/api-keys-and-authentication)
- [Create a flow](https://docs.langflow.org/concepts-flows) that you want to execute
- [Get the flow ID](https://docs.langflow.org/concepts-publish#api-access) or endpoint name of the flow you want to execute


### Set environment variables [​](https://docs.langflow.org/workflow-api-quickstart#set-environment-variables)


All code examples in this documentation assume you have set the following environment variables:


**Python:**


```python
import os

LANGFLOW_SERVER_URL = os.getenv("LANGFLOW_SERVER_URL")
LANGFLOW_API_KEY = os.getenv("LANGFLOW_API_KEY")
```


**TypeScript/JavaScript:**


```ts
const LANGFLOW_SERVER_URL = process.env.LANGFLOW_SERVER_URL;
const LANGFLOW_API_KEY = process.env.LANGFLOW_API_KEY;
```


Set these environment variables before running the examples, or replace the variable references in the code examples with your actual Langflow server URL and API key.


The default `LANGFLOW_SERVER_URL` for a local Langflow deployment is `http://localhost:7860`. For remote deployments, the domain is set by your hosting service, such as `https://UUID.ngrok.app`.


### Authentication and headers [​](https://docs.langflow.org/workflow-api-quickstart#authentication-and-headers)


All Workflow API requests require authentication using a Langflow API key. The API key is passed in the `x-api-key` header.


For more information, see [Create a Langflow API key](https://docs.langflow.org/api-keys-and-authentication).


| Header | Description | Example |
| --- | --- | --- |
| `Content-Type` | Specifies the JSON format. | `application/json` |
| `x-api-key` | Your Langflow API key. | `sk-...` |
| `accept` | Optional. Specifies the response format. | `application/json` |


The examples on this page also expect `FLOW_ID` to be set to your flow's UUID. Use a chat-style flow (for example **Basic Prompting**) so `output.text` contains the assistant reply.


## Run a flow synchronously [​](https://docs.langflow.org/workflow-api-quickstart#run-a-flow-synchronously)


Omit `mode` or set `"mode": "sync"` to run inline. When the flow finishes, the response includes a top-level `output.text` field with the primary answer.


- Python
- JavaScript
- curl


```python
import os

import requests

base = os.environ.get("LANGFLOW_URL") or os.environ.get("LANGFLOW_SERVER_URL", "")
flow_id = os.environ.get("FLOW_ID", "")
api_key = os.environ.get("LANGFLOW_API_KEY", "")

headers = {"Content-Type": "application/json", "x-api-key": api_key}
payload = {
    "flow_id": flow_id,
    "input_value": "what is 2+2",
    "session_id": "session-123",
    "mode": "sync",
}

response = requests.post(f"{base}/api/v2/workflows", headers=headers, json=payload, timeout=120)
response.raise_for_status()
body = response.json()
print(body["output"]["text"])
```


```js
(async () => {
  const base = (process.env.LANGFLOW_URL ?? process.env.LANGFLOW_SERVER_URL ?? "").replace(/\/$/, "");
  const flowId = process.env.FLOW_ID ?? "";
  const apiKey = process.env.LANGFLOW_API_KEY ?? "";

  const response = await fetch(`${base}/api/v2/workflows`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "x-api-key": apiKey,
    },
    body: JSON.stringify({
      flow_id: flowId,
      input_value: "what is 2+2",
      session_id: "session-123",
      mode: "sync",
    }),
  });

  if (!response.ok) {
    throw new Error(`HTTP ${response.status}: ${await response.text()}`);
  }

  const body = await response.json();
  console.log(body.output.text);
})().catch((error) => {
  console.error(error);
  process.exit(1);
});
```


```bash
curl -X POST \
  "$LANGFLOW_SERVER_URL/api/v2/workflows" \
  -H "Content-Type: application/json" \
  -H "x-api-key: $LANGFLOW_API_KEY" \
  -d '{
    "flow_id": "'"${FLOW_ID}"'",
    "input_value": "what is 2+2",
    "session_id": "session-123",
    "mode": "sync"
  }'
```


## Stream LLM tokens [​](https://docs.langflow.org/workflow-api-quickstart#stream-llm-tokens)


Set `"mode": "stream"` to open an SSE stream. Choose the wire format with `stream_protocol`:


- **`langflow`** (default): Langflow `EventManager` frames for existing Langflow clients.
- **`agui`**: [AG-UI](https://docs.ag-ui.com/introduction) lifecycle events for compatible clients.


For request examples, event types, and protocol details, see [Execute flow with selected `stream` mode](https://docs.langflow.org/workflow-api#execute-flow-with-selected-stream-mode) in the Workflow API reference.


### Langflow EventManager (default) [​](https://docs.langflow.org/workflow-api-quickstart#langflow-eventmanager-default)


Each `data:` line is JSON shaped like `{"event": "<type>", "data": {...}}`. The example below prints only `token` events (`data.chunk`) as they arrive.


- Python
- JavaScript
- curl


```python
import json
import os

import requests

base = os.environ.get("LANGFLOW_URL") or os.environ.get("LANGFLOW_SERVER_URL", "")
flow_id = os.environ.get("FLOW_ID", "")
api_key = os.environ.get("LANGFLOW_API_KEY", "")

headers = {"Content-Type": "application/json", "x-api-key": api_key}
payload = {
    "flow_id": flow_id,
    "input_value": "Tell me a short joke.",
    "mode": "stream",
    "session_id": "session-123",
}

with requests.post(
    f"{base}/api/v2/workflows",
    headers=headers,
    json=payload,
    stream=True,
    timeout=120,
) as response:
    response.raise_for_status()
    for line in response.iter_lines(decode_unicode=True):
        if not line or not line.startswith("data:"):
            continue
        frame = json.loads(line.removeprefix("data:").strip())
        if frame.get("event") == "token":
            print(frame["data"]["chunk"], end="", flush=True)
    print()
```


```js
(async () => {
  const base = (process.env.LANGFLOW_URL ?? process.env.LANGFLOW_SERVER_URL ?? "").replace(/\/$/, "");
  const flowId = process.env.FLOW_ID ?? "";
  const apiKey = process.env.LANGFLOW_API_KEY ?? "";

  const response = await fetch(`${base}/api/v2/workflows`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "x-api-key": apiKey,
    },
    body: JSON.stringify({
      flow_id: flowId,
      input_value: "Tell me a short joke.",
      mode: "stream",
      session_id: "session-123",
    }),
  });

  if (!response.ok) {
    throw new Error(`HTTP ${response.status}: ${await response.text()}`);
  }

  const reader = response.body.getReader();
  const decoder = new TextDecoder();
  let buffer = "";

  while (true) {
    const { done, value } = await reader.read();
    if (done) {
      break;
    }
    buffer += decoder.decode(value, { stream: true });
    const lines = buffer.split("\n");
    buffer = lines.pop() ?? "";
    for (const line of lines) {
      if (!line.startsWith("data:")) {
        continue;
      }
      const frame = JSON.parse(line.slice(5).trim());
      if (frame.event === "token") {
        process.stdout.write(frame.data.chunk);
      }
    }
  }

  buffer += decoder.decode();
  if (buffer.trim().startsWith("data:")) {
    const frame = JSON.parse(buffer.slice(5).trim());
    if (frame.event === "token") {
      process.stdout.write(frame.data.chunk);
    }
  }

  process.stdout.write("\n");
})().catch((error) => {
  console.error(error);
  process.exit(1);
});
```


```bash
curl -N -X POST \
  "$LANGFLOW_SERVER_URL/api/v2/workflows" \
  -H "Content-Type: application/json" \
  -H "x-api-key: $LANGFLOW_API_KEY" \
  -d '{
    "flow_id": "'"${FLOW_ID}"'",
    "input_value": "Tell me a short joke.",
    "mode": "stream",
    "session_id": "session-123"
  }'
```


### AG-UI [​](https://docs.langflow.org/workflow-api-quickstart#ag-ui)


Send `"stream_protocol": "agui"`. Each `data:` line contains one AG-UI event as JSON. The example below handles `TEXT_MESSAGE_CONTENT`, `TOOL_CALL_RESULT`, and `RUN_FINISHED`, extracts a number from the first reply, then chains a follow-up prompt in the same `session_id`.


- Python
- JavaScript
- curl


```python
import json
import os
import re

import requests

base = os.environ.get("LANGFLOW_URL") or os.environ.get("LANGFLOW_SERVER_URL", "")
flow_id = os.environ.get("FLOW_ID", "67ccd2be-17f0-8190-81ff-3bb2cf6508e6")
api_key = os.environ.get("LANGFLOW_API_KEY", "")
session_id = os.environ.get("AGUI_SESSION_ID", "thread-123")
number = re.compile(r"-?\d+(?:\.\d+)?")


def extract_number(text: str, tool_results: list) -> float | None:
    """Prefer calculator tool output, then the last number in the assistant reply."""
    for raw in reversed(tool_results):
        if matches := number.findall(str(raw)):
            return float(matches[-1])
    if matches := number.findall(text):
        return float(matches[-1])
    return None


def ask(prompt: str) -> tuple[str, list]:
    """Stream one AG-UI run; return assistant text and tool results."""
    text = ""
    tool_results = []

    with requests.post(
        f"{base}/api/v2/workflows",
        headers={
            "Content-Type": "application/json",
            "x-api-key": api_key,
            "Accept": "text/event-stream",
        },
        json={
            "flow_id": flow_id,
            "input_value": prompt,
            "mode": "stream",
            "stream_protocol": "agui",
            "session_id": session_id,
        },
        stream=True,
        timeout=120,
    ) as response:
        response.raise_for_status()
        for line in response.iter_lines(decode_unicode=True):
            if not line or not line.startswith("data:"):
                continue
            event = json.loads(line.removeprefix("data:").strip())
            match event.get("type"):
                case "TEXT_MESSAGE_CONTENT":
                    text += event.get("delta", "")
                case "TOOL_CALL_RESULT":
                    tool_results.append(event.get("content") or event.get("result"))
                case "RUN_ERROR":
                    raise RuntimeError(event.get("message") or "Run failed")
                case "RUN_FINISHED":
                    break

    return text, tool_results


prompt1 = os.environ.get("AGUI_PROMPT1", "What is 847 divided by 7?")
multiplier = int(os.environ.get("AGUI_MULTIPLIER", "3"))

print(f"User: {prompt1}")
reply1, tools1 = ask(prompt1)
quotient = extract_number(reply1, tools1)
if quotient is None:
    raise SystemExit("Could not extract a number from run 1.")
print(f"Assistant: {reply1.strip()}")
print(f"Extracted: {quotient:g}")

prompt2 = os.environ.get("AGUI_PROMPT2") or f"Now multiply {quotient:g} by {multiplier}."
print(f"\nUser: {prompt2}")
reply2, tools2 = ask(prompt2)
product = extract_number(reply2, tools2)
if product is None:
    raise SystemExit("Could not extract a number from run 2.")
print(f"Assistant: {reply2.strip()}")

print("\n=== Calculation chain ===")
print(f"847 ÷ 7 = {quotient:g}")
print(f"{quotient:g} × {multiplier} = {product:g}")
```


```js
const base = (process.env.LANGFLOW_URL ?? process.env.LANGFLOW_SERVER_URL ?? "").replace(/\/$/, "");
const flowId = process.env.FLOW_ID ?? "67ccd2be-17f0-8190-81ff-3bb2cf6508e6";
const apiKey = process.env.LANGFLOW_API_KEY ?? "";
const sessionId = process.env.AGUI_SESSION_ID ?? "thread-123";

const NUMBER = /-?\d+(?:\.\d+)?/;

function numbersFromToolResult(raw) {
  if (raw == null) {
    return [];
  }
  if (typeof raw === "number") {
    return [String(raw)];
  }
  if (typeof raw === "string") {
    return raw.match(new RegExp(NUMBER.source, "g")) ?? [];
  }
  if (typeof raw === "object") {
    for (const key of ["content", "result", "output", "text"]) {
      const value = raw[key];
      if (value == null) {
        continue;
      }
      if (typeof value === "number") {
        return [String(value)];
      }
      const asText = typeof value === "string" ? value : JSON.stringify(value);
      const matches = asText.match(new RegExp(NUMBER.source, "g"));
      if (matches?.length) {
        return matches;
      }
    }
    const serialized = JSON.stringify(raw);
    return serialized.match(new RegExp(NUMBER.source, "g")) ?? [];
  }
  return String(raw).match(new RegExp(NUMBER.source, "g")) ?? [];
}

function extractNumber(text, toolResults) {
  for (let i = toolResults.length - 1; i >= 0; i -= 1) {
    const matches = numbersFromToolResult(toolResults[i]);
    if (matches.length) {
      return Number(matches[matches.length - 1]);
    }
  }
  const matches = text.match(new RegExp(NUMBER.source, "g"));
  return matches?.length ? Number(matches[matches.length - 1]) : null;
}

async function ask(prompt) {
  let text = "";
  const toolResults = [];

  const response = await fetch(`${base}/api/v2/workflows`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "x-api-key": apiKey,
      Accept: "text/event-stream",
    },
    body: JSON.stringify({
      flow_id: flowId,
      input_value: prompt,
      mode: "stream",
      stream_protocol: "agui",
      session_id: sessionId,
    }),
  });

  if (!response.ok) {
    throw new Error(`HTTP ${response.status}: ${await response.text()}`);
  }

  const reader = response.body.getReader();
  const decoder = new TextDecoder();
  let buffer = "";

  while (true) {
    const { done, value } = await reader.read();
    if (done) {
      break;
    }
    buffer += decoder.decode(value, { stream: true });
    const lines = buffer.split("\n");
    buffer = lines.pop() ?? "";
    for (const line of lines) {
      if (!line.startsWith("data:")) {
        continue;
      }
      const event = JSON.parse(line.slice(5).trim());
      switch (event.type) {
        case "TEXT_MESSAGE_CONTENT":
          text += event.delta ?? "";
          break;
        case "TOOL_CALL_RESULT":
          toolResults.push(event.content ?? event.result);
          break;
        case "RUN_ERROR":
          throw new Error(event.message ?? "Run failed");
        case "RUN_FINISHED":
          await reader.cancel();
          return { text, toolResults };
        default:
          break;
      }
    }
  }

  return { text, toolResults };
}

async function main() {
  const prompt1 = process.env.AGUI_PROMPT1 ?? "What is 847 divided by 7?";
  const multiplier = Number(process.env.AGUI_MULTIPLIER ?? "3");

  console.log(`User: ${prompt1}`);
  const { text: reply1, toolResults: tools1 } = await ask(prompt1);
  const quotient = extractNumber(reply1, tools1);
  if (quotient == null) {
    throw new Error("Could not extract a number from run 1.");
  }
  console.log(`Assistant: ${reply1.trim()}`);
  console.log(`Extracted: ${quotient}`);

  const prompt2 = process.env.AGUI_PROMPT2 ?? `Now multiply ${quotient} by ${multiplier}.`;
  console.log(`\nUser: ${prompt2}`);
  const { text: reply2, toolResults: tools2 } = await ask(prompt2);
  const product = extractNumber(reply2, tools2);
  if (product == null) {
    throw new Error("Could not extract a number from run 2.");
  }
  console.log(`Assistant: ${reply2.trim()}`);

  console.log("\n=== Calculation chain ===");
  console.log(`847 ÷ 7 = ${quotient}`);
  console.log(`${quotient} × ${multiplier} = ${product}`);
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
```


```bash
#!/usr/bin/env bash
# Parse AG-UI SSE frames with jq and chain two workflow runs in one session.
set -euo pipefail

BASE="${LANGFLOW_URL:-${LANGFLOW_SERVER_URL:-}}"
FLOW_ID="${FLOW_ID:-67ccd2be-17f0-8190-81ff-3bb2cf6508e6}"
API_KEY="${LANGFLOW_API_KEY:-}"
SESSION_ID="${AGUI_SESSION_ID:-thread-123}"
MULTIPLIER="${AGUI_MULTIPLIER:-3}"
PROMPT1="${AGUI_PROMPT1:-What is 847 divided by 7?}"

TEXT_FILE="$(mktemp)"
TOOLS_FILE="$(mktemp)"
trap 'rm -f "$TEXT_FILE" "$TOOLS_FILE"' EXIT

extract_number() {
  local text last=""
  text="$(cat "$TEXT_FILE")"
  while IFS= read -r line; do
    match="$(grep -oE -- '-?[0-9]+(\.[0-9]+)?' <<< "$line" | tail -n1 || true)"
    if [[ -n "$match" ]]; then
      echo "$match"
      return 0
    fi
  done < <(tac "$TOOLS_FILE" 2>/dev/null || tail -r "$TOOLS_FILE")
  while read -r num; do
    last="$num"
  done < <(grep -oE -- '-?[0-9]+(\.[0-9]+)?' <<< "$text" || true)
  if [[ -n "$last" ]]; then
    echo "$last"
  fi
}

ask() {
  local prompt="$1"
  : > "$TEXT_FILE"
  : > "$TOOLS_FILE"
  curl --fail-with-body -N -sS -X POST "${BASE}/api/v2/workflows" \
    -H "Content-Type: application/json" \
    -H "x-api-key: ${API_KEY}" \
    -d "$(jq -n \
      --arg flow_id "$FLOW_ID" \
      --arg input_value "$prompt" \
      --arg session_id "$SESSION_ID" \
      '{flow_id: $flow_id, input_value: $input_value, mode: "stream", stream_protocol: "agui", session_id: $session_id}')" \
  | while IFS= read -r line; do
      [[ "$line" == data:* ]] || continue
      json="${line#data: }"
      case "$(jq -r '.type' <<<"$json")" in
        TEXT_MESSAGE_CONTENT)
          jq -r '.delta // ""' <<<"$json" >> "$TEXT_FILE"
          ;;
        TOOL_CALL_RESULT)
          jq -r '.content // .result // ""' <<<"$json" >> "$TOOLS_FILE"
          ;;
        RUN_ERROR)
          jq -r '.message // "Run failed"' <<<"$json" >&2
          exit 1
          ;;
        RUN_FINISHED)
          break
          ;;
      esac
    done
}

echo "User: ${PROMPT1}"
ask "$PROMPT1"
QUOTIENT="$(extract_number)"
if [[ -z "${QUOTIENT:-}" ]]; then
  echo "Could not extract a number from run 1." >&2
  exit 1
fi
echo "Assistant: $(tr -d '\n' < "$TEXT_FILE")"
echo "Extracted: ${QUOTIENT}"

PROMPT2="${AGUI_PROMPT2:-Now multiply ${QUOTIENT} by ${MULTIPLIER}.}"
echo
echo "User: ${PROMPT2}"
ask "$PROMPT2"
PRODUCT="$(extract_number)"
if [[ -z "${PRODUCT:-}" ]]; then
  echo "Could not extract a number from run 2." >&2
  exit 1
fi
echo "Assistant: $(tr -d '\n' < "$TEXT_FILE")"

echo
echo "=== Calculation chain ==="
echo "847 ÷ 7 = ${QUOTIENT}"
echo "${QUOTIENT} × ${MULTIPLIER} = ${PRODUCT}"
```


## Run in the background [​](https://docs.langflow.org/workflow-api-quickstart#run-in-the-background)


Set `"mode": "background"` to queue a job and receive a `job_id` immediately. Poll `GET /api/v2/workflows?job_id=…` until `status` is `completed`, then read `output.text` from the result.


- Python
- JavaScript
- curl


```python
import os
import time

import requests

base = os.environ.get("LANGFLOW_URL") or os.environ.get("LANGFLOW_SERVER_URL", "")
flow_id = os.environ.get("FLOW_ID", "")
api_key = os.environ.get("LANGFLOW_API_KEY", "")

headers = {"Content-Type": "application/json", "x-api-key": api_key}

start = requests.post(
    f"{base}/api/v2/workflows",
    headers=headers,
    json={
        "flow_id": flow_id,
        "input_value": "Process this in the background",
        "session_id": "session-456",
        "mode": "background",
    },
    timeout=60,
)
start.raise_for_status()
job_id = start.json()["job_id"]
print(f"Queued job {job_id}")

while True:
    status = requests.get(
        f"{base}/api/v2/workflows",
        headers=headers,
        params={"job_id": job_id},
        timeout=60,
    )
    status.raise_for_status()
    body = status.json()

    if body.get("object") == "response" and body.get("status") == "completed":
        print(body["output"]["text"])
        break

    if body.get("status") in {"failed", "cancelled", "timed_out"}:
        raise SystemExit(f"Job ended with status {body.get('status')}")

    time.sleep(1)
```


```js
(async () => {
  const base = (process.env.LANGFLOW_URL ?? process.env.LANGFLOW_SERVER_URL ?? "").replace(/\/$/, "");
  const flowId = process.env.FLOW_ID ?? "";
  const apiKey = process.env.LANGFLOW_API_KEY ?? "";

  const headers = {
    "Content-Type": "application/json",
    "x-api-key": apiKey,
  };

  const start = await fetch(`${base}/api/v2/workflows`, {
    method: "POST",
    headers,
    body: JSON.stringify({
      flow_id: flowId,
      input_value: "Process this in the background",
      session_id: "session-456",
      mode: "background",
    }),
  });

  if (!start.ok) {
    throw new Error(`HTTP ${start.status}: ${await start.text()}`);
  }

  const { job_id: jobId } = await start.json();
  console.log(`Queued job ${jobId}`);

  while (true) {
    const status = await fetch(`${base}/api/v2/workflows?job_id=${encodeURIComponent(jobId)}`, {
      headers,
    });
    if (!status.ok) {
      throw new Error(`HTTP ${status.status}: ${await status.text()}`);
    }

    const body = await status.json();
    if (body.object === "response" && body.status === "completed") {
      console.log(body.output.text);
      break;
    }

    if (["failed", "cancelled", "timed_out"].includes(body.status)) {
      throw new Error(`Job ended with status ${body.status}`);
    }

    await new Promise((resolve) => setTimeout(resolve, 1000));
  }
})().catch((error) => {
  console.error(error);
  process.exit(1);
});
```


```bash
#!/usr/bin/env bash
set -euo pipefail

JOB_ID="$(
  curl --fail-with-body -sS -X POST \
    "$LANGFLOW_SERVER_URL/api/v2/workflows" \
    -H "Content-Type: application/json" \
    -H "x-api-key: $LANGFLOW_API_KEY" \
    -d '{
      "flow_id": "'"${FLOW_ID}"'",
      "input_value": "Process this in the background",
      "session_id": "session-456",
      "mode": "background"
    }' | python3 -c 'import json,sys; print(json.load(sys.stdin)["job_id"])'
)"

echo "Queued job $JOB_ID"

while true; do
  BODY="$(curl --fail-with-body -sS \
    "$LANGFLOW_SERVER_URL/api/v2/workflows?job_id=$JOB_ID" \
    -H "x-api-key: $LANGFLOW_API_KEY")"
  STATUS="$(python3 -c 'import json,sys; print(json.load(sys.stdin).get("status",""))' <<<"$BODY")"
  OBJECT="$(python3 -c 'import json,sys; print(json.load(sys.stdin).get("object",""))' <<<"$BODY")"

  if [[ "$OBJECT" == "response" && "$STATUS" == "completed" ]]; then
    python3 -c 'import json,sys; print(json.load(sys.stdin)["output"]["text"])' <<<"$BODY"
    break
  fi

  if [[ "$STATUS" == "failed" || "$STATUS" == "cancelled" || "$STATUS" == "timed_out" ]]; then
    echo "Job ended with status $STATUS" >&2
    exit 1
  fi

  sleep 1
done
```


While a job is still `queued` or `in_progress`, the poll endpoint returns a job object (`object: "job"`) with `links` for status, events, and stop. When the job completes, the same endpoint returns the full execution response.


To connect to a background run, see [Re-attach to a background run](https://docs.langflow.org/workflow-api#re-attach-to-a-background-run).


## Next steps [​](https://docs.langflow.org/workflow-api-quickstart#next-steps)


- [Workflow API reference](https://docs.langflow.org/workflow-api) — request body fields, response schemas, status polling, stop endpoint, tweaks, globals, and error codes.
- [Flow trigger endpoints](https://docs.langflow.org/api-flows-run) — v1 `/run` and `/webhook` endpoints if you are migrating from or comparing with the v1 API.


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)

- [Prerequisites](https://docs.langflow.org/workflow-api-quickstart#prerequisites)
  - [Set environment variables](https://docs.langflow.org/workflow-api-quickstart#set-environment-variables)
  - [Authentication and headers](https://docs.langflow.org/workflow-api-quickstart#authentication-and-headers)- [Run a flow synchronously](https://docs.langflow.org/workflow-api-quickstart#run-a-flow-synchronously)
- [Stream LLM tokens](https://docs.langflow.org/workflow-api-quickstart#stream-llm-tokens)
  - [Langflow EventManager (default)](https://docs.langflow.org/workflow-api-quickstart#langflow-eventmanager-default)
  - [AG-UI](https://docs.langflow.org/workflow-api-quickstart#ag-ui)- [Run in the background](https://docs.langflow.org/workflow-api-quickstart#run-in-the-background)
- [Next steps](https://docs.langflow.org/workflow-api-quickstart#next-steps)[Manage Privacy Choices](https://docs.langflow.org/workflow-api-quickstart#)

---

# Workflow API (Beta) | Langflow Documentation

`https://docs.langflow.org/workflow-api`

# Workflow API (Beta
## Prerequisites​
*For more information, see Create a Langflow API key.*

## Execute workflow endpoint​
*Description: Execute a workflow in sync, stream, or background mode.*

*Set "mode": "stream" to receive a Server-Sent Events (SSE) stream for the run.*

*Send POST /api/v2/workflows with "mode": "stream" and "stream_protocol": "agui".*

*For the full AG-UI event catalog, see the AG-UI specification.*

*Background runs honor the stream_protocol selected when the job was created.*

*The response shape depends on the selected mode.*

*sync mode returns a completed WorkflowExecutionResponse, for example:*

*Each value in outputs includes:*

## Get workflow status endpoint​
*Endpoint: GET /api/v2/workflows*

*The status values are:*

## Stop workflow endpoint​
*Endpoint: POST /api/v2/workflows/stop*

## Pass request-level global variables​
## Component tweaks​
*Use the tweaks object for one-off component parameter overrides in a single run.*

*For more information, see Tweaks (API inputs).*

## Error handling​
## See also​









The Workflow API is currently in Beta. The API endpoints and response formats may change in future releases.

Copy page ⌥C Version: 1.12.x On this page


The Workflow API provides programmatic access to execute Langflow workflows in `sync`, `stream`, or `background` modes.


The Workflow API is part of the Langflow Developer v2 API and offers enhanced workflow execution capabilities compared to the v1 `/run` endpoint.


As of Langflow version 1.11, `stream` mode supports both Langflow's built-in `EventManager` and the [AG-UI protocol](https://docs.ag-ui.com/introduction).


## Prerequisites [​](https://docs.langflow.org/workflow-api#prerequisites)


- [Install and start Langflow](https://docs.langflow.org/get-started-installation) with the developer API enabled The Workflow API endpoints require the `developer_api_enabled` setting to be enabled. If this setting is disabled, these endpoints will return a 404 Not Found error. To enable the developer API endpoint, do the following: For more information about configuring environment variables, see [Environment variables](https://docs.langflow.org/environment-variables).
  1. In the Langflow `.env` file, set the environment variable to `true`: ```text LANGFLOW_DEVELOPER_API_ENABLED=true ```
  2. Start your Langflow server with the `.env` file enabled: ```text uv run langflow run --env-file .env ```- [Create a Langflow API key](https://docs.langflow.org/api-keys-and-authentication)
- [Create a flow](https://docs.langflow.org/concepts-flows) that you want to execute
- [Get the flow ID](https://docs.langflow.org/concepts-publish#api-access) or endpoint name of the flow you want to execute


### Set environment variables [​](https://docs.langflow.org/workflow-api#set-environment-variables)


All code examples in this documentation assume you have set the following environment variables:


**Python:**


```python
import os

LANGFLOW_SERVER_URL = os.getenv("LANGFLOW_SERVER_URL")
LANGFLOW_API_KEY = os.getenv("LANGFLOW_API_KEY")
```


**TypeScript/JavaScript:**


```ts
const LANGFLOW_SERVER_URL = process.env.LANGFLOW_SERVER_URL;
const LANGFLOW_API_KEY = process.env.LANGFLOW_API_KEY;
```


Set these environment variables before running the examples, or replace the variable references in the code examples with your actual Langflow server URL and API key.


The default `LANGFLOW_SERVER_URL` for a local Langflow deployment is `http://localhost:7860`. For remote deployments, the domain is set by your hosting service, such as `https://UUID.ngrok.app`.


### Authentication and headers [​](https://docs.langflow.org/workflow-api#authentication-and-headers)


All Workflow API requests require authentication using a Langflow API key. The API key is passed in the `x-api-key` header.


For more information, see [Create a Langflow API key](https://docs.langflow.org/api-keys-and-authentication).


| Header | Description | Example |
| --- | --- | --- |
| `Content-Type` | Specifies the JSON format. | `application/json` |
| `x-api-key` | Your Langflow API key. | `sk-...` |
| `accept` | Optional. Specifies the response format. | `application/json` |


## Execute workflow endpoint [​](https://docs.langflow.org/workflow-api#execute-workflow-endpoint)


**Endpoint:**


```text
POST /api/v2/workflows
```


**Description:** Execute a workflow in `sync`, `stream`, or `background` mode.


### Request body [​](https://docs.langflow.org/workflow-api#request-body)


| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `flow_​id` | `string` | Yes | - | UUID of the flow to execute. |
| `input_​value` | `string` | No | `""` | Chat-style input for the run. |
| `mode` | `string` | No | `sync` | Execution mode: `sync`, `stream`, or `background`. |
| `stream_​protocol` | `string` | No | `langflow` | Stream adapter name used for `stream` responses and background event re-attachment. Unknown values return a `422` code for any request mode because the API validates the field against the registered adapters before execution starts. |
| `session_​id` | `string` | No | - | Scopes message memory and chat history to this session. |
| `tweaks` | `object` | No | `{}` | Per-component parameter overrides keyed by component id. See [Component tweaks](https://docs.langflow.org/workflow-api#component-tweaks). |
| `globals` | `object` | No | `{}` | Request-level global variables. Available in sync mode only. Keys are limited to 256 characters and values to 64 KB. See [Pass request-level global variables](https://docs.langflow.org/workflow-api#request-level-global-variables). |
| `output_​ids` | `array` | No | - | Output component ids to use when resolving sync-mode answers (sync mode only). |
| `data` | `object` | No | - | Live-canvas override of nodes and edges (stream and background modes only). |
| `files` | `array` | No | - | Pre-uploaded file paths to attach to the run (stream and background modes only). |
| `start_​component_​id` | `string` | No | - | Partial-run start component id (stream and background modes only). |
| `stop_​component_​id` | `string` | No | - | Partial-run stop component id (stream and background modes only). |


### Execute flow in `sync` mode [​](https://docs.langflow.org/workflow-api#execute-flow-in-sync-mode)


Set `"mode": "sync"` or omit `mode` to run inline and receive the full response when execution completes.


- Python
- JavaScript
- curl


```python
import os

import requests

base = os.environ.get("LANGFLOW_URL") or os.environ.get("LANGFLOW_SERVER_URL", "")
flow_id = os.environ.get("FLOW_ID", "")
api_key = os.environ.get("LANGFLOW_API_KEY", "")

headers = {"Content-Type": "application/json", "x-api-key": api_key}

payload = {
    "flow_id": flow_id,
    "input_value": "what is 2+2",
    "session_id": "session-123",
    "mode": "sync",
    "globals": {
        "FILENAME": "relatório—final.pdf",
        "OWNER_NAME": "José",
    },
}

response = requests.post(f"{base}/api/v2/workflows", headers=headers, json=payload, timeout=120)
response.raise_for_status()
print(response.text)
```


```js
const url = `${process.env.LANGFLOW_SERVER_URL ?? ""}/api/v2/workflows`;

const options = {
  method: 'POST',
  headers: {
    "Content-Type": `application/json`,
    "x-api-key": `${process.env.LANGFLOW_API_KEY ?? ""}`,
  },
  body: JSON.stringify({
  "flow_id": "67ccd2be-17f0-8190-81ff-3bb2cf6508e6",
  "input_value": "what is 2+2",
  "session_id": "session-123",
  "mode": "sync",
  "globals": {
    "FILENAME": "relatório—final.pdf",
    "OWNER_NAME": "José"
  }
}),
};

fetch(url, options)
  .then(async (response) => {
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    const text = await response.text();
    console.log(text);
  })
  .catch((error) => console.error(error));
```


```bash
curl -X POST \
  "$LANGFLOW_SERVER_URL/api/v2/workflows" \
  -H "Content-Type: application/json" \
  -H "x-api-key: $LANGFLOW_API_KEY" \
  -d '{
    "flow_id": "67ccd2be-17f0-8190-81ff-3bb2cf6508e6",
    "input_value": "what is 2+2",
    "session_id": "session-123",
    "mode": "sync",
    "globals": {
      "FILENAME": "relatório—final.pdf",
      "OWNER_NAME": "José"
    }
  }'
```


### Execute flow with selected `stream` mode [​](https://docs.langflow.org/workflow-api#execute-flow-with-selected-stream-mode)


Set `"mode": "stream"` to receive a Server-Sent Events (SSE) stream for the run.


`stream_protocol` is set to `langflow` by default, which emits the built-in Langflow `EventManager` output. For more information, see [Stream with Langflow EventManager](https://docs.langflow.org/workflow-api#stream-with-langflow)


Set `stream_protocol` to `agui` to emit events using the [AG-UI protocol](https://docs.ag-ui.com/introduction) instead. For more information, see [Stream with AG-UI](https://docs.langflow.org/workflow-api#stream-with-ag-ui).


If `stream_protocol` names an unknown adapter, the endpoint returns `422` with an `available` list of registered protocol names.


#### Stream with Langflow EventManager [​](https://docs.langflow.org/workflow-api#stream-with-langflow)


`stream_protocol` defaults to `langflow`, which passes through the built-in Langflow `EventManager` events. Each SSE frame has a monotonic `id:` and a `data:` line containing JSON shaped like `{"event": "<type>", "data": {...}}`. This is the same wire format the v1 build stream uses, so existing Langflow clients can read it without changes.


Omit `stream_protocol` or set it explicitly to `"langflow"`. Use `curl -N` so the client does not buffer the stream.


- Python
- JavaScript
- curl


```python
import os

import requests

base = os.environ.get("LANGFLOW_URL") or os.environ.get("LANGFLOW_SERVER_URL", "")
flow_id = os.environ.get("FLOW_ID", "67ccd2be-17f0-8190-81ff-3bb2cf6508e6")
api_key = os.environ.get("LANGFLOW_API_KEY", "")

headers = {"Content-Type": "application/json", "x-api-key": api_key}

payload = {
    "flow_id": flow_id,
    "input_value": "Hello from a Langflow stream client",
    "mode": "stream",
    "session_id": "session-123",
}

with requests.post(
    f"{base}/api/v2/workflows",
    headers=headers,
    json=payload,
    stream=True,
    timeout=120,
) as response:
    response.raise_for_status()
    for line in response.iter_lines(decode_unicode=True):
        if line:
            print(line)
```


```js
const url = `${process.env.LANGFLOW_SERVER_URL ?? ""}/api/v2/workflows`;

const options = {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": `${process.env.LANGFLOW_API_KEY ?? ""}`,
  },
  body: JSON.stringify({
    flow_id: "67ccd2be-17f0-8190-81ff-3bb2cf6508e6",
    input_value: "Hello from a Langflow stream client",
    mode: "stream",
    session_id: "session-123",
  }),
};

(async () => {
  const response = await fetch(url, options);
  if (!response.ok) {
    throw new Error(`HTTP ${response.status}`);
  }

  const reader = response.body.getReader();
  const decoder = new TextDecoder();

  while (true) {
    const { done, value } = await reader.read();
    if (done) {
      break;
    }
    process.stdout.write(decoder.decode(value, { stream: true }));
  }
  process.stdout.write(decoder.decode());
})().catch((error) => console.error(error));
```


```bash
curl -N -X POST \
  "$LANGFLOW_SERVER_URL/api/v2/workflows" \
  -H "Content-Type: application/json" \
  -H "x-api-key: $LANGFLOW_API_KEY" \
  -d '{
    "flow_id": "67ccd2be-17f0-8190-81ff-3bb2cf6508e6",
    "input_value": "Hello from a Langflow stream client",
    "mode": "stream",
    "session_id": "session-123"
  }'
```


**Common EventManager event types:**


| Event | Purpose |
| --- | --- |
| `vertices_​sorted` | Execution order for the flow's components. |
| `add_​message` | Chat message added (user or assistant). |
| `token` | Streaming LLM token chunk (`data.chunk`). |
| `end_​vertex` | A component finished building. |
| `output` | Normalized terminal component output (same shape as sync-mode `outputs`). |
| `end` | Run finished successfully. |
| `error` | Run failed (`data.error`). |
| `cancelled` | Run stopped by the client. |


For more examples of `token` and `add_message` events, see [Stream LLM token responses](https://docs.langflow.org/api-flows-run#stream-llm-token-responses).


#### Stream with AG-UI [​](https://docs.langflow.org/workflow-api#stream-with-ag-ui)


Stream with the [AG-UI protocol](https://docs.ag-ui.com/introduction) when your client expects agent lifecycle events such as `RUN_STARTED` and `TEXT_MESSAGE_*` instead of Langflow's internal events. Read responses as an SSE stream. Each `data:` line contains one AG-UI event serialized as JSON. Close flow runs when you receive `RUN_FINISHED`, or handle failures on `RUN_ERROR`.


Send `POST /api/v2/workflows` with `"mode": "stream"` and `"stream_protocol": "agui"`.


- Python
- JavaScript
- curl


```python
import os

import requests

base = os.environ.get("LANGFLOW_URL") or os.environ.get("LANGFLOW_SERVER_URL", "")
flow_id = os.environ.get("FLOW_ID", "67ccd2be-17f0-8190-81ff-3bb2cf6508e6")
api_key = os.environ.get("LANGFLOW_API_KEY", "")

headers = {"Content-Type": "application/json", "x-api-key": api_key}

payload = {
    "flow_id": flow_id,
    "input_value": "Hello from an AG-UI client",
    "mode": "stream",
    "stream_protocol": "agui",
    "session_id": "thread-123",
}

with requests.post(
    f"{base}/api/v2/workflows",
    headers=headers,
    json=payload,
    stream=True,
    timeout=120,
) as response:
    response.raise_for_status()
    for line in response.iter_lines(decode_unicode=True):
        if line:
            print(line)
```


```js
const url = `${process.env.LANGFLOW_SERVER_URL ?? ""}/api/v2/workflows`;

const options = {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": `${process.env.LANGFLOW_API_KEY ?? ""}`,
  },
  body: JSON.stringify({
    flow_id: "67ccd2be-17f0-8190-81ff-3bb2cf6508e6",
    input_value: "Hello from an AG-UI client",
    mode: "stream",
    stream_protocol: "agui",
    session_id: "thread-123",
  }),
};

(async () => {
  const response = await fetch(url, options);
  if (!response.ok) {
    throw new Error(`HTTP ${response.status}`);
  }

  const reader = response.body.getReader();
  const decoder = new TextDecoder();

  while (true) {
    const { done, value } = await reader.read();
    if (done) {
      break;
    }
    process.stdout.write(decoder.decode(value, { stream: true }));
  }
  process.stdout.write(decoder.decode());
})().catch((error) => console.error(error));
```


```bash
curl -N -X POST \
  "$LANGFLOW_SERVER_URL/api/v2/workflows" \
  -H "Content-Type: application/json" \
  -H "x-api-key: $LANGFLOW_API_KEY" \
  -d '{
    "flow_id": "67ccd2be-17f0-8190-81ff-3bb2cf6508e6",
    "input_value": "Hello from an AG-UI client",
    "mode": "stream",
    "stream_protocol": "agui",
    "session_id": "thread-123"
  }'
```


**Common AG-UI event types:**


| Event type | Purpose |
| --- | --- |
| `RUN_​STARTED` / `RUN_​FINISHED` / `RUN_​ERROR` | Run lifecycle. |
| `TEXT_​MESSAGE_​START` / `TEXT_​MESSAGE_​CONTENT` / `TEXT_​MESSAGE_​END` | Streaming assistant text. |
| `TOOL_​CALL_​START` / `TOOL_​CALL_​ARGS` / `TOOL_​CALL_​END` / `TOOL_​CALL_​RESULT` | Tool invocation lifecycle. |
| `STEP_​STARTED` / `STEP_​FINISHED` | Per-component execution steps. |
| `STATE_​SNAPSHOT` / `STATE_​DELTA` | Node graph state (status and output). |
| `CUSTOM` | Langflow-specific extensions (see below). |


Langflow also emits `CUSTOM` events that generic AG-UI clients can ignore, such as `langflow.log`, `langflow.content.*`, `langflow.message.removed`, and `langflow.run.cancelled`.


For the full AG-UI event catalog, see the [AG-UI specification](https://docs.ag-ui.com/concepts/architecture).


For a longer client example that parses AG-UI frames and chains two runs in one `session_id`, see `example-stream-agui-parse.py` (and matching `.js` / `.sh` files) under [`docs/docs/API-Reference/`](https://github.com/langflow-ai/langflow/tree/main/docs/docs/API-Reference).


### Execute flow in `background` mode [​](https://docs.langflow.org/workflow-api#execute-flow-in-background-mode)


Set `"mode": "background"` to queue a job and receive a `job_id` immediately. Poll [GET /api/v2/workflows](https://docs.langflow.org/workflow-api#get-workflow-status-endpoint) for status and results, [re-attach to the event stream](https://docs.langflow.org/workflow-api#re-attach-to-a-background-run) with `GET /api/v2/workflows/{job_id}/events`, or stop the job with [POST /api/v2/workflows/stop](https://docs.langflow.org/workflow-api#stop-workflow-endpoint).


Background runs honor the `stream_protocol` selected when the job was created.


- Python
- JavaScript
- curl


```python
import os

import requests

base = os.environ.get("LANGFLOW_URL") or os.environ.get("LANGFLOW_SERVER_URL", "")
flow_id = os.environ.get("FLOW_ID", "")
api_key = os.environ.get("LANGFLOW_API_KEY", "")

headers = {"Content-Type": "application/json", "x-api-key": api_key}

payload = {
    "flow_id": flow_id,
    "input_value": "Process this in the background",
    "session_id": "session-456",
    "mode": "background",
}

response = requests.post(f"{base}/api/v2/workflows", headers=headers, json=payload, timeout=60)
response.raise_for_status()
print(response.text)
```


```js
const url = `${process.env.LANGFLOW_SERVER_URL ?? ""}/api/v2/workflows`;

const options = {
  method: 'POST',
  headers: {
    "Content-Type": `application/json`,
    "x-api-key": `${process.env.LANGFLOW_API_KEY ?? ""}`,
  },
  body: JSON.stringify({
  "flow_id": "67ccd2be-17f0-8190-81ff-3bb2cf6508e6",
  "input_value": "Process this in the background",
  "session_id": "session-456",
  "mode": "background"
}),
};

fetch(url, options)
  .then(async (response) => {
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    const text = await response.text();
    console.log(text);
  })
  .catch((error) => console.error(error));
```


```bash
curl -X POST \
  "$LANGFLOW_SERVER_URL/api/v2/workflows" \
  -H "Content-Type: application/json" \
  -H "x-api-key: $LANGFLOW_API_KEY" \
  -d '{
    "flow_id": "67ccd2be-17f0-8190-81ff-3bb2cf6508e6",
    "input_value": "Process this in the background",
    "session_id": "session-456",
    "mode": "background"
  }'
```


See [Background response fields](https://docs.langflow.org/workflow-api#background-response-fields) in [Response body](https://docs.langflow.org/workflow-api#response-body) for the job object returned when you queue a background run.


#### Re-attach to a background run [​](https://docs.langflow.org/workflow-api#re-attach-to-a-background-run)


**Endpoint:** `GET /api/v2/workflows/{job_id}/events` (also returned as `links.events` on the background job response)


You can replay buffered SSE events from a background run and tail the stream until the job finishes.


Each SSE frame includes an `id:` line. Pass the last `id` value you received in a `Last-Event-ID` header to resume from the next event.


```python
headers = {
    "x-api-key": api_key,
    "Accept": "text/event-stream",
    "Last-Event-ID": last_event_id,
}
```


### Response body [​](https://docs.langflow.org/workflow-api#response-body)


The response shape depends on the selected `mode`.


`stream` mode returns Server Sent Events. For more information, see [Execute flow with selected `stream` mode](https://docs.langflow.org/workflow-api#execute-flow-with-selected-stream-mode).


`sync` mode returns a completed `WorkflowExecutionResponse`, for example:


```json
{
  "flow_id": "67ccd2be-17f0-8190-81ff-3bb2cf6508e6",
  "session_id": "session-123",
  "job_id": "a98d9753-9259-47ca-9783-69a9d8d26889",
  "object": "response",
  "created_timestamp": "2026-06-30T16:00:56.917538+00:00",
  "status": "completed",
  "output": {
    "reason": "single",
    "text": "2 + 2 equals 4.",
    "source": "ChatOutput-xyz"
  },
  "has_errors": false,
  "errors": [],
  "inputs": {},
  "globals": {
    "FILENAME": "relatório—final.pdf",
    "OWNER_NAME": "José"
  },
  "outputs": {
    "ChatOutput-xyz": {
      "type": "message",
      "status": "completed",
      "display_name": "Chat Output",
      "content": "2 + 2 equals 4."
    }
  }
}
```


#### Sync response fields [​](https://docs.langflow.org/workflow-api#sync-response-fields)


| Field | Description |
| --- | --- |
| `output` | Primary text answer for the run. |
| `output.reason` | Why `output.text` was or wasn't populated: `single`, `multiple`, `none`, `non_​string`, or `failed`. |
| `output.text` | The answer when `output.reason` is `single`; otherwise `null`. |
| `output.source` | Component id that produced `output.text` when `output.reason` is `single`. |
| `outputs` | Map of component id → component result. |
| `has_​errors` | `true` when `errors` is non-empty. |
| `created_​timestamp` | ISO-8601 UTC timestamp (not a Unix epoch). |
| `session_​id` | Session used for the run; pass it on the next request to continue the same chat history. |


Each value in `outputs` includes:


| Field | Description |
| --- | --- |
| `type` | Content type (`message`, `image`, `sql`, `data`, `file`, etc.). |
| `status` | Component run status (`completed`, `failed`, …). |
| `display_​name` | Human-readable component name. |
| `content` | Component payload. |
| `metadata` | Optional extra metadata for the component output. |


#### Background response fields [​](https://docs.langflow.org/workflow-api#background-response-fields)


`background` mode returns a job object immediately (`object: "job"`). Poll [GET /api/v2/workflows](https://docs.langflow.org/workflow-api#get-workflow-status-endpoint) until the job completes; the completed result uses the same `WorkflowExecutionResponse` shape as sync mode (see the example above).


```json
{
  "job_id": "a98d9753-9259-47ca-9783-69a9d8d26889",
  "flow_id": "67ccd2be-17f0-8190-81ff-3bb2cf6508e6",
  "object": "job",
  "created_timestamp": "2026-06-30T16:00:56.917538+00:00",
  "status": "queued",
  "links": {
    "status": "/api/v2/workflows?job_id=a98d9753-9259-47ca-9783-69a9d8d26889",
    "events": "/api/v2/workflows/a98d9753-9259-47ca-9783-69a9d8d26889/events",
    "stop": "/api/v2/workflows/stop"
  },
  "errors": [],
  "globals": {}
}
```


| Field | Description |
| --- | --- |
| `object` | Always `"job"`. |
| `job_​id` | UUID for polling, re-attaching to events, and stop requests. |
| `links.status` | `GET /api/v2/workflows?job_​id=…` |
| `links.events` | `GET /api/v2/workflows/{job_​id}/events` |
| `links.stop` | `POST /api/v2/workflows/stop` |


## Get workflow status endpoint [​](https://docs.langflow.org/workflow-api#get-workflow-status-endpoint)


**Endpoint:** `GET /api/v2/workflows`


**Description:** Retrieve the status and results of a workflow execution by job ID.


### Example request [​](https://docs.langflow.org/workflow-api#example-request)


- Python
- JavaScript
- curl


```python
import os

import requests

base = os.environ.get("LANGFLOW_URL") or os.environ.get("LANGFLOW_SERVER_URL", "")
flow_id = os.environ.get("FLOW_ID", "")
api_key = os.environ.get("LANGFLOW_API_KEY", "")

headers = {"Content-Type": "application/json", "x-api-key": api_key}

start = requests.post(
    f"{base}/api/v2/workflows",
    headers=headers,
    json={
        "flow_id": flow_id,
        "input_value": "Process this in the background",
        "mode": "background",
    },
    timeout=60,
)
start.raise_for_status()
print(start.text)
```


```js
const url = `${process.env.LANGFLOW_SERVER_URL ?? ""}/api/v2/workflows?job_id=job_id_1234567890`;

const options = {
  method: 'GET',
  headers: {
    "accept": `application/json`,
    "x-api-key": `${process.env.LANGFLOW_API_KEY ?? ""}`,
  },
};

fetch(url, options)
  .then(async (response) => {
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    const text = await response.text();
    console.log(text);
  })
  .catch((error) => console.error(error));
```


```bash
curl -X GET \
  "$LANGFLOW_SERVER_URL/api/v2/workflows?job_id=job_id_1234567890" \
  -H "accept: application/json" \
  -H "x-api-key: $LANGFLOW_API_KEY"
```


### Query parameters [​](https://docs.langflow.org/workflow-api#query-parameters)


| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `job_​id` | `string` | Yes | The job ID returned from a workflow execution. |


### Example response [​](https://docs.langflow.org/workflow-api#example-response)


```json
{
  "flow_id": "67ccd2be-17f0-8190-81ff-3bb2cf6508e6",
  "session_id": "session-123",
  "job_id": "a98d9753-9259-47ca-9783-69a9d8d26889",
  "object": "response",
  "created_timestamp": "2026-06-30T16:00:56.917538+00:00",
  "status": "completed",
  "output": {
    "reason": "single",
    "text": "Processing complete...",
    "source": "ChatOutput-xyz"
  },
  "has_errors": false,
  "errors": [],
  "inputs": {},
  "globals": {},
  "outputs": {
    "ChatOutput-xyz": {
      "type": "message",
      "status": "completed",
      "display_name": "Chat Output",
      "content": "Processing complete..."
    }
  }
}
```


### Response body [​](https://docs.langflow.org/workflow-api#response-body)


Returns one of two JSON schemas depending on job state:


| Job state | Response | Notes |
| --- | --- | --- |
| `queued`, `in_​progress`, `cancelled` | `WorkflowJobResponse` | Same shape as a background job create response (`object: "job"`, `links`, …). |
| `completed` | `WorkflowExecutionResponse` | Full results (example above). |
| `failed` | HTTP `500` | Error detail in the response body; not a workflow result object. |
| `timed_​out` | HTTP `408` | Error detail in the response body. |


When the job is still active, poll `GET /api/v2/workflows?job_id=…` or re-attach to [events](https://docs.langflow.org/workflow-api#re-attach-to-a-background-run) for live output.


The `status` values are:


| Status | Description |
| --- | --- |
| `queued` | Job is queued and waiting to start. |
| `in_​progress` | Job is currently executing. |
| `suspended` | Job is paused and waiting for human input. See [Human-in-the-Loop](https://docs.langflow.org/human-in-the-loop). |
| `completed` | Job completed successfully. |
| `failed` | Job failed during execution. |
| `cancelled` | Job was stopped by the client. |
| `timed_​out` | Job exceeded the execution timeout. |


## Stop workflow endpoint [​](https://docs.langflow.org/workflow-api#stop-workflow-endpoint)


**Endpoint:** `POST /api/v2/workflows/stop`


**Description:** Stop a running workflow execution by job ID.


### Example request [​](https://docs.langflow.org/workflow-api#example-request-1)


- Python
- JavaScript
- curl


```python
import os

import requests

base = os.environ.get("LANGFLOW_URL") or os.environ.get("LANGFLOW_SERVER_URL", "")
flow_id = os.environ.get("FLOW_ID", "")
api_key = os.environ.get("LANGFLOW_API_KEY", "")

headers = {"Content-Type": "application/json", "x-api-key": api_key}

start = requests.post(
    f"{base}/api/v2/workflows",
    headers=headers,
    json={
        "flow_id": flow_id,
        "input_value": "Process this in the background",
        "mode": "background",
    },
    timeout=60,
)
start.raise_for_status()
job_id = start.json()["job_id"]

stop = requests.post(
    f"{base}/api/v2/workflows/stop",
    headers=headers,
    json={"job_id": job_id},
    timeout=60,
)
print(stop.status_code, stop.text)
```


```js
const url = `${process.env.LANGFLOW_SERVER_URL ?? ""}/api/v2/workflows/stop`;

const options = {
  method: 'POST',
  headers: {
    "Content-Type": `application/json`,
    "x-api-key": `${process.env.LANGFLOW_API_KEY ?? ""}`,
  },
  body: JSON.stringify({
  "job_id": "job_id_1234567890"
}),
};

fetch(url, options)
  .then(async (response) => {
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    const text = await response.text();
    console.log(text);
  })
  .catch((error) => console.error(error));
```


```bash
curl -X POST \
  "$LANGFLOW_SERVER_URL/api/v2/workflows/stop" \
  -H "Content-Type: application/json" \
  -H "x-api-key: $LANGFLOW_API_KEY" \
  -d '{
    "job_id": "job_id_1234567890"
  }'
```


### Request body [​](https://docs.langflow.org/workflow-api#request-body-1)


| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `job_​id` | `string` | Yes | - | The job ID of the workflow to stop. |


### Example response [​](https://docs.langflow.org/workflow-api#example-response-1)


```json
{
  "job_id": "job_id_1234567890",
  "message": "Job job_id_1234567890 cancelled successfully."
}
```


## Pass request-level global variables [​](https://docs.langflow.org/workflow-api#request-level-global-variables)


Pass request-scoped variables in the `globals` JSON field. They are available to workflow components for the duration of the run.


Use `globals` when values are large, shared across runs, or would exceed HTTP header size limits. [Tweaks](https://docs.langflow.org/workflow-api#component-tweaks) are better suited for one-off component overrides. `globals` is keyed by variable name and not component ID, so it stays stable when the UI regenerates node IDs when importing flows.


`globals` is honored in **sync mode only**; stream and background runs ignore it. The Workflow API is in **Beta**, and this transport may continue to evolve.


### Use a stable name in the UI and then pass it in `globals` [​](https://docs.langflow.org/workflow-api#use-a-stable-name-in-the-ui-and-then-pass-it-in-globals)


To avoid depending on changing component IDs, rename a component, create a matching global variable, bind the field, and pass the value in the request.


1. To rename the component in the UI, click **Edit**, and then rename the component. This example uses `CUSTOMER_PROMPT`.
2. Save the flow.
3. Create a new global variable with the same name as the component, such as `CUSTOMER_PROMPT`, and save it. For more about creating global variables, see [Global variables](https://docs.langflow.org/configuration-global-variables).
4. In the field you want to fill at runtime, click the **Globe** icon, select `CUSTOMER_PROMPT`, and save the flow.
5. Call the v2 Workflow API in sync mode and pass the value in `globals`.


```bash
curl -X POST "http://localhost:7860/api/v2/workflows" \
  -H "Content-Type: application/json" \
  -H "x-api-key: YOUR_API_KEY" \
  -d '{
    "flow_id": "YOUR_FLOW_ID",
    "mode": "sync",
    "input_value": "hello",
    "globals": {
      "CUSTOMER_PROMPT": "The prompt with many words..."
    }
  }'
```


## Component tweaks [​](https://docs.langflow.org/workflow-api#component-tweaks)


Use the `tweaks` object for one-off component parameter overrides in a single run.


```json
{
  "flow_id": "67ccd2be-17f0-8190-81ff-3bb2cf6508e6",
  "input_value": "what is 2+2",
  "tweaks": {
    "LLMComponent-123": {
      "temperature": 0.7,
      "max_tokens": 100
    }
  }
}
```


For more information, see [Tweaks (API inputs)](https://docs.langflow.org/concepts-publish#input-schema).


## Error handling [​](https://docs.langflow.org/workflow-api#error-handling)


The API uses standard HTTP status codes to indicate success or failure:


| Status Code | Description |
| --- | --- |
| `200 OK` | Request successful. |
| `400 Bad Request` | Invalid request parameters. |
| `403 Forbidden` | Invalid or missing API key. |
| `404 Not Found` | Flow not found or developer API disabled. |
| `422 Unprocessable Entity` | Unknown `stream_​protocol`, unsupported field for the selected mode, or refused `tweaks` with `TWEAKS_​REFUSED`. |
| `500 Internal Server Error` | Server error during execution. |
| `501 Not Implemented` | Endpoint not yet implemented. |


### Error response format [​](https://docs.langflow.org/workflow-api#error-response-format)


```json
{
  "detail": "Error message describing what went wrong"
}
```


For an unknown `stream_protocol`, the `422` response includes an `available` list of registered protocol names (`langflow`, `agui`).


For a refused tweak, `detail` is an object with `code` `TWEAKS_REFUSED`. See [Refused tweaks with `TWEAKS_REFUSED`](https://docs.langflow.org/deployment-tweaks-policy#tweaks-refused).


## See also [​](https://docs.langflow.org/workflow-api#see-also)


- [Workflow API quickstart](https://docs.langflow.org/workflow-api-quickstart) — run a flow in sync, stream, and background modes with copy-paste examples.


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)

- [Prerequisites](https://docs.langflow.org/workflow-api#prerequisites)
  - [Set environment variables](https://docs.langflow.org/workflow-api#set-environment-variables)
  - [Authentication and headers](https://docs.langflow.org/workflow-api#authentication-and-headers)- [Execute workflow endpoint](https://docs.langflow.org/workflow-api#execute-workflow-endpoint)
  - [Request body](https://docs.langflow.org/workflow-api#request-body)
  - [Execute flow in `sync` mode](https://docs.langflow.org/workflow-api#execute-flow-in-sync-mode)
  - [Execute flow with selected `stream` mode](https://docs.langflow.org/workflow-api#execute-flow-with-selected-stream-mode)
  - [Execute flow in `background` mode](https://docs.langflow.org/workflow-api#execute-flow-in-background-mode)
  - [Response body](https://docs.langflow.org/workflow-api#response-body)- [Get workflow status endpoint](https://docs.langflow.org/workflow-api#get-workflow-status-endpoint)
  - [Example request](https://docs.langflow.org/workflow-api#example-request)
  - [Query parameters](https://docs.langflow.org/workflow-api#query-parameters)
  - [Example response](https://docs.langflow.org/workflow-api#example-response)
  - [Response body](https://docs.langflow.org/workflow-api#response-body)- [Stop workflow endpoint](https://docs.langflow.org/workflow-api#stop-workflow-endpoint)
  - [Example request](https://docs.langflow.org/workflow-api#example-request-1)
  - [Request body](https://docs.langflow.org/workflow-api#request-body-1)
  - [Example response](https://docs.langflow.org/workflow-api#example-response-1)- [Pass request-level global variables](https://docs.langflow.org/workflow-api#request-level-global-variables)
  - [Use a stable name in the UI and then pass it in `globals`](https://docs.langflow.org/workflow-api#use-a-stable-name-in-the-ui-and-then-pass-it-in-globals)- [Component tweaks](https://docs.langflow.org/workflow-api#component-tweaks)
- [Error handling](https://docs.langflow.org/workflow-api#error-handling)
  - [Error response format](https://docs.langflow.org/workflow-api#error-response-format)- [See also](https://docs.langflow.org/workflow-api#see-also)[Manage Privacy Choices](https://docs.langflow.org/workflow-api#)

---

# Restrict API tweaks | Langflow Documentation

`https://docs.langflow.org/deployment-tweaks-policy`

# Restrict API tweaks
*To limit what callers can override, set the following environment variable:*

## Choose a policy​
*To mark fields that declared should allow, see Tweaks (API inputs).*

## Refused tweaks with TWEAKS_REFUSED​



When an application runs a flow through the Langflow API, the request can include tweaks, one-time overrides of component settings for that run.

Copy page ⌥C Version: 1.12.x On this page

When an application runs a flow through the Langflow API, the request can include `tweaks`, one-time overrides of component settings for that run.


By default, a caller can change almost any field, not only the fields marked **API** in the Langflow visual editor. The **API** button adds marked fields to the generated code snippets, but it does not stop the server from accepting other tweaks.


To limit what callers can override, set the following [environment variable](https://docs.langflow.org/environment-variables):


```bash
LANGFLOW_TWEAKS_POLICY=declared
```


Existing servers keep the default `permissive` behavior until you set this variable.


## Choose a policy [​](https://docs.langflow.org/deployment-tweaks-policy#choose-a-policy)


| Value | When to use it | What callers can change |
| --- | --- | --- |
| `permissive` (default) | Trusted callers, local development | Almost any component field. Code fields and other privileged settings stay blocked. |
| `declared` | Production APIs where you choose the knobs | Only fields marked **API** on a flow. If a flow marks none, it behaves like `permissive` so unpublished flows continue working. |
| `off` | Run-only serving | Nothing. Callers can still send the chat input (`input_​value`) and `session_​id`. |


This policy applies to API callers, not values Langflow passes internally. A **Run Flow** component can still feed a sub-flow under `off`.


MCP tools that only accept a prompt still work under `off`. Additional MCP fields are tweaks, so they are refused. Use `permissive` or `declared` for tools with additional MCP fields.


This setting does not hide components from the palette or block model providers. For those controls, see [Catalog and model policy](https://docs.langflow.org/api-governance-policy).


To mark fields that `declared` should allow, see [Tweaks (API inputs)](https://docs.langflow.org/concepts-publish#input-schema).


## Refused tweaks with `TWEAKS_REFUSED` [​](https://docs.langflow.org/deployment-tweaks-policy#tweaks-refused)


A refused tweak fails the run with `422 Unprocessable Entity`. The extra keys are not applied. `input_value` and `session_id` are not tweaks, so both values are still accepted.


```json
{
  "detail": {
    "error": "Refused tweaks",
    "code": "TWEAKS_REFUSED",
    "message": "This flow declares which fields the API may set. Only fields marked editable via API accept a tweak.",
    "fields": ["temperature"]
  }
}
```


Returned from `POST /api/v1/run`, `/run/advanced`, `/build/{flow_id}/flow`, and `/api/v2/workflows`.


For more information, see:


- [Environment variables](https://docs.langflow.org/environment-variables#visual-editor-and-playground-behavior)
- [Component hardening for untrusted users](https://docs.langflow.org/api-keys-and-authentication#multi-tenant-component-hardening)
- [Security](https://docs.langflow.org/security)


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)

- [Choose a policy](https://docs.langflow.org/deployment-tweaks-policy#choose-a-policy)
- [Refused tweaks with `TWEAKS_REFUSED`](https://docs.langflow.org/deployment-tweaks-policy#tweaks-refused)[Manage Privacy Choices](https://docs.langflow.org/deployment-tweaks-policy#)

---

# OpenAI Responses API | Langflow Documentation

`https://docs.langflow.org/api-openai-responses`

Copy page ⌥C Version: 1.12.x On this page

Langflow includes an endpoint that is compatible with the [OpenAI Responses API](https://platform.openai.com/docs/api-reference/responses). It is available at `POST /api/v1/responses`.


This endpoint allows you to use existing OpenAI client libraries with minimal code changes. You only need to replace the `model` name, such as `gpt-4`, with your `flow_id`. You can find Flow IDs in the code snippets on the [**API access** pane](https://docs.langflow.org/concepts-publish#api-access) or in a flow's URL.


## Prerequisites [​](https://docs.langflow.org/api-openai-responses#prerequisites)
## Prerequisites​
## Example request​
## Example response​
## Example streaming request​
## Continue conversations with response and session IDs​
*Optionally, you can use your own session ID values for the previous_response_id:*

## Retrieve tool call results​
*The response now includes the tool call's results.
For example:*

## Pass global variables to your flows in headers​
## Token usage tracking​










To be compatible with Langflow's OpenAI Responses API endpoint, your flow and request must adhere to the following requirements:


- **Chat Input**: Your flow must contain a **Chat Input** component. Flows without this component return an error when passed to this endpoint. The component types `ChatInput` and `Chat Input` are recognized as chat inputs.
- **Tools**: The `tools` parameter isn't supported, and returns an error if provided.
- **Model Names**: In your request, the `model` field must contain a valid flow ID or endpoint name.
- **Authentication**: All requests require an API key passed in the `x-api-key` header. For more information, see [API keys and authentication](https://docs.langflow.org/api-keys-and-authentication).


### Additional configuration for OpenAI client libraries [​](https://docs.langflow.org/api-openai-responses#additional-configuration-for-openai-client-libraries)


This endpoint is compatible with OpenAI's API, but requires special configuration when using OpenAI client libraries. Langflow uses `x-api-key` headers for authentication, while OpenAI uses `Authorization: Bearer` headers. When sending requests to Langflow with OpenAI client libraries, you must configure custom headers and include an `api_key` configuration. The `api_key` parameter can have any value, such as `"dummy-api-key"` in the client examples, as the actual authentication is handled through the `default_headers` configuration.


In the following examples, replace the values for `LANGFLOW_SERVER_URL`, `LANGFLOW_API_KEY`, and `FLOW_ID` with values from your deployment.


- OpenAI Python Client
- OpenAI TypeScript Client


```python
import os

from openai import OpenAI

base = (os.environ.get("LANGFLOW_URL") or os.environ.get("LANGFLOW_SERVER_URL", "")).rstrip("/")
api_key = os.environ.get("LANGFLOW_API_KEY", "")
flow_id = os.environ.get("FLOW_ID", "")

client = OpenAI(
    base_url=f"{base}/api/v1/",
    default_headers={"x-api-key": api_key},
    api_key="dummy-api-key",  # Required by OpenAI SDK but not used by Langflow
)

try:
    response = client.responses.create(
        model=flow_id,
        input="There is an event that happens on the second wednesday of every month. What are the event dates in 2026?",
    )
except Exception as exc:
    # Empty bootstrap flows return an error body; use a flow with ChatInput + ChatOutput in the UI.
    print(exc)
else:
    try:
        print(response.output_text)
    except Exception:
        print(response)
```


```js
import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "LANGFLOW_SERVER_URL/api/v1/",
  defaultHeaders: {
    "x-api-key": "LANGFLOW_API_KEY"
  },
  apiKey: "dummy-api-key" // Required by OpenAI SDK but not used by Langflow
});

const response = await client.responses.create({
  model: "FLOW_ID",
  input: "There is an event that happens on the second wednesday of every month. What are the event dates in 2026?"
});

console.log(response.output_text);
```


## Example request [​](https://docs.langflow.org/api-openai-responses#example-request)


- Python
- JavaScript
- curl


```python
import os

import requests

url = f"{os.getenv('LANGFLOW_SERVER_URL', '')}/api/v1/responses"

headers = {
    "x-api-key": f"{os.getenv('LANGFLOW_API_KEY', '')}",
    "Content-Type": "application/json",
}

payload = {"model": "$YOUR_FLOW_ID", "input": "Hello, how are you?", "stream": False}

response = requests.request("POST", url, headers=headers, json=payload)
response.raise_for_status()

print(response.text)
```


```js
const url = `${process.env.LANGFLOW_SERVER_URL ?? ""}/api/v1/responses`;

const options = {
  method: 'POST',
  headers: {
    "x-api-key": `${process.env.LANGFLOW_API_KEY ?? ""}`,
    "Content-Type": `application/json`,
  },
  body: JSON.stringify({
  "model": "$YOUR_FLOW_ID",
  "input": "Hello, how are you?",
  "stream": false
}),
};

fetch(url, options)
  .then(async (response) => {
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    const text = await response.text();
    console.log(text);
  })
  .catch((error) => console.error(error));
```


```bash
curl -X POST \
  "$LANGFLOW_SERVER_URL/api/v1/responses" \
  -H "x-api-key: $LANGFLOW_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "$YOUR_FLOW_ID",
    "input": "Hello, how are you?",
    "stream": false
  }'
```


### Headers [​](https://docs.langflow.org/api-openai-responses#headers)


| Header | Required | Description | Example |
| --- | --- | --- | --- |
| `x-api-key` | Yes | Your Langflow API key for authentication | `"sk-..."` |
| `Content-Type` | Yes | Specifies the JSON format | `"application/json"` |
| `X-LANGFLOW-GLOBAL-VAR-*` | No | Global variables for the flow | `"X-LANGFLOW-GLOBAL-VAR-API_​KEY: sk-..."` For more, see [Pass global variables to your flows in headers](https://docs.langflow.org/api-openai-responses#global-var). |


### Request body [​](https://docs.langflow.org/api-openai-responses#request-body)


| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `model` | `string` | Yes | - | The flow ID or endpoint name to execute. |
| `input` | `string` | Yes | - | The input text to process. |
| `stream` | `boolean` | No | `false` | Whether to stream the response. |
| `background` | `boolean` | No | `false` | Whether to process in background. |
| `tools` | `list[Any]` | No | `null` | Tools are not supported yet. |
| `previous_​response_​id` | `string` | No | `null` | ID of previous response to continue conversation. For more, see [Continue conversations with response and session IDs](https://docs.langflow.org/api-openai-responses#response-id). |
| `include` | `list[string]` | No | `null` | Additional response data to include, such as `['tool_​call.results']`. For more, see [Retrieve tool call results](https://docs.langflow.org/api-openai-responses#tool-call-results). |


## Example response [​](https://docs.langflow.org/api-openai-responses#example-response)


```json
{
  "id": "e5e8ef8a-7efd-4090-a110-6aca082bceb7",
  "object": "response",
  "created_at": 1756837941,
  "status": "completed",
  "model": "ced2ec91-f325-4bf0-8754-f3198c2b1563",
  "output": [
    {
      "type": "message",
      "id": "msg_e5e8ef8a-7efd-4090-a110-6aca082bceb7",
      "status": "completed",
      "role": "assistant",
      "content": [
        {
          "type": "output_text",
          "text": "Hello! I'm here and ready to help. How can I assist you today?",
          "annotations": []
        }
      ]
    }
  ],
  "parallel_tool_calls": true,
  "previous_response_id": null,
  "reasoning": {"effort": null, "summary": null},
  "store": true,
  "temperature": 1.0,
  "text": {"format": {"type": "text"}},
  "tool_choice": "auto",
  "tools": [],
  "top_p": 1.0,
  "truncation": "disabled",
  "usage": null,
  "user": null,
  "metadata": {}
}
```


### Response body [​](https://docs.langflow.org/api-openai-responses#response-body)


The response contains fields that Langflow sets dynamically and fields that use OpenAI-compatible defaults.


The OpenAI-compatible default values shown above are currently fixed and cannot be modified via the request. They are included to maintain API compatibility and provide a consistent response format.


For your requests, you will only be setting the dynamic fields. The default values are documented here for completeness and to show the full response structure.


Fields set dynamically by Langflow:


| Field | Type | Description |
| --- | --- | --- |
| `id` | `string` | Unique response identifier. |
| `created_​at` | `int` | Unix timestamp of response creation. |
| `model` | `string` | The flow ID that was executed. |
| `output` | `list[dict]` | Array of output items (messages, tool calls, etc.). |
| `previous_​response_​id` | `string` | ID of previous response if continuing conversation. |
| `usage` | `dict` | Token usage statistics if the `usage` field is available. Contains `prompt_​tokens`, `completion_​tokens`, and `total_​tokens`. |


## Example streaming request [​](https://docs.langflow.org/api-openai-responses#example-streaming-request)


When you set `"stream": true` with your request, the API returns a stream where each chunk contains a small piece of the response as it's generated. This provides a real-time experience where users can see the AI's output appear word by word, similar to ChatGPT's typing effect.


- Python
- JavaScript
- curl


```python
import os

import requests

url = f"{os.getenv('LANGFLOW_SERVER_URL', '')}/api/v1/responses"

headers = {
    "x-api-key": f"{os.getenv('LANGFLOW_API_KEY', '')}",
    "Content-Type": "application/json",
}

payload = {"model": "$FLOW_ID", "input": "Tell me a story about a robot", "stream": True}

response = requests.request("POST", url, headers=headers, json=payload)
response.raise_for_status()

print(response.text)
```


```js
const url = `${process.env.LANGFLOW_SERVER_URL ?? ""}/api/v1/responses`;

const options = {
  method: 'POST',
  headers: {
    "x-api-key": `${process.env.LANGFLOW_API_KEY ?? ""}`,
    "Content-Type": `application/json`,
  },
  body: JSON.stringify({
  "model": "$FLOW_ID",
  "input": "Tell me a story about a robot",
  "stream": true
}),
};

fetch(url, options)
  .then(async (response) => {
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    const text = await response.text();
    console.log(text);
  })
  .catch((error) => console.error(error));
```


```bash
curl -X POST \
  "$LANGFLOW_SERVER_URL/api/v1/responses" \
  -H "x-api-key: $LANGFLOW_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "$FLOW_ID",
    "input": "Tell me a story about a robot",
    "stream": true
  }'
```


### Streaming response body [​](https://docs.langflow.org/api-openai-responses#streaming-response-body)


| Field | Type | Description |
| --- | --- | --- |
| `id` | `string` | Unique response identifier. |
| `object` | `string` | Always `"response.chunk"`. |
| `created` | `int` | Unix timestamp of chunk creation. |
| `model` | `string` | The flow ID that was executed. |
| `delta` | `dict` | The new content chunk. |
| `status` | `string` | Response status: `"completed"`, `"in_​progress"`, or `"failed"` (optional). |


The stream continues until a final chunk with `"status": "completed"` indicates the response is finished.


## Continue conversations with response and session IDs [​](https://docs.langflow.org/api-openai-responses#response-id)


Conversation continuity allows you to maintain context across multiple API calls, enabling multi-turn conversations with your flows. This is essential for building chat applications where users can have ongoing conversations.


When you make a request, the API returns a response with an `id` field. You can use this `id` as the `previous_response_id` in your next request to continue the conversation from where it left off.


First Message:


- Python
- JavaScript
- curl


```python
import os

import requests

base = os.environ.get("LANGFLOW_URL") or os.environ.get("LANGFLOW_SERVER_URL", "")
flow_id = os.environ.get("FLOW_ID", "")
api_key = os.environ.get("LANGFLOW_API_KEY", "")

url = f"{base}/api/v1/responses"

headers = {
    "x-api-key": api_key,
    "Content-Type": "application/json",
}

payload = {
    "model": flow_id,
    "input": "Hello, my name is Alice",
    "stream": False,
}

response = requests.post(url, headers=headers, json=payload, timeout=120)
response.raise_for_status()

print(response.text)
```


```js
const url = `http://${process.env.LANGFLOW_SERVER_URL ?? ""}/api/v1/responses`;

const options = {
  method: 'POST',
  headers: {
    "x-api-key": `${process.env.LANGFLOW_API_KEY ?? ""}`,
    "Content-Type": `application/json`,
  },
  body: JSON.stringify({
  "model": "$FLOW_ID",
  "input": "Hello, my name is Alice"
}),
};

fetch(url, options)
  .then(async (response) => {
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    const text = await response.text();
    console.log(text);
  })
  .catch((error) => console.error(error));
```


```bash
BASE_URL="${LANGFLOW_SERVER_URL:-$LANGFLOW_URL}"

curl -X POST \
  "$BASE_URL/api/v1/responses" \
  -H "x-api-key: $LANGFLOW_API_KEY" \
  -H "Content-Type: application/json" \
  -d @- <<EOF
{
  "model": "$FLOW_ID",
  "input": "Hello, my name is Alice"
}
EOF
```


Follow-up message:


- Python
- JavaScript
- curl


```python
# Continuation requests use the same endpoint; add `previous_response_id` from a prior
# response's `id` field. The bootstrap flow is empty; use a Playground flow with ChatInput +
# ChatOutput for a full run. Same first message as continue-conversations-with-response-and-session-ids.py.

import os

import requests

base = os.environ.get("LANGFLOW_URL") or os.environ.get("LANGFLOW_SERVER_URL", "")
flow_id = os.environ.get("FLOW_ID", "")
api_key = os.environ.get("LANGFLOW_API_KEY", "")

url = f"{base}/api/v1/responses"

headers = {
    "x-api-key": api_key,
    "Content-Type": "application/json",
}

payload = {
    "model": flow_id,
    "input": "Hello, my name is Alice",
    "stream": False,
}

response = requests.post(url, headers=headers, json=payload, timeout=120)
response.raise_for_status()

print(response.text)
```


```js
const url = `http://${process.env.LANGFLOW_SERVER_URL ?? ""}/api/v1/responses`;

const options = {
  method: 'POST',
  headers: {
    "x-api-key": `${process.env.LANGFLOW_API_KEY ?? ""}`,
    "Content-Type": `application/json`,
  },
  body: JSON.stringify({
  "model": "ced2ec91-f325-4bf0-8754-f3198c2b1563",
  "input": "What's my name?",
  "previous_response_id": "c45f4ac8-772b-4675-8551-c560b1afd590"
}),
};

fetch(url, options)
  .then(async (response) => {
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    const text = await response.text();
    console.log(text);
  })
  .catch((error) => console.error(error));
```


```bash
BASE_URL="${LANGFLOW_SERVER_URL:-$LANGFLOW_URL}"

curl -X POST \
  "$BASE_URL/api/v1/responses" \
  -H "x-api-key: $LANGFLOW_API_KEY" \
  -H "Content-Type: application/json" \
  -d @- <<EOF
{
  "model": "$FLOW_ID",
  "input": "What's my name?",
  "previous_response_id": "c45f4ac8-772b-4675-8551-c560b1afd590"
}
EOF
```


Optionally, you can use your own session ID values for the `previous_response_id`:


- Python
- JavaScript
- curl


```python
# Same pattern as continue-conversations-with-response-and-session-ids-2.py; you can pass
# `previous_response_id` from the prior turn (or a session id your app stores).

import os

import requests

base = os.environ.get("LANGFLOW_URL") or os.environ.get("LANGFLOW_SERVER_URL", "")
flow_id = os.environ.get("FLOW_ID", "")
api_key = os.environ.get("LANGFLOW_API_KEY", "")

url = f"{base}/api/v1/responses"

headers = {
    "x-api-key": api_key,
    "Content-Type": "application/json",
}

payload = {
    "model": flow_id,
    "input": "Hello, my name is Alice",
    "stream": False,
}

response = requests.post(url, headers=headers, json=payload, timeout=120)
response.raise_for_status()

print(response.text)
```


```js
const url = `http://${process.env.LANGFLOW_SERVER_URL ?? ""}/api/v1/responses`;

const options = {
  method: 'POST',
  headers: {
    "x-api-key": `${process.env.LANGFLOW_API_KEY ?? ""}`,
    "Content-Type": `application/json`,
  },
  body: JSON.stringify({
  "model": "ced2ec91-f325-4bf0-8754-f3198c2b1563",
  "input": "What's my name?",
  "previous_response_id": "session-alice-1756839048"
}),
};

fetch(url, options)
  .then(async (response) => {
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    const text = await response.text();
    console.log(text);
  })
  .catch((error) => console.error(error));
```


```bash
BASE_URL="${LANGFLOW_SERVER_URL:-$LANGFLOW_URL}"

curl -X POST \
  "$BASE_URL/api/v1/responses" \
  -H "x-api-key: $LANGFLOW_API_KEY" \
  -H "Content-Type: application/json" \
  -d @- <<EOF
{
  "model": "$FLOW_ID",
  "input": "What's my name?",
  "previous_response_id": "session-alice-1756839048"
}
EOF
```


## Retrieve tool call results [​](https://docs.langflow.org/api-openai-responses#tool-call-results)


When you send a request to the `/api/v1/responses` endpoint to run a flow that includes tools or function calls, you can retrieve the raw tool execution details by adding `"include": ["tool_call.results"]` to the request payload.


Without the `include` parameter, tool calls return basic function call information, but not the raw tool results. For example:


```json
{
  "id": "fc_1",
  "type": "function_call",
  "status": "completed",
  "name": "evaluate_expression",
  "arguments": "{\"expression\": \"15*23\"}"
},
```


To get the raw `results` of each tool execution, add `include: ["tool_call.results"]` to the request payload:


- Python
- JavaScript
- curl


```python
import os

import requests

base = os.environ.get("LANGFLOW_URL") or os.environ.get("LANGFLOW_SERVER_URL", "")
flow_id = os.environ.get("FLOW_ID", "")
api_key = os.environ.get("LANGFLOW_API_KEY", "")

url = f"{base}/api/v1/responses"

headers = {
    "Content-Type": "application/json",
    "x-api-key": api_key,
}

payload = {
    "model": flow_id,
    "input": "Calculate 23 * 15 and show me the result",
    "stream": False,
    "include": ["tool_call.results"],
}

response = requests.post(url, headers=headers, json=payload, timeout=120)
response.raise_for_status()

print(response.text)
```


```js
const url = `http://${process.env.LANGFLOW_SERVER_URL ?? ""}/api/v1/responses`;

const options = {
  method: 'POST',
  headers: {
    "Content-Type": `application/json`,
    "x-api-key": `${process.env.LANGFLOW_API_KEY ?? ""}`,
  },
  body: JSON.stringify({
  "model": "FLOW_ID",
  "input": "Calculate 23 * 15 and show me the result",
  "stream": false,
  "include": [
    "tool_call.results"
  ]
}),
};

fetch(url, options)
  .then(async (response) => {
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    const text = await response.text();
    console.log(text);
  })
  .catch((error) => console.error(error));
```


```bash
BASE_URL="${LANGFLOW_SERVER_URL:-$LANGFLOW_URL}"

curl -X POST \
  "$BASE_URL/api/v1/responses" \
  -H "Content-Type: application/json" \
  -H "x-api-key: $LANGFLOW_API_KEY" \
  -d @- <<EOF
{
    "model": "$FLOW_ID",
    "input": "Calculate 23 * 15 and show me the result",
    "stream": false,
    "include": ["tool_call.results"]
}
EOF
```


The response now includes the tool call's results. For example:


```json
{
  "id": "evaluate_expression_1",
  "type": "tool_call",
  "tool_name": "evaluate_expression",
  "queries": ["15*23"],
  "results": {"result": "345"}
}
```


## Pass global variables to your flows in headers [​](https://docs.langflow.org/api-openai-responses#global-var)


Variables passed with `X-LANGFLOW-GLOBAL-VAR-{VARIABLE_NAME}` are always available to your flow, regardless of whether they exist in the database.


If your flow components reference variables that aren't provided in headers or your Langflow database, the flow fails by default.


To avoid this, you can set the `FALLBACK_TO_ENV_VARS` environment variable is `true`, which allows the flow to use values from the `.env` file if they aren't otherwise specified.


In the above example, `OPENAI_API_KEY` will fall back to the database variable if not provided in the header. `USER_ID` and `ENVIRONMENT` will fall back to environment variables if `FALLBACK_TO_ENV_VARS` is enabled. Otherwise, the flow fails.


## Token usage tracking [​](https://docs.langflow.org/api-openai-responses#token-usage-tracking)


The OpenAI Responses API endpoint tracks token usage when your flow uses language model components that provide token usage information. The `usage` field in the response contains statistics about the number of tokens used for the request and response.


Token usage is automatically extracted from the flow execution results when the `usage` field is available. The `usage` field follows OpenAI's format with `prompt_tokens`, `completion_tokens`, and `total_tokens` fields. If token usage information is not available from the flow components, the `usage` field is `null`.


The `usage` field is always present in the response, either with token counts or as `null`. The conditional checks shown in the examples below are optional defensive programming to handle cases where usage might not be available.


- Python
- JavaScript
- curl


```python
import os

import requests

url = f"{os.getenv('LANGFLOW_SERVER_URL', '')}/api/v1/responses"

headers = {
    "x-api-key": f"{os.getenv('LANGFLOW_API_KEY', '')}",
    "Content-Type": "application/json",
}

payload = {"model": "FLOW_ID", "input": "Explain quantum computing in simple terms", "stream": False}

response = requests.request("POST", url, headers=headers, json=payload)
response.raise_for_status()

print(response.text)
```


```js
const url = `${process.env.LANGFLOW_SERVER_URL ?? ""}/api/v1/responses`;

const options = {
  method: 'POST',
  headers: {
    "x-api-key": `${process.env.LANGFLOW_API_KEY ?? ""}`,
    "Content-Type": `application/json`,
  },
  body: JSON.stringify({
  "model": "FLOW_ID",
  "input": "Explain quantum computing in simple terms",
  "stream": false
}),
};

fetch(url, options)
  .then(async (response) => {
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    const text = await response.text();
    console.log(text);
  })
  .catch((error) => console.error(error));
```


```bash
curl -X POST \
  "$LANGFLOW_SERVER_URL/api/v1/responses" \
  -H "x-api-key: $LANGFLOW_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "FLOW_ID",
    "input": "Explain quantum computing in simple terms",
    "stream": false
  }'
```


Was this page helpful?

Good Bad [Support](https://docs.langflow.org/contributing-github-issues)

- [Prerequisites](https://docs.langflow.org/api-openai-responses#prerequisites)
  - [Additional configuration for OpenAI client libraries](https://docs.langflow.org/api-openai-responses#additional-configuration-for-openai-client-libraries)- [Example request](https://docs.langflow.org/api-openai-responses#example-request)
  - [Headers](https://docs.langflow.org/api-openai-responses#headers)
  - [Request body](https://docs.langflow.org/api-openai-responses#request-body)- [Example response](https://docs.langflow.org/api-openai-responses#example-response)
  - [Response body](https://docs.langflow.org/api-openai-responses#response-body)- [Example streaming request](https://docs.langflow.org/api-openai-responses#example-streaming-request)
  - [Streaming response body](https://docs.langflow.org/api-openai-responses#streaming-response-body)- [Continue conversations with response and session IDs](https://docs.langflow.org/api-openai-responses#response-id)
- [Retrieve tool call results](https://docs.langflow.org/api-openai-responses#tool-call-results)
- [Pass global variables to your flows in headers](https://docs.langflow.org/api-openai-responses#global-var)
- [Token usage tracking](https://docs.langflow.org/api-openai-responses#token-usage-tracking)[Manage Privacy Choices](https://docs.langflow.org/api-openai-responses#)
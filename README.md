# Incident Analysis
_A neural network based model for predicting causal factors of incidents described in natural language._

## Directory Structure
- `Incident-Analysis`
  - `data`: should include a spreadsheet export of the incidents, actions, and factors for each client to be analysed, named `client-`{`incidents`, `actions`, `factors`}`.xlsx`.
  - `code`
    - `modelling`
      - `incident_analysis.ipynb`: contains the entire pipeline for processing data from raw spreadsheet exports to generating a functional neural network model. Additionally provides code for testing the produced model on samples from the provided dataset. More documentation provided inline in the notebook.
      - `clients.py`: required since different clients define a different output format for their `.xlsx` exports. Contains an object for each client to be analysed which includes a mapping of requested columns to their column label in the `.xlsx` output.

## Suggestions for Future Development
- The use of spreadsheet exports should be completely avoided by interfacing directly with the client databases. This has the potential to eliminate the need for a manually defined mapping between the spreadsheet columns and required data (which currently exists in `clients.py`.)
- The architecture of the neural network - while it seems to be relatively successful - could be subjected to more rigorous analytical testing. Testing with datasets from a wider range of clients would increase confidence that the provided architecture was robust to usage by clients who use the software platform in different ways.
- The modelling could be simplified significantly by eliminating the ability to predict the number of factors and actions based on the text description. These predictions require a separate neural network model to the factor predictions, and considering the relatively tiny amount of factors and actions included with most incidents, rarely provide an estimate with a high enough confidence to add significant value to the incident module.
  - The inclusion of this model also means that clients who do not attach actions to incidents cannot currently be predicted without working around the issue.
- An existing limitation is the relatively small size of the dataset from any client in isolation. The few thousand incidents reported even by large clients results in predictions that, while seeming fairly consistently believable, occasionally include spurious, unexplainable results.
  - A potential solution to mitigate this would be to combine the datasets of multiple clients into a large training pool. This raises additional problems when considering that different clients use different sets of factors, but a system like this may be effective on modelling the pool of clients that use the default set of factors.
- Alternative models should be considered for the factor prediction task. Considering the nature of the text embedding model (representing each description as a 50-dimensional vector) a Support Vector Machine may be well equipped for the multi-class classification problem.
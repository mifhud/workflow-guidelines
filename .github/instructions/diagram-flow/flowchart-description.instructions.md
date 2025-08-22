Example mermaid.js flowchart using description text based:

- Basic sample
```
## Start
- **Start**: `Start`
- The process begins

## 1. Step Title
- **{Semantic Name's Shape of Mermaid.js}**: `{Description in Shape}`
- {Detail Description}

## 2. Step Title
- **{Semantic Name's Shape of Mermaid.js}**: `{Description in Shape}`
- {Detail Description}

### End
- **Stop**: `End`
- The process terminates
```

- If there is a decision point in the semantic process sample
```
## 1. Step Title
- **{Semantic Name's Shape of Mermaid.js}**: `{Description in Shape}`
- {Detail Description}
- **Condition**: If {short description condition, e.g yes, no, etc} {description detail}
  - **Condition**: If {short description condition, e.g yes, no, etc} {description detail e.g. must like: proceed to other header markdown step title must excatly same in reference markdown {## 3. Step Title}}
  - **Alternative**: If {short description condition, e.g yes, no, etc} {description detail}
- **Alternative**: If {short description condition, e.g yes, no, etc} {description detail e.g. must like: proceed to other header markdown step title must excatly same in reference markdown {## 2. Step Title}}

## 2. Step Title
- **{Semantic Name's Shape of Mermaid.js}**: `{Description in Shape}`
- {Detail Description}

## 3. Step Title
- **{Semantic Name's Shape of Mermaid.js}**: `{Description in Shape}`
- {Detail Description}
```

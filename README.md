# Concept-Based Spaced Repetition System

## Overview

This system helps with **spaced repetition of concepts**, not just flashcards. Unlike traditional tools like Anki that focus on _memorization_, this approach emphasizes _understanding_.

### The Problem with Traditional Systems

When you get a question wrong in traditional spaced repetition systems, they simply repeat it until you recall the right answer. This reinforces memory — but not comprehension.

**Example:**

```
Question: What is list comprehension in Python?
```

If you don't know the answer, you see the correct one, and the system keeps asking the same question later. Eventually, you memorize it — but do you _understand_ what a list comprehension actually is?

### A Better Approach: Conceptual Scaffolding

Instead of repeating the same question, the system asks an **easier, conceptually related question**:

```
Follow-up: What are lists?
```

This is more effective because the brain stores information in **connected chunks**, not isolated facts. By stepping back to a simpler concept ("lists"), you strengthen the foundation that supports the harder one ("list comprehension").

The same logic applies in reverse. If you get a question **right**, the system follows up with a **harder** question on the same topic.

This creates an adaptive learning loop where you're always working at the edge of your understanding — reinforcing what you know while expanding what you can do.

---

## Commands

### Add a Concept

Create a new concept node in your spaced repetition system:

```bash
sr -add --concept "concept name"
```

**Example:**

```bash
sr -add --concept "Linked Lists"
```

---

### Add Questions to a Concept

Add questions to an existing concept with difficulty levels and types:

```bash
sr -add --concept "Concept Name" -q "question" -d "difficulty" -type "type"
```

**Parameters:**

- `-q` : The question text
- `-d` : Difficulty level (`easy`, `medium`, `hard`)
- `-type` : Question type (`question` [default], `problem`)

**Example:**

```bash
sr -add --concept "Linked Lists" -q "What is a linked list?" -d "easy"
```

You can add multiple questions under the same concept, each tagged with a difficulty level.

---

### Revise All Concepts

Begin a revision session across all your concepts:

```bash
sr --revise
```

The system selects which question or concept to ask based on what it believes you need to study.

**Example Session:**

```
> What is a Linked List? (press Enter for answer)
<Enter>

A linked list is a data structure made of nodes, each containing 
data and a reference to the next node.

How would you rate your answer compared to the reference answer? {0–10}
<Enter>
```

**Adaptive Behavior:**

- **High rating** → You'll get a **harder** question
- **Low rating** → You'll get an **easier**, foundational question

---

### Revise a Specific Concept

Focus revision on a specific concept:

```bash
sr --revise --concept "concept name"
```

**Example:**

```bash
sr --revise --concept "Linked Lists"
```

This command behaves like `sr --revise`, but focuses only on the chosen concept.

---

## Data Models

### Concept Structure

Concepts are organized as a linked list, where each node knows its **previous**, **current**, and **next** concept:

```
----O----O----O----O----O----O----O----O----
```

**Example Structure:**

|prev|concept|next|
|---|---|---|
|none|lists|dicts|
|lists|dicts|tuples|

Each concept node contains a collection of questions/problems with their own attributes.

---

### Question Attributes

Each question within a concept tracks the following data:

|Question|Difficulty|Count|Success Rate|Last Revised|Type|Answer/Solution|
|---|---|---|---|---|---|---|
|What is a list?|Easy|5|7.4|2025-11-01|question|answer|

**Attributes:**

- **Question**: The question text
- **Difficulty**: `easy`, `medium`, or `hard`
- **Count**: Number of times reviewed
- **Success Rate**: Average self-rating (0-10 scale)
- **Last Revised**: Date of most recent review
- **Type**: `question` or `problem`
- **Answer/Solution**: Reference answer or solution

---

## Algorithm

The system calculates the optimal next question based on all tracked data:

1. **Within a concept**: Questions are selected based on difficulty, success rate, and time since last review
2. **Between concepts**:
    - If answers are consistently **correct** → Move to the **next** (harder) concept
    - If answers are consistently **incorrect** → Move to the **previous** (easier) concept
3. **Session continues** until the current concept is exhausted, then transitions to adjacent concepts

This creates a dynamic learning path that adapts to your current level of understanding.
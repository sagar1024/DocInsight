import pytest
from app.services.summarization import process_document
from app.services.chatbot import get_chatbot_response
from app.services.voice import text_to_speech
from app.utils.nlp_utils import generate_summary

def test_summarize_document():
    text = "DocInsight is an AI-powered application designed to summarize and analyze documents."
    summary = process_document(text, "short")
    assert len(summary) > 0
    assert "DocInsight" in summary

def test_chatbot_response():
    query = "What is DocInsight?"
    response = get_chatbot_response(query)
    assert len(response) > 0
    assert "DocInsight" in response

def test_text_to_speech():
    text = "This is a test for text-to-speech conversion."
    audio_data = text_to_speech(text)
    assert audio_data is not None
    assert isinstance(audio_data, bytes)

def test_generate_summary():
    text = "This is a long document explaining the details of an AI-powered document summarization system."
    summary = generate_summary(text, length="short")
    assert len(summary) > 0
    assert "document summarization" in summary

def test_process_document_with_images():
    file = open("test_data/sample_with_images.pdf", "rb")
    result = process_document(file)
    assert "Summary" in result
    assert result["images"] > 0
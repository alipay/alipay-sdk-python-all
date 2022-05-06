#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.NewsConcerned import NewsConcerned
from alipay.aop.api.domain.KeywordsHighlight import KeywordsHighlight
from alipay.aop.api.domain.NewsNerEntity import NewsNerEntity
from alipay.aop.api.domain.NewsRelatedCompany import NewsRelatedCompany


class NewsSource(object):

    def __init__(self):
        self._author_name = None
        self._concerned = None
        self._content_url = None
        self._doc_self_content_sign = None
        self._first_publish_media = None
        self._highlight = None
        self._images = None
        self._media_source = None
        self._ner_entities = None
        self._obj_id = None
        self._pub_time = None
        self._related_companies = None
        self._searchable_text = None
        self._source_doc_id = None
        self._source_doc_type = None
        self._source_type = None
        self._summary = None
        self._title = None

    @property
    def author_name(self):
        return self._author_name

    @author_name.setter
    def author_name(self, value):
        self._author_name = value
    @property
    def concerned(self):
        return self._concerned

    @concerned.setter
    def concerned(self, value):
        if isinstance(value, list):
            self._concerned = list()
            for i in value:
                if isinstance(i, NewsConcerned):
                    self._concerned.append(i)
                else:
                    self._concerned.append(NewsConcerned.from_alipay_dict(i))
    @property
    def content_url(self):
        return self._content_url

    @content_url.setter
    def content_url(self, value):
        self._content_url = value
    @property
    def doc_self_content_sign(self):
        return self._doc_self_content_sign

    @doc_self_content_sign.setter
    def doc_self_content_sign(self, value):
        self._doc_self_content_sign = value
    @property
    def first_publish_media(self):
        return self._first_publish_media

    @first_publish_media.setter
    def first_publish_media(self, value):
        self._first_publish_media = value
    @property
    def highlight(self):
        return self._highlight

    @highlight.setter
    def highlight(self, value):
        if isinstance(value, KeywordsHighlight):
            self._highlight = value
        else:
            self._highlight = KeywordsHighlight.from_alipay_dict(value)
    @property
    def images(self):
        return self._images

    @images.setter
    def images(self, value):
        if isinstance(value, list):
            self._images = list()
            for i in value:
                self._images.append(i)
    @property
    def media_source(self):
        return self._media_source

    @media_source.setter
    def media_source(self, value):
        self._media_source = value
    @property
    def ner_entities(self):
        return self._ner_entities

    @ner_entities.setter
    def ner_entities(self, value):
        if isinstance(value, list):
            self._ner_entities = list()
            for i in value:
                if isinstance(i, NewsNerEntity):
                    self._ner_entities.append(i)
                else:
                    self._ner_entities.append(NewsNerEntity.from_alipay_dict(i))
    @property
    def obj_id(self):
        return self._obj_id

    @obj_id.setter
    def obj_id(self, value):
        self._obj_id = value
    @property
    def pub_time(self):
        return self._pub_time

    @pub_time.setter
    def pub_time(self, value):
        self._pub_time = value
    @property
    def related_companies(self):
        return self._related_companies

    @related_companies.setter
    def related_companies(self, value):
        if isinstance(value, list):
            self._related_companies = list()
            for i in value:
                if isinstance(i, NewsRelatedCompany):
                    self._related_companies.append(i)
                else:
                    self._related_companies.append(NewsRelatedCompany.from_alipay_dict(i))
    @property
    def searchable_text(self):
        return self._searchable_text

    @searchable_text.setter
    def searchable_text(self, value):
        self._searchable_text = value
    @property
    def source_doc_id(self):
        return self._source_doc_id

    @source_doc_id.setter
    def source_doc_id(self, value):
        self._source_doc_id = value
    @property
    def source_doc_type(self):
        return self._source_doc_type

    @source_doc_type.setter
    def source_doc_type(self, value):
        self._source_doc_type = value
    @property
    def source_type(self):
        return self._source_type

    @source_type.setter
    def source_type(self, value):
        self._source_type = value
    @property
    def summary(self):
        return self._summary

    @summary.setter
    def summary(self, value):
        self._summary = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.author_name:
            if hasattr(self.author_name, 'to_alipay_dict'):
                params['author_name'] = self.author_name.to_alipay_dict()
            else:
                params['author_name'] = self.author_name
        if self.concerned:
            if isinstance(self.concerned, list):
                for i in range(0, len(self.concerned)):
                    element = self.concerned[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.concerned[i] = element.to_alipay_dict()
            if hasattr(self.concerned, 'to_alipay_dict'):
                params['concerned'] = self.concerned.to_alipay_dict()
            else:
                params['concerned'] = self.concerned
        if self.content_url:
            if hasattr(self.content_url, 'to_alipay_dict'):
                params['content_url'] = self.content_url.to_alipay_dict()
            else:
                params['content_url'] = self.content_url
        if self.doc_self_content_sign:
            if hasattr(self.doc_self_content_sign, 'to_alipay_dict'):
                params['doc_self_content_sign'] = self.doc_self_content_sign.to_alipay_dict()
            else:
                params['doc_self_content_sign'] = self.doc_self_content_sign
        if self.first_publish_media:
            if hasattr(self.first_publish_media, 'to_alipay_dict'):
                params['first_publish_media'] = self.first_publish_media.to_alipay_dict()
            else:
                params['first_publish_media'] = self.first_publish_media
        if self.highlight:
            if hasattr(self.highlight, 'to_alipay_dict'):
                params['highlight'] = self.highlight.to_alipay_dict()
            else:
                params['highlight'] = self.highlight
        if self.images:
            if isinstance(self.images, list):
                for i in range(0, len(self.images)):
                    element = self.images[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.images[i] = element.to_alipay_dict()
            if hasattr(self.images, 'to_alipay_dict'):
                params['images'] = self.images.to_alipay_dict()
            else:
                params['images'] = self.images
        if self.media_source:
            if hasattr(self.media_source, 'to_alipay_dict'):
                params['media_source'] = self.media_source.to_alipay_dict()
            else:
                params['media_source'] = self.media_source
        if self.ner_entities:
            if isinstance(self.ner_entities, list):
                for i in range(0, len(self.ner_entities)):
                    element = self.ner_entities[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ner_entities[i] = element.to_alipay_dict()
            if hasattr(self.ner_entities, 'to_alipay_dict'):
                params['ner_entities'] = self.ner_entities.to_alipay_dict()
            else:
                params['ner_entities'] = self.ner_entities
        if self.obj_id:
            if hasattr(self.obj_id, 'to_alipay_dict'):
                params['obj_id'] = self.obj_id.to_alipay_dict()
            else:
                params['obj_id'] = self.obj_id
        if self.pub_time:
            if hasattr(self.pub_time, 'to_alipay_dict'):
                params['pub_time'] = self.pub_time.to_alipay_dict()
            else:
                params['pub_time'] = self.pub_time
        if self.related_companies:
            if isinstance(self.related_companies, list):
                for i in range(0, len(self.related_companies)):
                    element = self.related_companies[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.related_companies[i] = element.to_alipay_dict()
            if hasattr(self.related_companies, 'to_alipay_dict'):
                params['related_companies'] = self.related_companies.to_alipay_dict()
            else:
                params['related_companies'] = self.related_companies
        if self.searchable_text:
            if hasattr(self.searchable_text, 'to_alipay_dict'):
                params['searchable_text'] = self.searchable_text.to_alipay_dict()
            else:
                params['searchable_text'] = self.searchable_text
        if self.source_doc_id:
            if hasattr(self.source_doc_id, 'to_alipay_dict'):
                params['source_doc_id'] = self.source_doc_id.to_alipay_dict()
            else:
                params['source_doc_id'] = self.source_doc_id
        if self.source_doc_type:
            if hasattr(self.source_doc_type, 'to_alipay_dict'):
                params['source_doc_type'] = self.source_doc_type.to_alipay_dict()
            else:
                params['source_doc_type'] = self.source_doc_type
        if self.source_type:
            if hasattr(self.source_type, 'to_alipay_dict'):
                params['source_type'] = self.source_type.to_alipay_dict()
            else:
                params['source_type'] = self.source_type
        if self.summary:
            if hasattr(self.summary, 'to_alipay_dict'):
                params['summary'] = self.summary.to_alipay_dict()
            else:
                params['summary'] = self.summary
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NewsSource()
        if 'author_name' in d:
            o.author_name = d['author_name']
        if 'concerned' in d:
            o.concerned = d['concerned']
        if 'content_url' in d:
            o.content_url = d['content_url']
        if 'doc_self_content_sign' in d:
            o.doc_self_content_sign = d['doc_self_content_sign']
        if 'first_publish_media' in d:
            o.first_publish_media = d['first_publish_media']
        if 'highlight' in d:
            o.highlight = d['highlight']
        if 'images' in d:
            o.images = d['images']
        if 'media_source' in d:
            o.media_source = d['media_source']
        if 'ner_entities' in d:
            o.ner_entities = d['ner_entities']
        if 'obj_id' in d:
            o.obj_id = d['obj_id']
        if 'pub_time' in d:
            o.pub_time = d['pub_time']
        if 'related_companies' in d:
            o.related_companies = d['related_companies']
        if 'searchable_text' in d:
            o.searchable_text = d['searchable_text']
        if 'source_doc_id' in d:
            o.source_doc_id = d['source_doc_id']
        if 'source_doc_type' in d:
            o.source_doc_type = d['source_doc_type']
        if 'source_type' in d:
            o.source_type = d['source_type']
        if 'summary' in d:
            o.summary = d['summary']
        if 'title' in d:
            o.title = d['title']
        return o



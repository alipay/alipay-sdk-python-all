#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenSearchDocBO(object):

    def __init__(self):
        self._abstract_extract = None
        self._channel = None
        self._doc = None
        self._doc_abstract = None
        self._doc_id = None
        self._doc_url = None
        self._model_abstract_score = None
        self._pic_afts_url_list = None
        self._pic_oss_path = None
        self._publish_timestamp = None
        self._rel_score = None
        self._scale_score = None
        self._source = None
        self._title = None
        self._type = None

    @property
    def abstract_extract(self):
        return self._abstract_extract

    @abstract_extract.setter
    def abstract_extract(self, value):
        self._abstract_extract = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def doc(self):
        return self._doc

    @doc.setter
    def doc(self, value):
        self._doc = value
    @property
    def doc_abstract(self):
        return self._doc_abstract

    @doc_abstract.setter
    def doc_abstract(self, value):
        self._doc_abstract = value
    @property
    def doc_id(self):
        return self._doc_id

    @doc_id.setter
    def doc_id(self, value):
        self._doc_id = value
    @property
    def doc_url(self):
        return self._doc_url

    @doc_url.setter
    def doc_url(self, value):
        self._doc_url = value
    @property
    def model_abstract_score(self):
        return self._model_abstract_score

    @model_abstract_score.setter
    def model_abstract_score(self, value):
        self._model_abstract_score = value
    @property
    def pic_afts_url_list(self):
        return self._pic_afts_url_list

    @pic_afts_url_list.setter
    def pic_afts_url_list(self, value):
        self._pic_afts_url_list = value
    @property
    def pic_oss_path(self):
        return self._pic_oss_path

    @pic_oss_path.setter
    def pic_oss_path(self, value):
        self._pic_oss_path = value
    @property
    def publish_timestamp(self):
        return self._publish_timestamp

    @publish_timestamp.setter
    def publish_timestamp(self, value):
        self._publish_timestamp = value
    @property
    def rel_score(self):
        return self._rel_score

    @rel_score.setter
    def rel_score(self, value):
        self._rel_score = value
    @property
    def scale_score(self):
        return self._scale_score

    @scale_score.setter
    def scale_score(self, value):
        self._scale_score = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.abstract_extract:
            if hasattr(self.abstract_extract, 'to_alipay_dict'):
                params['abstract_extract'] = self.abstract_extract.to_alipay_dict()
            else:
                params['abstract_extract'] = self.abstract_extract
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.doc:
            if hasattr(self.doc, 'to_alipay_dict'):
                params['doc'] = self.doc.to_alipay_dict()
            else:
                params['doc'] = self.doc
        if self.doc_abstract:
            if hasattr(self.doc_abstract, 'to_alipay_dict'):
                params['doc_abstract'] = self.doc_abstract.to_alipay_dict()
            else:
                params['doc_abstract'] = self.doc_abstract
        if self.doc_id:
            if hasattr(self.doc_id, 'to_alipay_dict'):
                params['doc_id'] = self.doc_id.to_alipay_dict()
            else:
                params['doc_id'] = self.doc_id
        if self.doc_url:
            if hasattr(self.doc_url, 'to_alipay_dict'):
                params['doc_url'] = self.doc_url.to_alipay_dict()
            else:
                params['doc_url'] = self.doc_url
        if self.model_abstract_score:
            if hasattr(self.model_abstract_score, 'to_alipay_dict'):
                params['model_abstract_score'] = self.model_abstract_score.to_alipay_dict()
            else:
                params['model_abstract_score'] = self.model_abstract_score
        if self.pic_afts_url_list:
            if hasattr(self.pic_afts_url_list, 'to_alipay_dict'):
                params['pic_afts_url_list'] = self.pic_afts_url_list.to_alipay_dict()
            else:
                params['pic_afts_url_list'] = self.pic_afts_url_list
        if self.pic_oss_path:
            if hasattr(self.pic_oss_path, 'to_alipay_dict'):
                params['pic_oss_path'] = self.pic_oss_path.to_alipay_dict()
            else:
                params['pic_oss_path'] = self.pic_oss_path
        if self.publish_timestamp:
            if hasattr(self.publish_timestamp, 'to_alipay_dict'):
                params['publish_timestamp'] = self.publish_timestamp.to_alipay_dict()
            else:
                params['publish_timestamp'] = self.publish_timestamp
        if self.rel_score:
            if hasattr(self.rel_score, 'to_alipay_dict'):
                params['rel_score'] = self.rel_score.to_alipay_dict()
            else:
                params['rel_score'] = self.rel_score
        if self.scale_score:
            if hasattr(self.scale_score, 'to_alipay_dict'):
                params['scale_score'] = self.scale_score.to_alipay_dict()
            else:
                params['scale_score'] = self.scale_score
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenSearchDocBO()
        if 'abstract_extract' in d:
            o.abstract_extract = d['abstract_extract']
        if 'channel' in d:
            o.channel = d['channel']
        if 'doc' in d:
            o.doc = d['doc']
        if 'doc_abstract' in d:
            o.doc_abstract = d['doc_abstract']
        if 'doc_id' in d:
            o.doc_id = d['doc_id']
        if 'doc_url' in d:
            o.doc_url = d['doc_url']
        if 'model_abstract_score' in d:
            o.model_abstract_score = d['model_abstract_score']
        if 'pic_afts_url_list' in d:
            o.pic_afts_url_list = d['pic_afts_url_list']
        if 'pic_oss_path' in d:
            o.pic_oss_path = d['pic_oss_path']
        if 'publish_timestamp' in d:
            o.publish_timestamp = d['publish_timestamp']
        if 'rel_score' in d:
            o.rel_score = d['rel_score']
        if 'scale_score' in d:
            o.scale_score = d['scale_score']
        if 'source' in d:
            o.source = d['source']
        if 'title' in d:
            o.title = d['title']
        if 'type' in d:
            o.type = d['type']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DataItem(object):

    def __init__(self):
        self._biz_trace_id = None
        self._ext_res_field = None
        self._highlight_summary = None
        self._highlight_title = None
        self._id = None
        self._images = None
        self._item_total_count = None
        self._score = None
        self._sequence = None
        self._summary = None
        self._title = None
        self._trace_id = None

    @property
    def biz_trace_id(self):
        return self._biz_trace_id

    @biz_trace_id.setter
    def biz_trace_id(self, value):
        self._biz_trace_id = value
    @property
    def ext_res_field(self):
        return self._ext_res_field

    @ext_res_field.setter
    def ext_res_field(self, value):
        if isinstance(value, list):
            self._ext_res_field = list()
            for i in value:
                self._ext_res_field.append(i)
    @property
    def highlight_summary(self):
        return self._highlight_summary

    @highlight_summary.setter
    def highlight_summary(self, value):
        self._highlight_summary = value
    @property
    def highlight_title(self):
        return self._highlight_title

    @highlight_title.setter
    def highlight_title(self, value):
        self._highlight_title = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
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
    def item_total_count(self):
        return self._item_total_count

    @item_total_count.setter
    def item_total_count(self, value):
        self._item_total_count = value
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value
    @property
    def sequence(self):
        return self._sequence

    @sequence.setter
    def sequence(self, value):
        self._sequence = value
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
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_trace_id:
            if hasattr(self.biz_trace_id, 'to_alipay_dict'):
                params['biz_trace_id'] = self.biz_trace_id.to_alipay_dict()
            else:
                params['biz_trace_id'] = self.biz_trace_id
        if self.ext_res_field:
            if isinstance(self.ext_res_field, list):
                for i in range(0, len(self.ext_res_field)):
                    element = self.ext_res_field[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ext_res_field[i] = element.to_alipay_dict()
            if hasattr(self.ext_res_field, 'to_alipay_dict'):
                params['ext_res_field'] = self.ext_res_field.to_alipay_dict()
            else:
                params['ext_res_field'] = self.ext_res_field
        if self.highlight_summary:
            if hasattr(self.highlight_summary, 'to_alipay_dict'):
                params['highlight_summary'] = self.highlight_summary.to_alipay_dict()
            else:
                params['highlight_summary'] = self.highlight_summary
        if self.highlight_title:
            if hasattr(self.highlight_title, 'to_alipay_dict'):
                params['highlight_title'] = self.highlight_title.to_alipay_dict()
            else:
                params['highlight_title'] = self.highlight_title
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
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
        if self.item_total_count:
            if hasattr(self.item_total_count, 'to_alipay_dict'):
                params['item_total_count'] = self.item_total_count.to_alipay_dict()
            else:
                params['item_total_count'] = self.item_total_count
        if self.score:
            if hasattr(self.score, 'to_alipay_dict'):
                params['score'] = self.score.to_alipay_dict()
            else:
                params['score'] = self.score
        if self.sequence:
            if hasattr(self.sequence, 'to_alipay_dict'):
                params['sequence'] = self.sequence.to_alipay_dict()
            else:
                params['sequence'] = self.sequence
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
        if self.trace_id:
            if hasattr(self.trace_id, 'to_alipay_dict'):
                params['trace_id'] = self.trace_id.to_alipay_dict()
            else:
                params['trace_id'] = self.trace_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DataItem()
        if 'biz_trace_id' in d:
            o.biz_trace_id = d['biz_trace_id']
        if 'ext_res_field' in d:
            o.ext_res_field = d['ext_res_field']
        if 'highlight_summary' in d:
            o.highlight_summary = d['highlight_summary']
        if 'highlight_title' in d:
            o.highlight_title = d['highlight_title']
        if 'id' in d:
            o.id = d['id']
        if 'images' in d:
            o.images = d['images']
        if 'item_total_count' in d:
            o.item_total_count = d['item_total_count']
        if 'score' in d:
            o.score = d['score']
        if 'sequence' in d:
            o.sequence = d['sequence']
        if 'summary' in d:
            o.summary = d['summary']
        if 'title' in d:
            o.title = d['title']
        if 'trace_id' in d:
            o.trace_id = d['trace_id']
        return o



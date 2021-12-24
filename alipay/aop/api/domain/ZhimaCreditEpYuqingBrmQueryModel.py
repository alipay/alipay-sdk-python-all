#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditEpYuqingBrmQueryModel(object):

    def __init__(self):
        self._begin = None
        self._crn = None
        self._doc_self_content_sign = None
        self._end = None
        self._entities_and = None
        self._entities_or = None
        self._ids = None
        self._keywords_and = None
        self._keywords_or = None
        self._labels = None
        self._need_entity_agg = None
        self._need_label_agg = None
        self._page = None
        self._size = None
        self._use_update_time = None

    @property
    def begin(self):
        return self._begin

    @begin.setter
    def begin(self, value):
        self._begin = value
    @property
    def crn(self):
        return self._crn

    @crn.setter
    def crn(self, value):
        self._crn = value
    @property
    def doc_self_content_sign(self):
        return self._doc_self_content_sign

    @doc_self_content_sign.setter
    def doc_self_content_sign(self, value):
        self._doc_self_content_sign = value
    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, value):
        self._end = value
    @property
    def entities_and(self):
        return self._entities_and

    @entities_and.setter
    def entities_and(self, value):
        if isinstance(value, list):
            self._entities_and = list()
            for i in value:
                self._entities_and.append(i)
    @property
    def entities_or(self):
        return self._entities_or

    @entities_or.setter
    def entities_or(self, value):
        if isinstance(value, list):
            self._entities_or = list()
            for i in value:
                self._entities_or.append(i)
    @property
    def ids(self):
        return self._ids

    @ids.setter
    def ids(self, value):
        if isinstance(value, list):
            self._ids = list()
            for i in value:
                self._ids.append(i)
    @property
    def keywords_and(self):
        return self._keywords_and

    @keywords_and.setter
    def keywords_and(self, value):
        if isinstance(value, list):
            self._keywords_and = list()
            for i in value:
                self._keywords_and.append(i)
    @property
    def keywords_or(self):
        return self._keywords_or

    @keywords_or.setter
    def keywords_or(self, value):
        if isinstance(value, list):
            self._keywords_or = list()
            for i in value:
                self._keywords_or.append(i)
    @property
    def labels(self):
        return self._labels

    @labels.setter
    def labels(self, value):
        if isinstance(value, list):
            self._labels = list()
            for i in value:
                self._labels.append(i)
    @property
    def need_entity_agg(self):
        return self._need_entity_agg

    @need_entity_agg.setter
    def need_entity_agg(self, value):
        self._need_entity_agg = value
    @property
    def need_label_agg(self):
        return self._need_label_agg

    @need_label_agg.setter
    def need_label_agg(self, value):
        self._need_label_agg = value
    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, value):
        self._page = value
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value
    @property
    def use_update_time(self):
        return self._use_update_time

    @use_update_time.setter
    def use_update_time(self, value):
        self._use_update_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.begin:
            if hasattr(self.begin, 'to_alipay_dict'):
                params['begin'] = self.begin.to_alipay_dict()
            else:
                params['begin'] = self.begin
        if self.crn:
            if hasattr(self.crn, 'to_alipay_dict'):
                params['crn'] = self.crn.to_alipay_dict()
            else:
                params['crn'] = self.crn
        if self.doc_self_content_sign:
            if hasattr(self.doc_self_content_sign, 'to_alipay_dict'):
                params['doc_self_content_sign'] = self.doc_self_content_sign.to_alipay_dict()
            else:
                params['doc_self_content_sign'] = self.doc_self_content_sign
        if self.end:
            if hasattr(self.end, 'to_alipay_dict'):
                params['end'] = self.end.to_alipay_dict()
            else:
                params['end'] = self.end
        if self.entities_and:
            if isinstance(self.entities_and, list):
                for i in range(0, len(self.entities_and)):
                    element = self.entities_and[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.entities_and[i] = element.to_alipay_dict()
            if hasattr(self.entities_and, 'to_alipay_dict'):
                params['entities_and'] = self.entities_and.to_alipay_dict()
            else:
                params['entities_and'] = self.entities_and
        if self.entities_or:
            if isinstance(self.entities_or, list):
                for i in range(0, len(self.entities_or)):
                    element = self.entities_or[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.entities_or[i] = element.to_alipay_dict()
            if hasattr(self.entities_or, 'to_alipay_dict'):
                params['entities_or'] = self.entities_or.to_alipay_dict()
            else:
                params['entities_or'] = self.entities_or
        if self.ids:
            if isinstance(self.ids, list):
                for i in range(0, len(self.ids)):
                    element = self.ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ids[i] = element.to_alipay_dict()
            if hasattr(self.ids, 'to_alipay_dict'):
                params['ids'] = self.ids.to_alipay_dict()
            else:
                params['ids'] = self.ids
        if self.keywords_and:
            if isinstance(self.keywords_and, list):
                for i in range(0, len(self.keywords_and)):
                    element = self.keywords_and[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.keywords_and[i] = element.to_alipay_dict()
            if hasattr(self.keywords_and, 'to_alipay_dict'):
                params['keywords_and'] = self.keywords_and.to_alipay_dict()
            else:
                params['keywords_and'] = self.keywords_and
        if self.keywords_or:
            if isinstance(self.keywords_or, list):
                for i in range(0, len(self.keywords_or)):
                    element = self.keywords_or[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.keywords_or[i] = element.to_alipay_dict()
            if hasattr(self.keywords_or, 'to_alipay_dict'):
                params['keywords_or'] = self.keywords_or.to_alipay_dict()
            else:
                params['keywords_or'] = self.keywords_or
        if self.labels:
            if isinstance(self.labels, list):
                for i in range(0, len(self.labels)):
                    element = self.labels[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.labels[i] = element.to_alipay_dict()
            if hasattr(self.labels, 'to_alipay_dict'):
                params['labels'] = self.labels.to_alipay_dict()
            else:
                params['labels'] = self.labels
        if self.need_entity_agg:
            if hasattr(self.need_entity_agg, 'to_alipay_dict'):
                params['need_entity_agg'] = self.need_entity_agg.to_alipay_dict()
            else:
                params['need_entity_agg'] = self.need_entity_agg
        if self.need_label_agg:
            if hasattr(self.need_label_agg, 'to_alipay_dict'):
                params['need_label_agg'] = self.need_label_agg.to_alipay_dict()
            else:
                params['need_label_agg'] = self.need_label_agg
        if self.page:
            if hasattr(self.page, 'to_alipay_dict'):
                params['page'] = self.page.to_alipay_dict()
            else:
                params['page'] = self.page
        if self.size:
            if hasattr(self.size, 'to_alipay_dict'):
                params['size'] = self.size.to_alipay_dict()
            else:
                params['size'] = self.size
        if self.use_update_time:
            if hasattr(self.use_update_time, 'to_alipay_dict'):
                params['use_update_time'] = self.use_update_time.to_alipay_dict()
            else:
                params['use_update_time'] = self.use_update_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpYuqingBrmQueryModel()
        if 'begin' in d:
            o.begin = d['begin']
        if 'crn' in d:
            o.crn = d['crn']
        if 'doc_self_content_sign' in d:
            o.doc_self_content_sign = d['doc_self_content_sign']
        if 'end' in d:
            o.end = d['end']
        if 'entities_and' in d:
            o.entities_and = d['entities_and']
        if 'entities_or' in d:
            o.entities_or = d['entities_or']
        if 'ids' in d:
            o.ids = d['ids']
        if 'keywords_and' in d:
            o.keywords_and = d['keywords_and']
        if 'keywords_or' in d:
            o.keywords_or = d['keywords_or']
        if 'labels' in d:
            o.labels = d['labels']
        if 'need_entity_agg' in d:
            o.need_entity_agg = d['need_entity_agg']
        if 'need_label_agg' in d:
            o.need_label_agg = d['need_label_agg']
        if 'page' in d:
            o.page = d['page']
        if 'size' in d:
            o.size = d['size']
        if 'use_update_time' in d:
            o.use_update_time = d['use_update_time']
        return o



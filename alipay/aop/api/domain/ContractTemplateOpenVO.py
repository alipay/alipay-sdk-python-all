#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CorporateSealRectOpenVO import CorporateSealRectOpenVO
from alipay.aop.api.domain.MultilineTextRectOpenVO import MultilineTextRectOpenVO
from alipay.aop.api.domain.PersonalSealRectOpenVO import PersonalSealRectOpenVO
from alipay.aop.api.domain.MultilineTextRectOpenVO import MultilineTextRectOpenVO
from alipay.aop.api.domain.TimeStampRectOpenVO import TimeStampRectOpenVO


class ContractTemplateOpenVO(object):

    def __init__(self):
        self._corporate_seal_rects = None
        self._multiline_text_rects = None
        self._must_read = None
        self._personal_seal_rects = None
        self._preview_url = None
        self._singleline_text_rects = None
        self._template_id = None
        self._template_memo = None
        self._template_name = None
        self._template_source = None
        self._template_type = None
        self._time_stamp_rects = None

    @property
    def corporate_seal_rects(self):
        return self._corporate_seal_rects

    @corporate_seal_rects.setter
    def corporate_seal_rects(self, value):
        if isinstance(value, list):
            self._corporate_seal_rects = list()
            for i in value:
                if isinstance(i, CorporateSealRectOpenVO):
                    self._corporate_seal_rects.append(i)
                else:
                    self._corporate_seal_rects.append(CorporateSealRectOpenVO.from_alipay_dict(i))
    @property
    def multiline_text_rects(self):
        return self._multiline_text_rects

    @multiline_text_rects.setter
    def multiline_text_rects(self, value):
        if isinstance(value, list):
            self._multiline_text_rects = list()
            for i in value:
                if isinstance(i, MultilineTextRectOpenVO):
                    self._multiline_text_rects.append(i)
                else:
                    self._multiline_text_rects.append(MultilineTextRectOpenVO.from_alipay_dict(i))
    @property
    def must_read(self):
        return self._must_read

    @must_read.setter
    def must_read(self, value):
        self._must_read = value
    @property
    def personal_seal_rects(self):
        return self._personal_seal_rects

    @personal_seal_rects.setter
    def personal_seal_rects(self, value):
        if isinstance(value, list):
            self._personal_seal_rects = list()
            for i in value:
                if isinstance(i, PersonalSealRectOpenVO):
                    self._personal_seal_rects.append(i)
                else:
                    self._personal_seal_rects.append(PersonalSealRectOpenVO.from_alipay_dict(i))
    @property
    def preview_url(self):
        return self._preview_url

    @preview_url.setter
    def preview_url(self, value):
        self._preview_url = value
    @property
    def singleline_text_rects(self):
        return self._singleline_text_rects

    @singleline_text_rects.setter
    def singleline_text_rects(self, value):
        if isinstance(value, list):
            self._singleline_text_rects = list()
            for i in value:
                if isinstance(i, MultilineTextRectOpenVO):
                    self._singleline_text_rects.append(i)
                else:
                    self._singleline_text_rects.append(MultilineTextRectOpenVO.from_alipay_dict(i))
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def template_memo(self):
        return self._template_memo

    @template_memo.setter
    def template_memo(self, value):
        self._template_memo = value
    @property
    def template_name(self):
        return self._template_name

    @template_name.setter
    def template_name(self, value):
        self._template_name = value
    @property
    def template_source(self):
        return self._template_source

    @template_source.setter
    def template_source(self, value):
        self._template_source = value
    @property
    def template_type(self):
        return self._template_type

    @template_type.setter
    def template_type(self, value):
        self._template_type = value
    @property
    def time_stamp_rects(self):
        return self._time_stamp_rects

    @time_stamp_rects.setter
    def time_stamp_rects(self, value):
        if isinstance(value, list):
            self._time_stamp_rects = list()
            for i in value:
                if isinstance(i, TimeStampRectOpenVO):
                    self._time_stamp_rects.append(i)
                else:
                    self._time_stamp_rects.append(TimeStampRectOpenVO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.corporate_seal_rects:
            if isinstance(self.corporate_seal_rects, list):
                for i in range(0, len(self.corporate_seal_rects)):
                    element = self.corporate_seal_rects[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.corporate_seal_rects[i] = element.to_alipay_dict()
            if hasattr(self.corporate_seal_rects, 'to_alipay_dict'):
                params['corporate_seal_rects'] = self.corporate_seal_rects.to_alipay_dict()
            else:
                params['corporate_seal_rects'] = self.corporate_seal_rects
        if self.multiline_text_rects:
            if isinstance(self.multiline_text_rects, list):
                for i in range(0, len(self.multiline_text_rects)):
                    element = self.multiline_text_rects[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.multiline_text_rects[i] = element.to_alipay_dict()
            if hasattr(self.multiline_text_rects, 'to_alipay_dict'):
                params['multiline_text_rects'] = self.multiline_text_rects.to_alipay_dict()
            else:
                params['multiline_text_rects'] = self.multiline_text_rects
        if self.must_read:
            if hasattr(self.must_read, 'to_alipay_dict'):
                params['must_read'] = self.must_read.to_alipay_dict()
            else:
                params['must_read'] = self.must_read
        if self.personal_seal_rects:
            if isinstance(self.personal_seal_rects, list):
                for i in range(0, len(self.personal_seal_rects)):
                    element = self.personal_seal_rects[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.personal_seal_rects[i] = element.to_alipay_dict()
            if hasattr(self.personal_seal_rects, 'to_alipay_dict'):
                params['personal_seal_rects'] = self.personal_seal_rects.to_alipay_dict()
            else:
                params['personal_seal_rects'] = self.personal_seal_rects
        if self.preview_url:
            if hasattr(self.preview_url, 'to_alipay_dict'):
                params['preview_url'] = self.preview_url.to_alipay_dict()
            else:
                params['preview_url'] = self.preview_url
        if self.singleline_text_rects:
            if isinstance(self.singleline_text_rects, list):
                for i in range(0, len(self.singleline_text_rects)):
                    element = self.singleline_text_rects[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.singleline_text_rects[i] = element.to_alipay_dict()
            if hasattr(self.singleline_text_rects, 'to_alipay_dict'):
                params['singleline_text_rects'] = self.singleline_text_rects.to_alipay_dict()
            else:
                params['singleline_text_rects'] = self.singleline_text_rects
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        if self.template_memo:
            if hasattr(self.template_memo, 'to_alipay_dict'):
                params['template_memo'] = self.template_memo.to_alipay_dict()
            else:
                params['template_memo'] = self.template_memo
        if self.template_name:
            if hasattr(self.template_name, 'to_alipay_dict'):
                params['template_name'] = self.template_name.to_alipay_dict()
            else:
                params['template_name'] = self.template_name
        if self.template_source:
            if hasattr(self.template_source, 'to_alipay_dict'):
                params['template_source'] = self.template_source.to_alipay_dict()
            else:
                params['template_source'] = self.template_source
        if self.template_type:
            if hasattr(self.template_type, 'to_alipay_dict'):
                params['template_type'] = self.template_type.to_alipay_dict()
            else:
                params['template_type'] = self.template_type
        if self.time_stamp_rects:
            if isinstance(self.time_stamp_rects, list):
                for i in range(0, len(self.time_stamp_rects)):
                    element = self.time_stamp_rects[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.time_stamp_rects[i] = element.to_alipay_dict()
            if hasattr(self.time_stamp_rects, 'to_alipay_dict'):
                params['time_stamp_rects'] = self.time_stamp_rects.to_alipay_dict()
            else:
                params['time_stamp_rects'] = self.time_stamp_rects
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ContractTemplateOpenVO()
        if 'corporate_seal_rects' in d:
            o.corporate_seal_rects = d['corporate_seal_rects']
        if 'multiline_text_rects' in d:
            o.multiline_text_rects = d['multiline_text_rects']
        if 'must_read' in d:
            o.must_read = d['must_read']
        if 'personal_seal_rects' in d:
            o.personal_seal_rects = d['personal_seal_rects']
        if 'preview_url' in d:
            o.preview_url = d['preview_url']
        if 'singleline_text_rects' in d:
            o.singleline_text_rects = d['singleline_text_rects']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'template_memo' in d:
            o.template_memo = d['template_memo']
        if 'template_name' in d:
            o.template_name = d['template_name']
        if 'template_source' in d:
            o.template_source = d['template_source']
        if 'template_type' in d:
            o.template_type = d['template_type']
        if 'time_stamp_rects' in d:
            o.time_stamp_rects = d['time_stamp_rects']
        return o



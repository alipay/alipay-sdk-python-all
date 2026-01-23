#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCustomerCreditinfoCommentdataSyncModel(object):

    def __init__(self):
        self._comment_desc = None
        self._comment_no = None
        self._comment_source = None
        self._comment_tag = None
        self._has_real_label = None
        self._out_agreement_no = None
        self._real_label = None
        self._user_score = None

    @property
    def comment_desc(self):
        return self._comment_desc

    @comment_desc.setter
    def comment_desc(self, value):
        self._comment_desc = value
    @property
    def comment_no(self):
        return self._comment_no

    @comment_no.setter
    def comment_no(self, value):
        self._comment_no = value
    @property
    def comment_source(self):
        return self._comment_source

    @comment_source.setter
    def comment_source(self, value):
        self._comment_source = value
    @property
    def comment_tag(self):
        return self._comment_tag

    @comment_tag.setter
    def comment_tag(self, value):
        self._comment_tag = value
    @property
    def has_real_label(self):
        return self._has_real_label

    @has_real_label.setter
    def has_real_label(self, value):
        self._has_real_label = value
    @property
    def out_agreement_no(self):
        return self._out_agreement_no

    @out_agreement_no.setter
    def out_agreement_no(self, value):
        self._out_agreement_no = value
    @property
    def real_label(self):
        return self._real_label

    @real_label.setter
    def real_label(self, value):
        if isinstance(value, list):
            self._real_label = list()
            for i in value:
                self._real_label.append(i)
    @property
    def user_score(self):
        return self._user_score

    @user_score.setter
    def user_score(self, value):
        self._user_score = value


    def to_alipay_dict(self):
        params = dict()
        if self.comment_desc:
            if hasattr(self.comment_desc, 'to_alipay_dict'):
                params['comment_desc'] = self.comment_desc.to_alipay_dict()
            else:
                params['comment_desc'] = self.comment_desc
        if self.comment_no:
            if hasattr(self.comment_no, 'to_alipay_dict'):
                params['comment_no'] = self.comment_no.to_alipay_dict()
            else:
                params['comment_no'] = self.comment_no
        if self.comment_source:
            if hasattr(self.comment_source, 'to_alipay_dict'):
                params['comment_source'] = self.comment_source.to_alipay_dict()
            else:
                params['comment_source'] = self.comment_source
        if self.comment_tag:
            if hasattr(self.comment_tag, 'to_alipay_dict'):
                params['comment_tag'] = self.comment_tag.to_alipay_dict()
            else:
                params['comment_tag'] = self.comment_tag
        if self.has_real_label:
            if hasattr(self.has_real_label, 'to_alipay_dict'):
                params['has_real_label'] = self.has_real_label.to_alipay_dict()
            else:
                params['has_real_label'] = self.has_real_label
        if self.out_agreement_no:
            if hasattr(self.out_agreement_no, 'to_alipay_dict'):
                params['out_agreement_no'] = self.out_agreement_no.to_alipay_dict()
            else:
                params['out_agreement_no'] = self.out_agreement_no
        if self.real_label:
            if isinstance(self.real_label, list):
                for i in range(0, len(self.real_label)):
                    element = self.real_label[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.real_label[i] = element.to_alipay_dict()
            if hasattr(self.real_label, 'to_alipay_dict'):
                params['real_label'] = self.real_label.to_alipay_dict()
            else:
                params['real_label'] = self.real_label
        if self.user_score:
            if hasattr(self.user_score, 'to_alipay_dict'):
                params['user_score'] = self.user_score.to_alipay_dict()
            else:
                params['user_score'] = self.user_score
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCustomerCreditinfoCommentdataSyncModel()
        if 'comment_desc' in d:
            o.comment_desc = d['comment_desc']
        if 'comment_no' in d:
            o.comment_no = d['comment_no']
        if 'comment_source' in d:
            o.comment_source = d['comment_source']
        if 'comment_tag' in d:
            o.comment_tag = d['comment_tag']
        if 'has_real_label' in d:
            o.has_real_label = d['has_real_label']
        if 'out_agreement_no' in d:
            o.out_agreement_no = d['out_agreement_no']
        if 'real_label' in d:
            o.real_label = d['real_label']
        if 'user_score' in d:
            o.user_score = d['user_score']
        return o



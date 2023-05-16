#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ScoreDetailInfo import ScoreDetailInfo


class CmtContentBackFlow(object):

    def __init__(self):
        self._cmt_status = None
        self._content = None
        self._out_trade_no = None
        self._pictures = None
        self._score_details = None
        self._total_score = None
        self._total_score_label = None

    @property
    def cmt_status(self):
        return self._cmt_status

    @cmt_status.setter
    def cmt_status(self, value):
        self._cmt_status = value
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def pictures(self):
        return self._pictures

    @pictures.setter
    def pictures(self, value):
        if isinstance(value, list):
            self._pictures = list()
            for i in value:
                self._pictures.append(i)
    @property
    def score_details(self):
        return self._score_details

    @score_details.setter
    def score_details(self, value):
        if isinstance(value, list):
            self._score_details = list()
            for i in value:
                if isinstance(i, ScoreDetailInfo):
                    self._score_details.append(i)
                else:
                    self._score_details.append(ScoreDetailInfo.from_alipay_dict(i))
    @property
    def total_score(self):
        return self._total_score

    @total_score.setter
    def total_score(self, value):
        self._total_score = value
    @property
    def total_score_label(self):
        return self._total_score_label

    @total_score_label.setter
    def total_score_label(self, value):
        if isinstance(value, list):
            self._total_score_label = list()
            for i in value:
                self._total_score_label.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.cmt_status:
            if hasattr(self.cmt_status, 'to_alipay_dict'):
                params['cmt_status'] = self.cmt_status.to_alipay_dict()
            else:
                params['cmt_status'] = self.cmt_status
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.pictures:
            if isinstance(self.pictures, list):
                for i in range(0, len(self.pictures)):
                    element = self.pictures[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pictures[i] = element.to_alipay_dict()
            if hasattr(self.pictures, 'to_alipay_dict'):
                params['pictures'] = self.pictures.to_alipay_dict()
            else:
                params['pictures'] = self.pictures
        if self.score_details:
            if isinstance(self.score_details, list):
                for i in range(0, len(self.score_details)):
                    element = self.score_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.score_details[i] = element.to_alipay_dict()
            if hasattr(self.score_details, 'to_alipay_dict'):
                params['score_details'] = self.score_details.to_alipay_dict()
            else:
                params['score_details'] = self.score_details
        if self.total_score:
            if hasattr(self.total_score, 'to_alipay_dict'):
                params['total_score'] = self.total_score.to_alipay_dict()
            else:
                params['total_score'] = self.total_score
        if self.total_score_label:
            if isinstance(self.total_score_label, list):
                for i in range(0, len(self.total_score_label)):
                    element = self.total_score_label[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.total_score_label[i] = element.to_alipay_dict()
            if hasattr(self.total_score_label, 'to_alipay_dict'):
                params['total_score_label'] = self.total_score_label.to_alipay_dict()
            else:
                params['total_score_label'] = self.total_score_label
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CmtContentBackFlow()
        if 'cmt_status' in d:
            o.cmt_status = d['cmt_status']
        if 'content' in d:
            o.content = d['content']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'pictures' in d:
            o.pictures = d['pictures']
        if 'score_details' in d:
            o.score_details = d['score_details']
        if 'total_score' in d:
            o.total_score = d['total_score']
        if 'total_score_label' in d:
            o.total_score_label = d['total_score_label']
        return o



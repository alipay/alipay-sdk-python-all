#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ReportCommentDetailDTO import ReportCommentDetailDTO


class OpenapiInterviewReportItemDTO(object):

    def __init__(self):
        self._ai_interview_id = None
        self._ai_interview_status = None
        self._report_comment = None
        self._report_comment_all = None
        self._report_score = None
        self._report_url = None

    @property
    def ai_interview_id(self):
        return self._ai_interview_id

    @ai_interview_id.setter
    def ai_interview_id(self, value):
        self._ai_interview_id = value
    @property
    def ai_interview_status(self):
        return self._ai_interview_status

    @ai_interview_status.setter
    def ai_interview_status(self, value):
        self._ai_interview_status = value
    @property
    def report_comment(self):
        return self._report_comment

    @report_comment.setter
    def report_comment(self, value):
        self._report_comment = value
    @property
    def report_comment_all(self):
        return self._report_comment_all

    @report_comment_all.setter
    def report_comment_all(self, value):
        if isinstance(value, list):
            self._report_comment_all = list()
            for i in value:
                if isinstance(i, ReportCommentDetailDTO):
                    self._report_comment_all.append(i)
                else:
                    self._report_comment_all.append(ReportCommentDetailDTO.from_alipay_dict(i))
    @property
    def report_score(self):
        return self._report_score

    @report_score.setter
    def report_score(self, value):
        self._report_score = value
    @property
    def report_url(self):
        return self._report_url

    @report_url.setter
    def report_url(self, value):
        self._report_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.ai_interview_id:
            if hasattr(self.ai_interview_id, 'to_alipay_dict'):
                params['ai_interview_id'] = self.ai_interview_id.to_alipay_dict()
            else:
                params['ai_interview_id'] = self.ai_interview_id
        if self.ai_interview_status:
            if hasattr(self.ai_interview_status, 'to_alipay_dict'):
                params['ai_interview_status'] = self.ai_interview_status.to_alipay_dict()
            else:
                params['ai_interview_status'] = self.ai_interview_status
        if self.report_comment:
            if hasattr(self.report_comment, 'to_alipay_dict'):
                params['report_comment'] = self.report_comment.to_alipay_dict()
            else:
                params['report_comment'] = self.report_comment
        if self.report_comment_all:
            if isinstance(self.report_comment_all, list):
                for i in range(0, len(self.report_comment_all)):
                    element = self.report_comment_all[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.report_comment_all[i] = element.to_alipay_dict()
            if hasattr(self.report_comment_all, 'to_alipay_dict'):
                params['report_comment_all'] = self.report_comment_all.to_alipay_dict()
            else:
                params['report_comment_all'] = self.report_comment_all
        if self.report_score:
            if hasattr(self.report_score, 'to_alipay_dict'):
                params['report_score'] = self.report_score.to_alipay_dict()
            else:
                params['report_score'] = self.report_score
        if self.report_url:
            if hasattr(self.report_url, 'to_alipay_dict'):
                params['report_url'] = self.report_url.to_alipay_dict()
            else:
                params['report_url'] = self.report_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenapiInterviewReportItemDTO()
        if 'ai_interview_id' in d:
            o.ai_interview_id = d['ai_interview_id']
        if 'ai_interview_status' in d:
            o.ai_interview_status = d['ai_interview_status']
        if 'report_comment' in d:
            o.report_comment = d['report_comment']
        if 'report_comment_all' in d:
            o.report_comment_all = d['report_comment_all']
        if 'report_score' in d:
            o.report_score = d['report_score']
        if 'report_url' in d:
            o.report_url = d['report_url']
        return o



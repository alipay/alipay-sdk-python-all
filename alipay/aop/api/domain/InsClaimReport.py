#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsClaimAttachment import InsClaimAttachment
from alipay.aop.api.domain.InsClaim import InsClaim
from alipay.aop.api.domain.InsClaimReportProgress import InsClaimReportProgress
from alipay.aop.api.domain.InsPerson import InsPerson


class InsClaimReport(object):

    def __init__(self):
        self._accident_address = None
        self._accident_desc = None
        self._accident_time = None
        self._attachments = None
        self._biz_data = None
        self._claim_report_no = None
        self._claims = None
        self._progress = None
        self._report_reject_reason = None
        self._reporter = None
        self._status = None

    @property
    def accident_address(self):
        return self._accident_address

    @accident_address.setter
    def accident_address(self, value):
        self._accident_address = value
    @property
    def accident_desc(self):
        return self._accident_desc

    @accident_desc.setter
    def accident_desc(self, value):
        self._accident_desc = value
    @property
    def accident_time(self):
        return self._accident_time

    @accident_time.setter
    def accident_time(self, value):
        self._accident_time = value
    @property
    def attachments(self):
        return self._attachments

    @attachments.setter
    def attachments(self, value):
        if isinstance(value, list):
            self._attachments = list()
            for i in value:
                if isinstance(i, InsClaimAttachment):
                    self._attachments.append(i)
                else:
                    self._attachments.append(InsClaimAttachment.from_alipay_dict(i))
    @property
    def biz_data(self):
        return self._biz_data

    @biz_data.setter
    def biz_data(self, value):
        self._biz_data = value
    @property
    def claim_report_no(self):
        return self._claim_report_no

    @claim_report_no.setter
    def claim_report_no(self, value):
        self._claim_report_no = value
    @property
    def claims(self):
        return self._claims

    @claims.setter
    def claims(self, value):
        if isinstance(value, list):
            self._claims = list()
            for i in value:
                if isinstance(i, InsClaim):
                    self._claims.append(i)
                else:
                    self._claims.append(InsClaim.from_alipay_dict(i))
    @property
    def progress(self):
        return self._progress

    @progress.setter
    def progress(self, value):
        if isinstance(value, list):
            self._progress = list()
            for i in value:
                if isinstance(i, InsClaimReportProgress):
                    self._progress.append(i)
                else:
                    self._progress.append(InsClaimReportProgress.from_alipay_dict(i))
    @property
    def report_reject_reason(self):
        return self._report_reject_reason

    @report_reject_reason.setter
    def report_reject_reason(self, value):
        self._report_reject_reason = value
    @property
    def reporter(self):
        return self._reporter

    @reporter.setter
    def reporter(self, value):
        if isinstance(value, InsPerson):
            self._reporter = value
        else:
            self._reporter = InsPerson.from_alipay_dict(value)
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.accident_address:
            if hasattr(self.accident_address, 'to_alipay_dict'):
                params['accident_address'] = self.accident_address.to_alipay_dict()
            else:
                params['accident_address'] = self.accident_address
        if self.accident_desc:
            if hasattr(self.accident_desc, 'to_alipay_dict'):
                params['accident_desc'] = self.accident_desc.to_alipay_dict()
            else:
                params['accident_desc'] = self.accident_desc
        if self.accident_time:
            if hasattr(self.accident_time, 'to_alipay_dict'):
                params['accident_time'] = self.accident_time.to_alipay_dict()
            else:
                params['accident_time'] = self.accident_time
        if self.attachments:
            if isinstance(self.attachments, list):
                for i in range(0, len(self.attachments)):
                    element = self.attachments[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.attachments[i] = element.to_alipay_dict()
            if hasattr(self.attachments, 'to_alipay_dict'):
                params['attachments'] = self.attachments.to_alipay_dict()
            else:
                params['attachments'] = self.attachments
        if self.biz_data:
            if hasattr(self.biz_data, 'to_alipay_dict'):
                params['biz_data'] = self.biz_data.to_alipay_dict()
            else:
                params['biz_data'] = self.biz_data
        if self.claim_report_no:
            if hasattr(self.claim_report_no, 'to_alipay_dict'):
                params['claim_report_no'] = self.claim_report_no.to_alipay_dict()
            else:
                params['claim_report_no'] = self.claim_report_no
        if self.claims:
            if isinstance(self.claims, list):
                for i in range(0, len(self.claims)):
                    element = self.claims[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.claims[i] = element.to_alipay_dict()
            if hasattr(self.claims, 'to_alipay_dict'):
                params['claims'] = self.claims.to_alipay_dict()
            else:
                params['claims'] = self.claims
        if self.progress:
            if isinstance(self.progress, list):
                for i in range(0, len(self.progress)):
                    element = self.progress[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.progress[i] = element.to_alipay_dict()
            if hasattr(self.progress, 'to_alipay_dict'):
                params['progress'] = self.progress.to_alipay_dict()
            else:
                params['progress'] = self.progress
        if self.report_reject_reason:
            if hasattr(self.report_reject_reason, 'to_alipay_dict'):
                params['report_reject_reason'] = self.report_reject_reason.to_alipay_dict()
            else:
                params['report_reject_reason'] = self.report_reject_reason
        if self.reporter:
            if hasattr(self.reporter, 'to_alipay_dict'):
                params['reporter'] = self.reporter.to_alipay_dict()
            else:
                params['reporter'] = self.reporter
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsClaimReport()
        if 'accident_address' in d:
            o.accident_address = d['accident_address']
        if 'accident_desc' in d:
            o.accident_desc = d['accident_desc']
        if 'accident_time' in d:
            o.accident_time = d['accident_time']
        if 'attachments' in d:
            o.attachments = d['attachments']
        if 'biz_data' in d:
            o.biz_data = d['biz_data']
        if 'claim_report_no' in d:
            o.claim_report_no = d['claim_report_no']
        if 'claims' in d:
            o.claims = d['claims']
        if 'progress' in d:
            o.progress = d['progress']
        if 'report_reject_reason' in d:
            o.report_reject_reason = d['report_reject_reason']
        if 'reporter' in d:
            o.reporter = d['reporter']
        if 'status' in d:
            o.status = d['status']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ReplyRecord import ReplyRecord
from alipay.aop.api.domain.ReplyRecord import ReplyRecord
from alipay.aop.api.domain.AuditEvidenceInfo import AuditEvidenceInfo


class AlipayOpenViolationViolationdetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenViolationViolationdetailQueryResponse, self).__init__()
        self._appeal_dead_line = None
        self._appeal_reply_records = None
        self._can_appeal = None
        self._can_rectify = None
        self._punish_action = None
        self._rectify_dead_line = None
        self._rectify_reply_records = None
        self._status = None
        self._surplus_appeal_cnt = None
        self._surplus_rectify_cnt = None
        self._target_id = None
        self._target_name = None
        self._target_type = None
        self._violation_evidence = None
        self._violation_reason = None
        self._violation_record_id = None
        self._violation_time = None
        self._violation_type = None

    @property
    def appeal_dead_line(self):
        return self._appeal_dead_line

    @appeal_dead_line.setter
    def appeal_dead_line(self, value):
        self._appeal_dead_line = value
    @property
    def appeal_reply_records(self):
        return self._appeal_reply_records

    @appeal_reply_records.setter
    def appeal_reply_records(self, value):
        if isinstance(value, list):
            self._appeal_reply_records = list()
            for i in value:
                if isinstance(i, ReplyRecord):
                    self._appeal_reply_records.append(i)
                else:
                    self._appeal_reply_records.append(ReplyRecord.from_alipay_dict(i))
    @property
    def can_appeal(self):
        return self._can_appeal

    @can_appeal.setter
    def can_appeal(self, value):
        self._can_appeal = value
    @property
    def can_rectify(self):
        return self._can_rectify

    @can_rectify.setter
    def can_rectify(self, value):
        self._can_rectify = value
    @property
    def punish_action(self):
        return self._punish_action

    @punish_action.setter
    def punish_action(self, value):
        if isinstance(value, list):
            self._punish_action = list()
            for i in value:
                self._punish_action.append(i)
    @property
    def rectify_dead_line(self):
        return self._rectify_dead_line

    @rectify_dead_line.setter
    def rectify_dead_line(self, value):
        self._rectify_dead_line = value
    @property
    def rectify_reply_records(self):
        return self._rectify_reply_records

    @rectify_reply_records.setter
    def rectify_reply_records(self, value):
        if isinstance(value, list):
            self._rectify_reply_records = list()
            for i in value:
                if isinstance(i, ReplyRecord):
                    self._rectify_reply_records.append(i)
                else:
                    self._rectify_reply_records.append(ReplyRecord.from_alipay_dict(i))
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def surplus_appeal_cnt(self):
        return self._surplus_appeal_cnt

    @surplus_appeal_cnt.setter
    def surplus_appeal_cnt(self, value):
        self._surplus_appeal_cnt = value
    @property
    def surplus_rectify_cnt(self):
        return self._surplus_rectify_cnt

    @surplus_rectify_cnt.setter
    def surplus_rectify_cnt(self, value):
        self._surplus_rectify_cnt = value
    @property
    def target_id(self):
        return self._target_id

    @target_id.setter
    def target_id(self, value):
        self._target_id = value
    @property
    def target_name(self):
        return self._target_name

    @target_name.setter
    def target_name(self, value):
        self._target_name = value
    @property
    def target_type(self):
        return self._target_type

    @target_type.setter
    def target_type(self, value):
        self._target_type = value
    @property
    def violation_evidence(self):
        return self._violation_evidence

    @violation_evidence.setter
    def violation_evidence(self, value):
        if isinstance(value, list):
            self._violation_evidence = list()
            for i in value:
                if isinstance(i, AuditEvidenceInfo):
                    self._violation_evidence.append(i)
                else:
                    self._violation_evidence.append(AuditEvidenceInfo.from_alipay_dict(i))
    @property
    def violation_reason(self):
        return self._violation_reason

    @violation_reason.setter
    def violation_reason(self, value):
        self._violation_reason = value
    @property
    def violation_record_id(self):
        return self._violation_record_id

    @violation_record_id.setter
    def violation_record_id(self, value):
        self._violation_record_id = value
    @property
    def violation_time(self):
        return self._violation_time

    @violation_time.setter
    def violation_time(self, value):
        self._violation_time = value
    @property
    def violation_type(self):
        return self._violation_type

    @violation_type.setter
    def violation_type(self, value):
        self._violation_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenViolationViolationdetailQueryResponse, self).parse_response_content(response_content)
        if 'appeal_dead_line' in response:
            self.appeal_dead_line = response['appeal_dead_line']
        if 'appeal_reply_records' in response:
            self.appeal_reply_records = response['appeal_reply_records']
        if 'can_appeal' in response:
            self.can_appeal = response['can_appeal']
        if 'can_rectify' in response:
            self.can_rectify = response['can_rectify']
        if 'punish_action' in response:
            self.punish_action = response['punish_action']
        if 'rectify_dead_line' in response:
            self.rectify_dead_line = response['rectify_dead_line']
        if 'rectify_reply_records' in response:
            self.rectify_reply_records = response['rectify_reply_records']
        if 'status' in response:
            self.status = response['status']
        if 'surplus_appeal_cnt' in response:
            self.surplus_appeal_cnt = response['surplus_appeal_cnt']
        if 'surplus_rectify_cnt' in response:
            self.surplus_rectify_cnt = response['surplus_rectify_cnt']
        if 'target_id' in response:
            self.target_id = response['target_id']
        if 'target_name' in response:
            self.target_name = response['target_name']
        if 'target_type' in response:
            self.target_type = response['target_type']
        if 'violation_evidence' in response:
            self.violation_evidence = response['violation_evidence']
        if 'violation_reason' in response:
            self.violation_reason = response['violation_reason']
        if 'violation_record_id' in response:
            self.violation_record_id = response['violation_record_id']
        if 'violation_time' in response:
            self.violation_time = response['violation_time']
        if 'violation_type' in response:
            self.violation_type = response['violation_type']

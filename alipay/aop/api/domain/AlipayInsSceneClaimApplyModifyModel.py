#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsOpenAttachmentDTO import InsOpenAttachmentDTO


class AlipayInsSceneClaimApplyModifyModel(object):

    def __init__(self):
        self._accident_address = None
        self._accident_desc = None
        self._accident_time = None
        self._accident_type = None
        self._accident_type_detail = None
        self._apply_amout = None
        self._attachment_submit_type = None
        self._attachments = None
        self._claim_report_biz_info = None
        self._claim_report_no = None
        self._out_biz_no = None
        self._partner_org_id = None

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
    def accident_type(self):
        return self._accident_type

    @accident_type.setter
    def accident_type(self, value):
        self._accident_type = value
    @property
    def accident_type_detail(self):
        return self._accident_type_detail

    @accident_type_detail.setter
    def accident_type_detail(self, value):
        self._accident_type_detail = value
    @property
    def apply_amout(self):
        return self._apply_amout

    @apply_amout.setter
    def apply_amout(self, value):
        self._apply_amout = value
    @property
    def attachment_submit_type(self):
        return self._attachment_submit_type

    @attachment_submit_type.setter
    def attachment_submit_type(self, value):
        self._attachment_submit_type = value
    @property
    def attachments(self):
        return self._attachments

    @attachments.setter
    def attachments(self, value):
        if isinstance(value, list):
            self._attachments = list()
            for i in value:
                if isinstance(i, InsOpenAttachmentDTO):
                    self._attachments.append(i)
                else:
                    self._attachments.append(InsOpenAttachmentDTO.from_alipay_dict(i))
    @property
    def claim_report_biz_info(self):
        return self._claim_report_biz_info

    @claim_report_biz_info.setter
    def claim_report_biz_info(self, value):
        self._claim_report_biz_info = value
    @property
    def claim_report_no(self):
        return self._claim_report_no

    @claim_report_no.setter
    def claim_report_no(self, value):
        self._claim_report_no = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def partner_org_id(self):
        return self._partner_org_id

    @partner_org_id.setter
    def partner_org_id(self, value):
        self._partner_org_id = value


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
        if self.accident_type:
            if hasattr(self.accident_type, 'to_alipay_dict'):
                params['accident_type'] = self.accident_type.to_alipay_dict()
            else:
                params['accident_type'] = self.accident_type
        if self.accident_type_detail:
            if hasattr(self.accident_type_detail, 'to_alipay_dict'):
                params['accident_type_detail'] = self.accident_type_detail.to_alipay_dict()
            else:
                params['accident_type_detail'] = self.accident_type_detail
        if self.apply_amout:
            if hasattr(self.apply_amout, 'to_alipay_dict'):
                params['apply_amout'] = self.apply_amout.to_alipay_dict()
            else:
                params['apply_amout'] = self.apply_amout
        if self.attachment_submit_type:
            if hasattr(self.attachment_submit_type, 'to_alipay_dict'):
                params['attachment_submit_type'] = self.attachment_submit_type.to_alipay_dict()
            else:
                params['attachment_submit_type'] = self.attachment_submit_type
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
        if self.claim_report_biz_info:
            if hasattr(self.claim_report_biz_info, 'to_alipay_dict'):
                params['claim_report_biz_info'] = self.claim_report_biz_info.to_alipay_dict()
            else:
                params['claim_report_biz_info'] = self.claim_report_biz_info
        if self.claim_report_no:
            if hasattr(self.claim_report_no, 'to_alipay_dict'):
                params['claim_report_no'] = self.claim_report_no.to_alipay_dict()
            else:
                params['claim_report_no'] = self.claim_report_no
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.partner_org_id:
            if hasattr(self.partner_org_id, 'to_alipay_dict'):
                params['partner_org_id'] = self.partner_org_id.to_alipay_dict()
            else:
                params['partner_org_id'] = self.partner_org_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneClaimApplyModifyModel()
        if 'accident_address' in d:
            o.accident_address = d['accident_address']
        if 'accident_desc' in d:
            o.accident_desc = d['accident_desc']
        if 'accident_time' in d:
            o.accident_time = d['accident_time']
        if 'accident_type' in d:
            o.accident_type = d['accident_type']
        if 'accident_type_detail' in d:
            o.accident_type_detail = d['accident_type_detail']
        if 'apply_amout' in d:
            o.apply_amout = d['apply_amout']
        if 'attachment_submit_type' in d:
            o.attachment_submit_type = d['attachment_submit_type']
        if 'attachments' in d:
            o.attachments = d['attachments']
        if 'claim_report_biz_info' in d:
            o.claim_report_biz_info = d['claim_report_biz_info']
        if 'claim_report_no' in d:
            o.claim_report_no = d['claim_report_no']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'partner_org_id' in d:
            o.partner_org_id = d['partner_org_id']
        return o



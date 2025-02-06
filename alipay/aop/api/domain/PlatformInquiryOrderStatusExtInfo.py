#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PlatformInquiryOrderStatusExtInfo(object):

    def __init__(self):
        self._alipay_trade_no = None
        self._cancel_reason = None
        self._chat_url = None
        self._complaint = None
        self._doctor_inquiry_link_page = None
        self._doctor_out_id = None
        self._doctor_out_name = None
        self._doctor_refuse_reason = None
        self._first_reply = None
        self._gmt_adoption = None
        self._gmt_cancel = None
        self._gmt_finished = None
        self._gmt_paid = None
        self._gmt_refund = None
        self._gmt_refund_applying = None
        self._inquiry_complete_status = None
        self._notice = None
        self._real_amount = None
        self._refund_amount = None
        self._refund_reason = None
        self._reject_refund_reason = None
        self._remind_pay = None
        self._reply_content = None
        self._service_end_time = None

    @property
    def alipay_trade_no(self):
        return self._alipay_trade_no

    @alipay_trade_no.setter
    def alipay_trade_no(self, value):
        self._alipay_trade_no = value
    @property
    def cancel_reason(self):
        return self._cancel_reason

    @cancel_reason.setter
    def cancel_reason(self, value):
        self._cancel_reason = value
    @property
    def chat_url(self):
        return self._chat_url

    @chat_url.setter
    def chat_url(self, value):
        self._chat_url = value
    @property
    def complaint(self):
        return self._complaint

    @complaint.setter
    def complaint(self, value):
        self._complaint = value
    @property
    def doctor_inquiry_link_page(self):
        return self._doctor_inquiry_link_page

    @doctor_inquiry_link_page.setter
    def doctor_inquiry_link_page(self, value):
        self._doctor_inquiry_link_page = value
    @property
    def doctor_out_id(self):
        return self._doctor_out_id

    @doctor_out_id.setter
    def doctor_out_id(self, value):
        self._doctor_out_id = value
    @property
    def doctor_out_name(self):
        return self._doctor_out_name

    @doctor_out_name.setter
    def doctor_out_name(self, value):
        self._doctor_out_name = value
    @property
    def doctor_refuse_reason(self):
        return self._doctor_refuse_reason

    @doctor_refuse_reason.setter
    def doctor_refuse_reason(self, value):
        self._doctor_refuse_reason = value
    @property
    def first_reply(self):
        return self._first_reply

    @first_reply.setter
    def first_reply(self, value):
        self._first_reply = value
    @property
    def gmt_adoption(self):
        return self._gmt_adoption

    @gmt_adoption.setter
    def gmt_adoption(self, value):
        self._gmt_adoption = value
    @property
    def gmt_cancel(self):
        return self._gmt_cancel

    @gmt_cancel.setter
    def gmt_cancel(self, value):
        self._gmt_cancel = value
    @property
    def gmt_finished(self):
        return self._gmt_finished

    @gmt_finished.setter
    def gmt_finished(self, value):
        self._gmt_finished = value
    @property
    def gmt_paid(self):
        return self._gmt_paid

    @gmt_paid.setter
    def gmt_paid(self, value):
        self._gmt_paid = value
    @property
    def gmt_refund(self):
        return self._gmt_refund

    @gmt_refund.setter
    def gmt_refund(self, value):
        self._gmt_refund = value
    @property
    def gmt_refund_applying(self):
        return self._gmt_refund_applying

    @gmt_refund_applying.setter
    def gmt_refund_applying(self, value):
        self._gmt_refund_applying = value
    @property
    def inquiry_complete_status(self):
        return self._inquiry_complete_status

    @inquiry_complete_status.setter
    def inquiry_complete_status(self, value):
        self._inquiry_complete_status = value
    @property
    def notice(self):
        return self._notice

    @notice.setter
    def notice(self, value):
        self._notice = value
    @property
    def real_amount(self):
        return self._real_amount

    @real_amount.setter
    def real_amount(self, value):
        self._real_amount = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_reason(self):
        return self._refund_reason

    @refund_reason.setter
    def refund_reason(self, value):
        self._refund_reason = value
    @property
    def reject_refund_reason(self):
        return self._reject_refund_reason

    @reject_refund_reason.setter
    def reject_refund_reason(self, value):
        self._reject_refund_reason = value
    @property
    def remind_pay(self):
        return self._remind_pay

    @remind_pay.setter
    def remind_pay(self, value):
        self._remind_pay = value
    @property
    def reply_content(self):
        return self._reply_content

    @reply_content.setter
    def reply_content(self, value):
        self._reply_content = value
    @property
    def service_end_time(self):
        return self._service_end_time

    @service_end_time.setter
    def service_end_time(self, value):
        self._service_end_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_trade_no:
            if hasattr(self.alipay_trade_no, 'to_alipay_dict'):
                params['alipay_trade_no'] = self.alipay_trade_no.to_alipay_dict()
            else:
                params['alipay_trade_no'] = self.alipay_trade_no
        if self.cancel_reason:
            if hasattr(self.cancel_reason, 'to_alipay_dict'):
                params['cancel_reason'] = self.cancel_reason.to_alipay_dict()
            else:
                params['cancel_reason'] = self.cancel_reason
        if self.chat_url:
            if hasattr(self.chat_url, 'to_alipay_dict'):
                params['chat_url'] = self.chat_url.to_alipay_dict()
            else:
                params['chat_url'] = self.chat_url
        if self.complaint:
            if hasattr(self.complaint, 'to_alipay_dict'):
                params['complaint'] = self.complaint.to_alipay_dict()
            else:
                params['complaint'] = self.complaint
        if self.doctor_inquiry_link_page:
            if hasattr(self.doctor_inquiry_link_page, 'to_alipay_dict'):
                params['doctor_inquiry_link_page'] = self.doctor_inquiry_link_page.to_alipay_dict()
            else:
                params['doctor_inquiry_link_page'] = self.doctor_inquiry_link_page
        if self.doctor_out_id:
            if hasattr(self.doctor_out_id, 'to_alipay_dict'):
                params['doctor_out_id'] = self.doctor_out_id.to_alipay_dict()
            else:
                params['doctor_out_id'] = self.doctor_out_id
        if self.doctor_out_name:
            if hasattr(self.doctor_out_name, 'to_alipay_dict'):
                params['doctor_out_name'] = self.doctor_out_name.to_alipay_dict()
            else:
                params['doctor_out_name'] = self.doctor_out_name
        if self.doctor_refuse_reason:
            if hasattr(self.doctor_refuse_reason, 'to_alipay_dict'):
                params['doctor_refuse_reason'] = self.doctor_refuse_reason.to_alipay_dict()
            else:
                params['doctor_refuse_reason'] = self.doctor_refuse_reason
        if self.first_reply:
            if hasattr(self.first_reply, 'to_alipay_dict'):
                params['first_reply'] = self.first_reply.to_alipay_dict()
            else:
                params['first_reply'] = self.first_reply
        if self.gmt_adoption:
            if hasattr(self.gmt_adoption, 'to_alipay_dict'):
                params['gmt_adoption'] = self.gmt_adoption.to_alipay_dict()
            else:
                params['gmt_adoption'] = self.gmt_adoption
        if self.gmt_cancel:
            if hasattr(self.gmt_cancel, 'to_alipay_dict'):
                params['gmt_cancel'] = self.gmt_cancel.to_alipay_dict()
            else:
                params['gmt_cancel'] = self.gmt_cancel
        if self.gmt_finished:
            if hasattr(self.gmt_finished, 'to_alipay_dict'):
                params['gmt_finished'] = self.gmt_finished.to_alipay_dict()
            else:
                params['gmt_finished'] = self.gmt_finished
        if self.gmt_paid:
            if hasattr(self.gmt_paid, 'to_alipay_dict'):
                params['gmt_paid'] = self.gmt_paid.to_alipay_dict()
            else:
                params['gmt_paid'] = self.gmt_paid
        if self.gmt_refund:
            if hasattr(self.gmt_refund, 'to_alipay_dict'):
                params['gmt_refund'] = self.gmt_refund.to_alipay_dict()
            else:
                params['gmt_refund'] = self.gmt_refund
        if self.gmt_refund_applying:
            if hasattr(self.gmt_refund_applying, 'to_alipay_dict'):
                params['gmt_refund_applying'] = self.gmt_refund_applying.to_alipay_dict()
            else:
                params['gmt_refund_applying'] = self.gmt_refund_applying
        if self.inquiry_complete_status:
            if hasattr(self.inquiry_complete_status, 'to_alipay_dict'):
                params['inquiry_complete_status'] = self.inquiry_complete_status.to_alipay_dict()
            else:
                params['inquiry_complete_status'] = self.inquiry_complete_status
        if self.notice:
            if hasattr(self.notice, 'to_alipay_dict'):
                params['notice'] = self.notice.to_alipay_dict()
            else:
                params['notice'] = self.notice
        if self.real_amount:
            if hasattr(self.real_amount, 'to_alipay_dict'):
                params['real_amount'] = self.real_amount.to_alipay_dict()
            else:
                params['real_amount'] = self.real_amount
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.refund_reason:
            if hasattr(self.refund_reason, 'to_alipay_dict'):
                params['refund_reason'] = self.refund_reason.to_alipay_dict()
            else:
                params['refund_reason'] = self.refund_reason
        if self.reject_refund_reason:
            if hasattr(self.reject_refund_reason, 'to_alipay_dict'):
                params['reject_refund_reason'] = self.reject_refund_reason.to_alipay_dict()
            else:
                params['reject_refund_reason'] = self.reject_refund_reason
        if self.remind_pay:
            if hasattr(self.remind_pay, 'to_alipay_dict'):
                params['remind_pay'] = self.remind_pay.to_alipay_dict()
            else:
                params['remind_pay'] = self.remind_pay
        if self.reply_content:
            if hasattr(self.reply_content, 'to_alipay_dict'):
                params['reply_content'] = self.reply_content.to_alipay_dict()
            else:
                params['reply_content'] = self.reply_content
        if self.service_end_time:
            if hasattr(self.service_end_time, 'to_alipay_dict'):
                params['service_end_time'] = self.service_end_time.to_alipay_dict()
            else:
                params['service_end_time'] = self.service_end_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PlatformInquiryOrderStatusExtInfo()
        if 'alipay_trade_no' in d:
            o.alipay_trade_no = d['alipay_trade_no']
        if 'cancel_reason' in d:
            o.cancel_reason = d['cancel_reason']
        if 'chat_url' in d:
            o.chat_url = d['chat_url']
        if 'complaint' in d:
            o.complaint = d['complaint']
        if 'doctor_inquiry_link_page' in d:
            o.doctor_inquiry_link_page = d['doctor_inquiry_link_page']
        if 'doctor_out_id' in d:
            o.doctor_out_id = d['doctor_out_id']
        if 'doctor_out_name' in d:
            o.doctor_out_name = d['doctor_out_name']
        if 'doctor_refuse_reason' in d:
            o.doctor_refuse_reason = d['doctor_refuse_reason']
        if 'first_reply' in d:
            o.first_reply = d['first_reply']
        if 'gmt_adoption' in d:
            o.gmt_adoption = d['gmt_adoption']
        if 'gmt_cancel' in d:
            o.gmt_cancel = d['gmt_cancel']
        if 'gmt_finished' in d:
            o.gmt_finished = d['gmt_finished']
        if 'gmt_paid' in d:
            o.gmt_paid = d['gmt_paid']
        if 'gmt_refund' in d:
            o.gmt_refund = d['gmt_refund']
        if 'gmt_refund_applying' in d:
            o.gmt_refund_applying = d['gmt_refund_applying']
        if 'inquiry_complete_status' in d:
            o.inquiry_complete_status = d['inquiry_complete_status']
        if 'notice' in d:
            o.notice = d['notice']
        if 'real_amount' in d:
            o.real_amount = d['real_amount']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'refund_reason' in d:
            o.refund_reason = d['refund_reason']
        if 'reject_refund_reason' in d:
            o.reject_refund_reason = d['reject_refund_reason']
        if 'remind_pay' in d:
            o.remind_pay = d['remind_pay']
        if 'reply_content' in d:
            o.reply_content = d['reply_content']
        if 'service_end_time' in d:
            o.service_end_time = d['service_end_time']
        return o



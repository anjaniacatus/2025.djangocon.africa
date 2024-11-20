from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import get_object_or_404
from . import models
from . import forms


@login_required
def my_proposals(request):
    """show a list of talk proposals for the current logged-in user"""
    proposals = models.Proposal.objects.filter(user=request.user)

    context = {"proposals": proposals}

    return render(request, "proposals/my_proposals.html", context)


@login_required
def action_delete_my_proposal(request, proposal_id):

    proposal = get_object_or_404(models.Proposal, pk=proposal_id)
    if proposal.user != request.user:
        raise Http404("Proposal does not exist")
    proposal.delete()

    proposals = models.Proposal.objects.filter(user=request.user)

    context = {"proposals": proposals}
    return render(request, "proposals/my_proposals.html#table_body", context)


@login_required
def create_proposal(request):
    form = forms.ProposalForm()
    context = {"form": form}
    return render(request, "proposals/create_proposal.html", context)

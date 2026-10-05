from django.db import models


class Service(models.Model):
    number = models.CharField(max_length=5, help_text="e.g. 01, 02, 03")
    slug = models.SlugField(unique=True, help_text="Used in the URL, e.g. 'custom-software'")
    title = models.CharField(max_length=100)
    summary = models.TextField(help_text="Short description shown on the homepage card")
    details = models.TextField(
        help_text="Full overview paragraphs. Separate each paragraph with a blank line."
    )
    features = models.TextField(
        help_text="What's included list. Put one feature per line."
    )
    order = models.PositiveIntegerField(default=0, help_text="Controls display order (lower = first)")

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.title

    def details_list(self):
        """Split details into paragraphs for the template."""
        return [p.strip() for p in self.details.split('\n\n') if p.strip()]

    def features_list(self):
        """Split features into a list for the template."""
        return [f.strip() for f in self.features.split('\n') if f.strip()]


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    company = models.CharField(max_length=150, blank=True)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False, help_text="Mark as read once you've followed up")

    class Meta:
        ordering = ['-submitted_at'] 

    def __str__(self):
        return f"{self.name} — {self.submitted_at.strftime('%Y-%m-%d')}"
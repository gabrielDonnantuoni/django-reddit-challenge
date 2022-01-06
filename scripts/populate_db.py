#  To paste to django shell:
#  exec(open('scripts/populate_db.py').read())


from topics.models import Topic
from posts.models import Tag, Post
from comments.models import Comment
from accounts.models import User
from rest_framework.authtoken.models import Token


###
# Create users
###
user1, was_created = User.objects.get_or_create(
    username='user1',
    defaults={
        'email': 'user1@gmail.com',
    },
)
if was_created:
    user1.set_password('12345678')
    user1.save()

Token.objects.get_or_create(user=user1)


user2, was_created = User.objects.get_or_create(
    username='user2',
    defaults={
        'email': 'user2@gmail.com',
    },
)
if was_created:
    user2.set_password('12345678')
    user2.save()

Token.objects.get_or_create(user=user2)


user3, was_created = User.objects.get_or_create(
    username='user3',
    defaults={
        'email': 'user3@gmail.com',
    },
)
if was_created:
    user3.set_password('12345678')
    user3.save()

Token.objects.get_or_create(user=user3)


###
# Create topics
###
gaming, _ = Topic.objects.get_or_create(
    slug='gaming',
    title='Gaming topic',
    description='Gaming description',
    author=user1,
)
healthy_lifestyle, _ = Topic.objects.get_or_create(
    slug='healthy-lifestyle',
    title='Healthy lifestyle topic',
    description='Healthy lifestyle description',
    author=user1,
)
sports, _ = Topic.objects.get_or_create(
    slug='sports',
    title='Sports topic',
    description='Sports description',
    author=user1,
)
marvel, _ = Topic.objects.get_or_create(
    slug='marvel',
    title='Marvel topic',
    description='Marvel description',
    author=user2,
)
dc, _ = Topic.objects.get_or_create(
    slug='dc',
    title='DC topic',
    description='DC description',
    author=user2,
)
cooking, _ = Topic.objects.get_or_create(
    slug='cooking',
    title='Cooking topic',
    description='Cooking description',
    author=user3,
)


###
# Create tags
###
clip, _ = Tag.objects.get_or_create(name='Clip')
merchandise, _ = Tag.objects.get_or_create(name='Merchandise')
promotional, _ = Tag.objects.get_or_create(name='Promotional')
discussion, _ = Tag.objects.get_or_create(name='Discussion')
theory, _ = Tag.objects.get_or_create(name='Theory')
article, _ = Tag.objects.get_or_create(name='Article')
rumour, _ = Tag.objects.get_or_create(name='Rumour')
question, _ = Tag.objects.get_or_create(name='Question')


###
# Create posts
###
game_post, was_created = Post.objects.get_or_create(
    title='What do you think about games?',
    content='I was wondering if I should start playing eletronic games.',
    author=user1,
    topic=gaming,
)
if was_created:
    game_post.tags.add(question, article)
    game_post.up_votes.add(user2, user3)

egg_post, was_created = Post.objects.get_or_create(
    title='Is egg one of the greatest food?',
    content='Someone told me that eggs are great for health, is this true?',
    author=user1,
    topic=healthy_lifestyle,
)
if was_created:
    egg_post.tags.add(question, discussion)

marvel_post, was_created = Post.objects.get_or_create(
    title='Spider man: No way home is awesome',
    content='Do someone do not agree with it?',
    author=user2,
    topic=marvel,
)
if was_created:
    marvel_post.tags.add(question, discussion)

cook_post, was_created = Post.objects.get_or_create(
    title='Cookies 50% off',
    content=(
        'I am selling this nice chocolate cookies with 50% off, who '
        'is interested?'
    ),
    author=user3,
    topic=cooking,
)
if was_created:
    cook_post.tags.add(promotional)
    cook_post.down_votes.add(user1, user2)

###
# Create comments
###

# Game ones
game_c1, _ = Comment.objects.get_or_create(
    content=(
        'Man, if you go for the right ones, you will definitely '
        ' have a greate time.'
    ),
    parent_comment=None,
    author=user2,
    post=game_post,
)

game_c2, _ = Comment.objects.get_or_create(
    content=(
        'You should try League of Legends, if you have really free time.'
    ),
    parent_comment=None,
    author=user3,
    post=game_post,
)

game_c3, _ = Comment.objects.get_or_create(
    content=(
        'What do you call the right ones?'
    ),
    parent_comment=game_c1,
    author=user1,
    post=game_post,
)

game_c4, _ = Comment.objects.get_or_create(
    content=(
        'It really dependes on the genre you like.'
    ),
    parent_comment=game_c1,
    author=user2,
    post=game_post,
)

# Marvel ones
marvel_c1, _ = Comment.objects.get_or_create(
    content=(
        'I disagree, it should be much better.'
    ),
    parent_comment=None,
    author=user1,
    post=marvel_post,
)

marvel_c2, _ = Comment.objects.get_or_create(
    content=(
        'I have never seen such a good movie like it.'
    ),
    parent_comment=None,
    author=user3,
    post=marvel_post,
)

marvel_c3, _ = Comment.objects.get_or_create(
    content=(
        'Do you have at least one argument for it?'
    ),
    parent_comment=marvel_c1,
    author=user3,
    post=marvel_post,
)

marvel_c4, _ = Comment.objects.get_or_create(
    content=(
        'Yes, it is boring.'
    ),
    parent_comment=marvel_c3,
    author=user1,
    post=marvel_post,
)

marvel_c5, _ = Comment.objects.get_or_create(
    content=(
        'Oww, well explained!'
    ),
    parent_comment=marvel_c4,
    author=user3,
    post=marvel_post,
)

# Cook ones
cook_c1, _ = Comment.objects.get_or_create(
    content=(
        'I think this topic should not be used for sales.'
    ),
    parent_comment=None,
    author=user1,
    post=cook_post,
)

cook_c2, _ = Comment.objects.get_or_create(
    content=(
        'Totally agree.'
    ),
    parent_comment=cook_c1,
    author=user1,
    post=cook_post,
)
